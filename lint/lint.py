#!/usr/bin/env python3
"""TMF Knowledge Base linter.

Walks wiki/ and validates pages against the constitution in CLAUDE.md.
Run from anywhere: `python lint/lint.py` or `python3 lint/lint.py`.

Exit codes:
  0 — pass (no errors; warnings allowed)
  1 — lint failure (one or more errors)
  2 — environment error (missing PyYAML, missing wiki/, etc.)

Rules are documented in lint/lint_checks.md.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ─── Paths ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
RAW_ROOT = REPO_ROOT / "raw"


# ─── Schema constants (from CLAUDE.md §5, §6, §7) ─────────────────────────────

REQUIRED_FRONTMATTER: dict[str, list[str]] = {
    "etom-l2": ["type", "spec_id", "spec_version", "retrieval_date",
                "source_paths", "l1_parent", "l2_id", "l2_name"],
    "sid-abe": ["type", "spec_id", "spec_version", "retrieval_date",
                "source_paths", "abe_category", "entity_name"],
    "oda-component": ["type", "spec_id", "spec_version", "retrieval_date",
                      "source_paths", "oda_domain", "component_id", "component_name"],
    "foundation": ["type", "spec_id", "spec_version", "retrieval_date",
                   "source_paths", "concept_category", "title"],
    "view": ["type", "derived_from"],
}

REQUIRED_HEADINGS: dict[str, list[str]] = {
    "etom-l2": [
        "Overview",
        "L3 Processes",
        "SID Entities Manipulated",
        "ODA Components That Realise This Process",
        "Open Questions",
    ],
    "sid-abe": [
        "Overview",
        "Key Attributes",
        "Relationships",
        "ODA Components That Own This Entity",
        "eTOM Processes That Manipulate This Entity",
        "Open Questions",
    ],
    "oda-component": [
        "Overview",
        "Responsibilities",
        "SID Entities Owned",
        "eTOM Processes Realised",
        "Component Dependencies",
        "Open Questions",
    ],
    "foundation": [
        "Overview",
        "Cross-Framework Application",
        "Open Questions",
    ],
    "view": [
        "Purpose",
        "Source Pages",
    ],
}

# Sections that participate in trilateral linking (eTOM ↔ SID ↔ ODA), per page type.
# Component Dependencies on oda-component is intentionally excluded — it is within-ODA
# navigation, not trilateral.
TRILATERAL_SECTIONS: dict[str, list[str]] = {
    "etom-l2": ["SID Entities Manipulated", "ODA Components That Realise This Process"],
    "sid-abe": ["ODA Components That Own This Entity",
                "eTOM Processes That Manipulate This Entity"],
    "oda-component": ["SID Entities Owned", "eTOM Processes Realised"],
    "foundation": [],
    "view": [],
}

# Reciprocal section: link from A's section X must be returned in B's section Y.
RECIPROCAL: dict[str, str] = {
    # eTOM ↔ SID
    "SID Entities Manipulated": "eTOM Processes That Manipulate This Entity",
    "eTOM Processes That Manipulate This Entity": "SID Entities Manipulated",
    # eTOM ↔ ODA
    "ODA Components That Realise This Process": "eTOM Processes Realised",
    "eTOM Processes Realised": "ODA Components That Realise This Process",
    # SID ↔ ODA
    "ODA Components That Own This Entity": "SID Entities Owned",
    "SID Entities Owned": "ODA Components That Own This Entity",
}

# Files that exist but are not subject to type-based anatomy/frontmatter checks.
EXEMPT_RELATIVE_PATHS: set[str] = {
    "wiki/index.md",
    "wiki/log.md",
    "wiki/open-questions.md",
    "wiki/sid/product-abe.md",
    "wiki/sid/service-abe.md",
    "wiki/sid/resource-abe.md",
    "wiki/sid/common-abe.md",
}


# ─── Regexes ──────────────────────────────────────────────────────────────────

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
OQ_REF_RE = re.compile(r"OQ-(\d{3,})")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)

# Strip fenced code blocks and inline code spans before searching for wikilinks.
# Wikilinks inside code (e.g. `[[wiki/...]]` as syntax illustration) are not real
# links and must not register as broken or as satisfying trilateral requirements.
FENCED_CODE_RE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans for wikilink scanning."""
    text = FENCED_CODE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


