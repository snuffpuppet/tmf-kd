#!/usr/bin/env python3
"""
Add a .h5-desc line to each H5 sub-capability box across all 3 HTML files.
Insert position: between h5-name and h5-src. Source-faithful condensations
of each H5's underlying L3 / responsibility-block content.
"""
import re
from pathlib import Path

DIR = Path(__file__).parent

# {h5_anchor: description (one short distinguishing sentence)}
DESCRIPTIONS = {
    # ----- S2R H5s (6) -----
    "cap-service-strategy-test":
        "Define test types per business activity; analyze test quality offline",
    "cap-resource-strategy-test":
        "Define test types per business activity; analyze test quality offline",
    "cap-service-specification-lifecycle-test":
        "Specify each Service Test (roles, methods, rules, thresholds); composes Resource Test",
    "cap-resource-specification-lifecycle-test":
        "Specify each Resource Test; base of cross-PSR test composition stack",
    "cap-service-specification-lifecycle-exit":
        "Identify unviable service classes; impacted products / customers; manage exit",
    "cap-resource-specification-lifecycle-exit":
        "Identify unviable resources; impacted customers; transition strategies; manage exit",

    # ----- Operations H5s (8) -----
    "cap-service-support-security":
        "Vulnerability mgmt, threat assessments, risk assessments + mitigation",
    "cap-service-support-inventory":
        "Manage Service Inventory DB + processes; audit; track; identify issues",
    "cap-service-support-test":
        "Execute end-to-end service tests; orchestrate Product + Resource test composition",
    "cap-resource-support-security":
        "Vulnerability mgmt, threat assessments, risk assessments + mitigation",
    "cap-resource-support-workforce":
        "Manage field workforce roster, skills, training (establishment side)",
    "cap-resource-support-inventory":
        "Manage Resource Inventory DB + processes; track; identify issues",
    "cap-resource-support-test":
        "Execute end-to-end resource tests; bottom of cross-PSR test composition",
    "cap-resource-order-workforce":
        "Allocate work orders to field workforce per resource order (execution side)",
}

# CSS rule for .h5 .h5-desc
H5_DESC_CSS = """  .h5 .h5-desc {
    font-size: 6.5pt;
    font-style: italic;
    color: #6a4810;
    opacity: 0.85;
    line-height: 1.2;
    margin: 1px 0 0 0;
  }
"""


def add_h5_descriptions(text: str) -> tuple[str, int]:
    """Insert <div class="h5-desc">...</div> after each <div class="h5-name">...
    line, matched by the H5 block's h5-anchor div content."""
    lines = text.split('\n')
    new_lines = []
    inserted = 0
    i = 0
    while i < len(lines):
        new_lines.append(lines[i])
        # Detect an h5-name line; look ahead within the same H5 block for the anchor
        if 'class="h5-name"' in lines[i]:
            anchor = None
            # H5 block is small — anchor is within next ~4 lines
            for j in range(i + 1, min(i + 6, len(lines))):
                m = re.search(r'<div class="h5-anchor">([^<]+)</div>', lines[j])
                if m:
                    anchor = m.group(1).strip()
                    break
            if anchor in DESCRIPTIONS:
                # Use the same indentation as the h5-name line
                indent = re.match(r'(\s*)', lines[i]).group(1)
                new_lines.append(
                    f'{indent}<div class="h5-desc">{DESCRIPTIONS[anchor]}</div>'
                )
                inserted += 1
        i += 1
    return '\n'.join(new_lines), inserted


def add_h5_desc_css(text: str) -> str:
    """Insert .h5 .h5-desc CSS rule just after the .h5 .h5-name CSS block."""
    if "h5-desc" in text and ".h5 .h5-desc" in text:
        return text  # already present
    pattern = re.compile(
        r"(\.h5 \.h5-name \{[^}]*\}\n)", re.MULTILINE
    )
    match = pattern.search(text)
    if match:
        return text[:match.end()] + H5_DESC_CSS + text[match.end():]
    return text


def process_file(path: Path) -> int:
    text = path.read_text()
    text = add_h5_desc_css(text)
    text, n = add_h5_descriptions(text)
    path.write_text(text)
    return n


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
        n = process_file(f)
        print(f"{f.name}: +{n} H5 descriptions")


if __name__ == "__main__":
    main()
