#!/usr/bin/env python3
"""
One-shot script to:
1. Remove the obvious domain-header .desc lines added in the prior iteration.
2. Add a .l2-desc line to each L2 capability box across all 3 HTML files.
3. Insert a CSS rule for .l2 .l2-desc styling.

Source-faithful condensations of each L2's GB921 v25.5 Extended Description,
keyed by L2 ID. Verbatim discipline (CLAUDE.md §1) — these are condensations,
not paraphrases of normative content.

Run from anywhere; targets the three HTML files in this directory.
"""
import re
from pathlib import Path

DIR = Path(__file__).parent

# {l2_id: description (single sentence, no surrounding punctuation)}
DESCRIPTIONS = {
    # ----- S2R area -----
    # Strategy Management
    "1.4.1":  "Annual and multi-year strategic plans for services and service directions",
    "1.5.1":  "Annual and multi-year resource strategies; v25.5 carries AI-readiness guidance",
    # Capability Management
    "1.4.2":  "Plan and deliver new and enhanced service capabilities (project-driven)",
    "1.5.2":  "Deploy new and enhanced technology and resources; logical and physical",
    "1.4.12": "Plan / forecast / optimize service capacity vs SLA / SLO / SLR",
    "1.5.14": "Plan / forecast / optimize resource capacity vs business objectives",
    "1.4.16": "Design the catalog scheme; define the Service Catalog Specification",
    "1.5.18": "Design the catalog scheme; define the Resource Catalog Specification",
    "1.4.19": "Describe / model / analyze service specification artefacts (ongoing maintenance)",
    "1.5.19": "Develop / master / analyze + version Resource Specifications (ongoing maintenance)",
    # Business Value Development
    "1.4.3":  "Project-driven introduction-to-retirement of new service classes; Test catalogue",
    "1.5.3":  "Same — with explicit 4-step Exit decomposition (Resource decommissioning is heavier)",
    "1.4.13": "Catalog implementation lifecycle: design → build → policy",
    "1.5.15": "Catalog implementation lifecycle: design → build → policy",
    "1.4.17": "Define / orchestrate / monitor Anomaly Closed Loops (OODA-anchored governance)",
    "1.5.20": "Define / orchestrate / monitor Anomaly Closed Loops (OODA-anchored governance)",
    # ----- Operations area -----
    # Operations Readiness & Support
    "1.4.4":  "Operational substrate for all Service FAB processes",
    "1.4.14": "Operate the Service Catalog as a production service",
    "1.4.15": "Manage what's in the published Service Catalog",
    "1.5.4":  "Operational substrate for all Resource FAB; workforce establishment lives here",
    "1.5.7":  "Collect / distribute / manage resource data across all OFAB verticals",
    "1.5.16": "Operate the Resource Catalog as a production service",
    "1.5.17": "Manage what's in the published Resource Catalog",
    # Fulfillment
    "1.4.5":  "Activate and configure service instances per customer order",
    "1.5.5":  "Capture / schedule / allocate resource orders; work-order execution",
    # Assurance
    "1.4.6":  "Restore service; isolate cause of customer-impacting service issues",
    "1.4.7":  "Monitor / measure / report on service KPIs and SLAs",
    "1.4.18": "Predict / detect / assess / mitigate anomalies before they become Problems",
    "1.5.8":  "Detect / isolate / fix resource faults; convergence for alarms + performance",
    "1.5.9":  "Monitor / measure / report on resource KPIs",
    "1.5.21": "Predict / detect / assess / mitigate resource anomalies",
    # Billing
    "1.4.8":  "Pre-billing mediation of service usage events",
    "1.5.10": "Pre-billing mediation of resource usage events",
}

# CSS rule to insert just after `.l2 .name { ... }` declaration in each file
L2_DESC_CSS = """  .l2 .l2-desc {
    font-size: 7.5pt;
    font-style: italic;
    color: #555;
    line-height: 1.25;
    margin: 0 0 4px 0;
  }
"""

# Domain-header .desc lines to remove (added in prior iteration; user wants them gone)
DOMAIN_DESC_REMOVALS = [
    '    <div class="desc">Services realizing Product offerings to the market — customer-facing (CFS) and resource-facing (RFS). The <i>what is sold</i> layer.</div>\n',
    '    <div class="desc">Infrastructure resources realizing Services — functions, applications, computing, networking, storage. The <i>what runs underneath</i> layer.</div>\n',
]

# CSS block for .domain-hdr .desc to remove (added in prior iteration)
DOMAIN_DESC_CSS_REMOVAL = """  .domain-hdr .desc {
    font-size: 8.5pt;
    opacity: 0.92;
    margin-top: 5px;
    line-height: 1.3;
    font-weight: 400;
    font-style: italic;
    max-width: 540px;
    margin-left: auto;
    margin-right: auto;
  }
"""


def process_file(path: Path) -> tuple[int, int]:
    """Returns (l2_descriptions_added, domain_descriptions_removed)."""
    text = path.read_text()

    # Step 1 — remove domain-header .desc lines
    domain_removed = 0
    for line in DOMAIN_DESC_REMOVALS:
        if line in text:
            text = text.replace(line, "")
            domain_removed += 1

    # Step 2 — remove .domain-hdr .desc CSS block
    if DOMAIN_DESC_CSS_REMOVAL in text:
        text = text.replace(DOMAIN_DESC_CSS_REMOVAL, "")

    # Step 3 — insert .l2 .l2-desc CSS rule after the .l2 .name CSS block
    name_css_pattern = re.compile(
        r"(\.l2 \.name \{[^}]*\}\n)", re.MULTILINE
    )
    if "l2 .l2-desc" not in text:
        match = name_css_pattern.search(text)
        if match:
            text = text[:match.end()] + L2_DESC_CSS + text[match.end():]

    # Step 4 — insert <div class="l2-desc">...</div> after the <div class="name">...</div>
    # in each .l2 box. Find each L2 box by its <div class="id">{l2_id}</div> marker.
    # Pattern: <div class="id">1.4.1</div>...<div class="name">...</div>
    # We insert the desc div immediately after the name div.
    added = 0
    for l2_id, desc in DESCRIPTIONS.items():
        # Match the <div class="id">{l2_id}[*]?</div> ... <div class="name">...</div>
        # where the [*] handles the multi-vertical asterisk marker (e.g. "1.5.5*").
        # We need to find each occurrence and insert the desc.
        escaped_id = re.escape(l2_id)
        # Match the L2 block's id and name divs (with optional * after id)
        pattern = re.compile(
            rf'(<div class="id">{escaped_id}\*?</div>\s*'
            rf'<div class="name">[^<]*</div>)\n',
            re.MULTILINE
        )
        new_block = rf'\1\n      <div class="l2-desc">{desc}</div>\n'
        new_text, n = pattern.subn(new_block, text)
        if n > 0:
            text = new_text
            added += n

    path.write_text(text)
    return added, domain_removed


def main():
    files = [
        DIR / "capability-map-s2r.html",
        DIR / "capability-map.html",
        DIR / "capability-map-combined.html",
    ]
    for f in files:
        if not f.exists():
            print(f"skip {f.name} — not found")
            continue
        added, removed = process_file(f)
        print(f"{f.name}: +{added} L2 descriptions, -{removed} domain descriptions")


if __name__ == "__main__":
    main()