# ─── Types ────────────────────────────────────────────────────────────────────

@dataclass
class Page:
    path: Path
    relative_path: str
    frontmatter: dict
    body: str
    headings: list[tuple[int, str]]
    yaml_error: Optional[str] = None

    @property
    def page_type(self) -> Optional[str]:
        return self.frontmatter.get("type") if isinstance(self.frontmatter, dict) else None

    @property
    def is_exempt(self) -> bool:
        return self.relative_path in EXEMPT_RELATIVE_PATHS or self.path.name == "_index.md"


@dataclass
class Finding:
    path: str
    severity: str  # "error" | "warning"
    rule: str
    message: str

    def render(self) -> str:
        return f"  [{self.severity.upper():<7}] {self.rule:<14} {self.message}"


# ─── Parsing ──────────────────────────────────────────────────────────────────

def parse_page(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(REPO_ROOT))
    m = FRONTMATTER_RE.match(text)
    if not m:
        return Page(path=path, relative_path=rel, frontmatter={}, body=text,
                    headings=parse_headings(text))
    fm_text, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(fm_text) or {}
        if not isinstance(fm, dict):
            fm = {}
        return Page(path=path, relative_path=rel, frontmatter=fm, body=body,
                    headings=parse_headings(body))
    except yaml.YAMLError as e:
        return Page(path=path, relative_path=rel, frontmatter={}, body=body,
                    headings=parse_headings(body), yaml_error=str(e))


def parse_headings(body: str) -> list[tuple[int, str]]:
    return [(len(m.group(1)), m.group(2)) for m in HEADING_RE.finditer(body)]


def get_section_body(body: str, heading: str) -> Optional[str]:
    """Return the text under '## {heading}' up to the next ## of equal/lower depth or EOF."""
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(body)
    return m.group(1) if m else None


def normalise_wikilink_target(target: str) -> str:
    """Strip anchor/.md/whitespace, return '<path>.md'."""
    target = target.strip().split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target + ".md"


def collect_pages() -> list[Page]:
    pages = []
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        pages.append(parse_page(path))
    return pages


def known_wiki_paths() -> set[str]:
    """All paths a wikilink may legitimately resolve to."""
    paths: set[str] = set()
    for p in WIKI_ROOT.rglob("*.md"):
        paths.add(str(p.relative_to(REPO_ROOT)))
    paths.add("CLAUDE.md")
    paths.add("templates/README.md")
    return paths


# ─── Lint rules ───────────────────────────────────────────────────────────────

def lint_frontmatter(page: Page) -> list[Finding]:
    findings: list[Finding] = []
    if page.is_exempt:
        return findings
    if page.yaml_error:
        findings.append(Finding(page.relative_path, "error", "FM-PARSE",
                                f"YAML parse error: {page.yaml_error}"))
        return findings
    fm = page.frontmatter
    if not fm:
        findings.append(Finding(page.relative_path, "error", "FM-MISSING",
                                "Missing frontmatter block"))
        return findings
    page_type = fm.get("type")
    if page_type not in REQUIRED_FRONTMATTER:
        findings.append(Finding(page.relative_path, "error", "FM-TYPE",
                                f"Invalid or missing 'type': {page_type!r}. "
                                f"Allowed: {sorted(REQUIRED_FRONTMATTER)}"))
        return findings
    for field in REQUIRED_FRONTMATTER[page_type]:
        if field not in fm:
            findings.append(Finding(page.relative_path, "error", "FM-FIELD",
                                    f"Missing required field: {field}"))
        elif fm[field] in (None, "", []):
            findings.append(Finding(page.relative_path, "error", "FM-EMPTY",
                                    f"Empty value for required field: {field}"))
    if "source_paths" in fm and fm["source_paths"] is not None and not isinstance(fm["source_paths"], list):
        findings.append(Finding(page.relative_path, "error", "FM-LIST",
                                "source_paths must be a YAML list"))
    if "source_extract_paths" in fm and fm["source_extract_paths"] is not None and not isinstance(fm["source_extract_paths"], list):
        findings.append(Finding(page.relative_path, "error", "FM-LIST",
                                "source_extract_paths must be a YAML list"))
    if "derived_from" in fm and fm["derived_from"] is not None and not isinstance(fm["derived_from"], list):
        findings.append(Finding(page.relative_path, "error", "FM-LIST",
                                "derived_from must be a YAML list"))
    return findings


def lint_anatomy(page: Page) -> list[Finding]:
    findings: list[Finding] = []
    if page.is_exempt:
        return findings
    page_type = page.page_type
    if page_type not in REQUIRED_HEADINGS:
        return findings  # FM-TYPE already raised
    required = REQUIRED_HEADINGS[page_type]
    h2s = [text for (level, text) in page.headings if level == 2]
    cursor = 0
    for req in required:
        try:
            idx = h2s.index(req, cursor)
            cursor = idx + 1
        except ValueError:
            findings.append(Finding(page.relative_path, "error", "ANAT-SECTION",
                                    f"Missing or out-of-order required section: ## {req}"))
    h1s = [text for (level, text) in page.headings if level == 1]
    if not h1s:
        findings.append(Finding(page.relative_path, "error", "ANAT-TITLE",
                                "Missing H1 title"))
    elif len(h1s) > 1:
        findings.append(Finding(page.relative_path, "error", "ANAT-TITLE",
                                f"Multiple H1 titles: {h1s}"))
    if "{{" in page.body and "}}" in page.body:
        findings.append(Finding(page.relative_path, "warning", "ANAT-PLACEHOLDER",
                                "Page contains unfilled {{placeholders}}"))
    return findings


def lint_trilateral(page: Page) -> list[Finding]:
    findings: list[Finding] = []
    if page.is_exempt:
        return findings
    page_type = page.page_type
    if page_type not in TRILATERAL_SECTIONS or not TRILATERAL_SECTIONS[page_type]:
        return findings
    for section in TRILATERAL_SECTIONS[page_type]:
        body = get_section_body(page.body, section)
        if body is None:
            continue  # already raised by ANAT-SECTION
        scannable = strip_code(body)
        has_link = bool(WIKILINK_RE.search(scannable))
        has_oq = bool(OQ_REF_RE.search(scannable))
        if not has_link and not has_oq:
            findings.append(Finding(page.relative_path, "error", "TRI-EMPTY",
                                    f"'## {section}' has neither a wikilink nor an OQ-NNN reference"))
    return findings


def lint_wikilinks(page: Page, known_paths: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for m in WIKILINK_RE.finditer(strip_code(page.body)):
        raw_target = m.group(1).strip()
        target_no_anchor = raw_target.split("#", 1)[0].strip()
        if not target_no_anchor:
            continue  # in-page anchor
        resolved = normalise_wikilink_target(target_no_anchor)
        if resolved not in known_paths:
            findings.append(Finding(page.relative_path, "error", "LINK-BROKEN",
                                    f"Wikilink target does not resolve: [[{raw_target}]]"))
    return findings


def lint_source_paths(page: Page) -> list[Finding]:
    findings: list[Finding] = []
    if page.is_exempt:
        return findings
    fm = page.frontmatter
    for key, severity in (("source_paths", "error"), ("source_extract_paths", "warning")):
        paths = fm.get(key)
        if not isinstance(paths, list):
            continue
        for p in paths:
            if p in (None, ""):
                continue
            full = REPO_ROOT / str(p)
            if not full.exists():
                findings.append(Finding(page.relative_path, severity, "SRC-MISSING",
                                        f"{key} entry does not exist: {p}"))
    return findings


def build_link_index(pages: list[Page]) -> dict[tuple[str, str], set[str]]:
    """Map (page_path, section_name) -> set of resolved wikilink targets."""
    index: dict[tuple[str, str], set[str]] = {}
    for page in pages:
        if page.is_exempt:
            continue
        page_type = page.page_type
        for section in TRILATERAL_SECTIONS.get(page_type, []):
            body = get_section_body(page.body, section)
            if body is None:
                continue
            targets = {
                normalise_wikilink_target(m.group(1).split("#", 1)[0])
                for m in WIKILINK_RE.finditer(strip_code(body))
            }
            index[(page.relative_path, section)] = targets
    return index


def lint_bidirectional(pages: list[Page],
                        link_index: dict[tuple[str, str], set[str]]) -> list[Finding]:
    findings: list[Finding] = []
    pages_by_path = {p.relative_path: p for p in pages}
    for (src_path, src_section), targets in link_index.items():
        recip_section = RECIPROCAL.get(src_section)
        if not recip_section:
            continue
        for target_path in targets:
            target_page = pages_by_path.get(target_path)
            if target_page is None:
                continue  # unresolved link already flagged elsewhere
            if target_page.is_exempt:
                continue  # exempt pages have no anatomy/reciprocal sections
            recip_body = get_section_body(target_page.body, recip_section)
            if recip_body is None:
                findings.append(Finding(target_path, "error", "BI-NO-SECTION",
                                        f"Reciprocal section '## {recip_section}' missing "
                                        f"(needed by link from {src_path})"))
                continue
            recip_targets = {
                normalise_wikilink_target(m.group(1).split("#", 1)[0])
                for m in WIKILINK_RE.finditer(strip_code(recip_body))
            }
            if src_path not in recip_targets:
                findings.append(Finding(target_path, "error", "BI-MISSING",
                                        f"No reciprocal link to {src_path} "
                                        f"in '## {recip_section}'"))
    return findings


def lint_log_freshness(pages: list[Page]) -> list[Finding]:
    findings: list[Finding] = []
    log_path = WIKI_ROOT / "log.md"
    if not log_path.exists():
        findings.append(Finding("wiki/log.md", "error", "LOG-MISSING",
                                "wiki/log.md does not exist"))
        return findings
    typed_pages = [p for p in pages if not p.is_exempt]
    if not typed_pages:
        return findings  # nothing has been ingested; vacuously fresh
    log_mtime = log_path.stat().st_mtime
    stale = [p for p in typed_pages if p.path.stat().st_mtime > log_mtime + 5]
    if stale:
        findings.append(Finding("wiki/log.md", "warning", "LOG-STALE",
                                f"{len(stale)} page(s) modified after log.md "
                                f"(first: {stale[0].relative_path}); log entry may be missing"))
    return findings


def lint_oq_references(pages: list[Page]) -> list[Finding]:
    findings: list[Finding] = []
    oq_path = WIKI_ROOT / "open-questions.md"
    if not oq_path.exists():
        findings.append(Finding("wiki/open-questions.md", "error", "OQ-FILE",
                                "wiki/open-questions.md does not exist"))
        return findings
    oq_text = oq_path.read_text(encoding="utf-8")
    declared = set(OQ_REF_RE.findall(oq_text))
    for page in pages:
        for ref in set(OQ_REF_RE.findall(page.body)):
            if ref not in declared:
                findings.append(Finding(page.relative_path, "warning", "OQ-NOT-FOUND",
                                        f"References OQ-{ref} but no entry "
                                        f"found in open-questions.md"))
    return findings


# ─── Driver ───────────────────────────────────────────────────────────────────

def main() -> int:
    if not WIKI_ROOT.exists():
        print(f"ERROR: wiki/ not found at {WIKI_ROOT}", file=sys.stderr)
        return 2
    pages = collect_pages()
    known_paths = known_wiki_paths()

    findings: list[Finding] = []
    for page in pages:
        findings.extend(lint_frontmatter(page))
        findings.extend(lint_anatomy(page))
        findings.extend(lint_trilateral(page))
        findings.extend(lint_wikilinks(page, known_paths))
        findings.extend(lint_source_paths(page))
    link_index = build_link_index(pages)
    findings.extend(lint_bidirectional(pages, link_index))
    findings.extend(lint_log_freshness(pages))
    findings.extend(lint_oq_references(pages))

    n_errors = sum(1 for f in findings if f.severity == "error")
    n_warnings = sum(1 for f in findings if f.severity == "warning")

    if not findings:
        print(f"PASS — {len(pages)} page(s) checked, 0 findings.")
        return 0

    by_path: dict[str, list[Finding]] = {}
    for f in findings:
        by_path.setdefault(f.path, []).append(f)
    for path in sorted(by_path):
        print(f"\n{path}")
        for f in by_path[path]:
            print(f.render())
    print(f"\n{'-' * 60}")
    print(f"{n_errors} error(s), {n_warnings} warning(s) "
          f"across {len(by_path)} file(s); {len(pages)} pages checked.")
    return 1 if n_errors else 0


if __name__ == "__main__":
    sys.exit(main())
