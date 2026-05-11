#!/usr/bin/env python3
"""
Generate capability-map.drawio — a single multi-page draw.io file with three
pages (S2R / Operations / Combined) covering all 47 stable heat-map anchors.

Uses only standard draw.io shapes (rounded rectangles, plain text labels) —
no external shape libraries — so the file opens cleanly in any draw.io
install. Container=1 on L2 boxes lets H5s nest visually and move together.

Output: capability-map.drawio in this directory.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from datetime import datetime, timezone
from itertools import count

DIR = Path(__file__).parent
OUT = DIR / "capability-map.drawio"

# ----------------------------------------------------------------------
# Color palette (matches HTML renders)
# ----------------------------------------------------------------------
S2R_DARK = "#1F3B6B"
S2R_MID = "#2A5298"
S2R_CELL = "#F5F7FB"
OPS_DARK = "#1A5F4A"
OPS_MID = "#2A8268"
OPS_CELL = "#F4FAF7"
L2_FILL = "#FFFFFF"
H5_FILL = "#FFF7D6"
H5_STROKE = "#D8B860"
DESC_COLOR = "#555555"

# ----------------------------------------------------------------------
# Data — same descriptions as the HTML renders
# ----------------------------------------------------------------------

# Each L2: (id, name, description, [(h5_anchor, h5_name, h5_src, h5_desc)])
# Verbatim from the _apply_*_descriptions.py dictionaries.

L2_DESC = {
    "1.4.1":  "Annual and multi-year strategic plans for services and service directions",
    "1.5.1":  "Annual and multi-year resource strategies; v25.5 carries AI-readiness guidance",
    "1.4.2":  "Plan and deliver new and enhanced service capabilities (project-driven)",
    "1.5.2":  "Deploy new and enhanced technology and resources; logical and physical",
    "1.4.12": "Plan / forecast / optimize service capacity vs SLA / SLO / SLR",
    "1.5.14": "Plan / forecast / optimize resource capacity vs business objectives",
    "1.4.16": "Design the catalog scheme; define the Service Catalog Specification",
    "1.5.18": "Design the catalog scheme; define the Resource Catalog Specification",
    "1.4.19": "Describe / model / analyze service specification artefacts (ongoing maintenance)",
    "1.5.19": "Develop / master / analyze + version Resource Specifications (ongoing maintenance)",
    "1.4.3":  "Project-driven introduction-to-retirement of new service classes; Test catalogue",
    "1.5.3":  "Same — with explicit 4-step Exit decomposition (Resource decommissioning is heavier)",
    "1.4.13": "Catalog implementation lifecycle: design → build → policy",
    "1.5.15": "Catalog implementation lifecycle: design → build → policy",
    "1.4.17": "Define / orchestrate / monitor Anomaly Closed Loops (OODA-anchored governance)",
    "1.5.20": "Define / orchestrate / monitor Anomaly Closed Loops (OODA-anchored governance)",
    "1.4.4":  "Operational substrate for all Service FAB processes",
    "1.4.14": "Operate the Service Catalog as a production service",
    "1.4.15": "Manage what's in the published Service Catalog",
    "1.5.4":  "Operational substrate for all Resource FAB; workforce establishment lives here",
    "1.5.7":  "Collect / distribute / manage resource data across all OFAB verticals",
    "1.5.16": "Operate the Resource Catalog as a production service",
    "1.5.17": "Manage what's in the published Resource Catalog",
    "1.4.5":  "Activate and configure service instances per customer order",
    "1.5.5":  "Capture / schedule / allocate resource orders; work-order execution",
    "1.4.6":  "Restore service; isolate cause of customer-impacting service issues",
    "1.4.7":  "Monitor / measure / report on service KPIs and SLAs",
    "1.4.18": "Predict / detect / assess / mitigate anomalies before they become Problems",
    "1.5.8":  "Detect / isolate / fix resource faults; convergence for alarms + performance",
    "1.5.9":  "Monitor / measure / report on resource KPIs",
    "1.5.21": "Predict / detect / assess / mitigate resource anomalies",
    "1.4.8":  "Pre-billing mediation of service usage events",
    "1.5.10": "Pre-billing mediation of resource usage events",
}

L2_NAME = {
    "1.4.1":  "Service Strategy Management",
    "1.5.1":  "Resource Strategy Management",
    "1.4.2":  "Service Capability Delivery",
    "1.5.2":  "Resource Capability Delivery",
    "1.4.12": "Service Capacity Management",
    "1.5.14": "Resource Capacity Management",
    "1.4.16": "Service Catalog Planning Management",
    "1.5.18": "Resource Catalog Planning Management",
    "1.4.19": "Service Specification Management",
    "1.5.19": "Resource Specification Management",
    "1.4.3":  "Service Specification Lifecycle Management",
    "1.5.3":  "Resource Specification Lifecycle Management",
    "1.4.13": "Service Catalog Lifecycle Management",
    "1.5.15": "Resource Catalog Lifecycle Management",
    "1.4.17": "Service Anomaly Lifecycle Management",
    "1.5.20": "Resource Anomaly Lifecycle Management",
    "1.4.4":  "Service Support Management",
    "1.4.14": "Service Catalog — Operational Readiness",
    "1.4.15": "Service Catalog — Content",
    "1.5.4":  "Resource Support Management",
    "1.5.7":  "Resource Data Management*",
    "1.5.16": "Resource Catalog — Operational Readiness",
    "1.5.17": "Resource Catalog — Content",
    "1.4.5":  "Service Activation Management",
    "1.5.5":  "Resource Order Management*",
    "1.4.6":  "Service Problem Management",
    "1.4.7":  "Service Performance Management",
    "1.4.18": "Service Anomaly Management",
    "1.5.8":  "Resource Trouble Management",
    "1.5.9":  "Resource Performance Management",
    "1.5.21": "Resource Anomaly Management",
    "1.4.8":  "Service Guiding & Mediation",
    "1.5.10": "Resource Mediation & Reporting",
}

L2_ANCHOR = {
    "1.4.1":  "cap-service-strategy",
    "1.5.1":  "cap-resource-strategy",
    "1.4.2":  "cap-service-capability-delivery",
    "1.5.2":  "cap-resource-capability-delivery",
    "1.4.12": "cap-service-capacity",
    "1.5.14": "cap-resource-capacity",
    "1.4.16": "cap-service-catalog-planning",
    "1.5.18": "cap-resource-catalog-planning",
    "1.4.19": "cap-service-specification",
    "1.5.19": "cap-resource-specification",
    "1.4.3":  "cap-service-specification-lifecycle",
    "1.5.3":  "cap-resource-specification-lifecycle",
    "1.4.13": "cap-service-catalog-lifecycle",
    "1.5.15": "cap-resource-catalog-lifecycle",
    "1.4.17": "cap-service-anomaly-lifecycle",
    "1.5.20": "cap-resource-anomaly-lifecycle",
    "1.4.4":  "cap-service-support",
    "1.4.14": "cap-service-catalog-operational-readiness",
    "1.4.15": "cap-service-catalog-content",
    "1.5.4":  "cap-resource-support",
    "1.5.7":  "cap-resource-data",
    "1.5.16": "cap-resource-catalog-operational-readiness",
    "1.5.17": "cap-resource-catalog-content",
    "1.4.5":  "cap-service-activation",
    "1.5.5":  "cap-resource-order",
    "1.4.6":  "cap-service-problem",
    "1.4.7":  "cap-service-performance",
    "1.4.18": "cap-service-anomaly",
    "1.5.8":  "cap-resource-trouble",
    "1.5.9":  "cap-resource-performance",
    "1.5.21": "cap-resource-anomaly",
    "1.4.8":  "cap-service-guiding-and-mediation",
    "1.5.10": "cap-resource-mediation-and-reporting",
}

# H5 sub-capabilities, keyed by parent L2 ID — list of (anchor, name, src, desc)
H5S = {
    "1.4.1": [("cap-service-strategy-test", "Test management strategy",
               "L3 1.4.1.8 + 1.4.1.9",
               "Define test types per business activity; analyze test quality offline")],
    "1.5.1": [("cap-resource-strategy-test", "Test management strategy",
               "L3 1.5.1.8 + 1.5.1.9",
               "Define test types per business activity; analyze test quality offline")],
    "1.4.3": [
        ("cap-service-specification-lifecycle-test", "Test catalogue dev & retirement",
         "L3 1.4.3.8 (new in v25.5)",
         "Specify each Service Test (roles, methods, rules, thresholds); composes Resource Test"),
        ("cap-service-specification-lifecycle-exit", "Service end-of-life management",
         "L3 1.4.3.7 (narrative-only)",
         "Identify unviable service classes; impacted products / customers; manage exit"),
    ],
    "1.5.3": [
        ("cap-resource-specification-lifecycle-test", "Test catalogue dev & retirement",
         "L3 1.5.3.8 (new in v25.5)",
         "Specify each Resource Test; base of cross-PSR test composition stack"),
        ("cap-resource-specification-lifecycle-exit", "Resource end-of-life management",
         "L3 1.5.3.7 (4 L4s — PSR-asymm)",
         "Identify unviable resources; impacted customers; transition strategies; manage exit"),
    ],
    "1.4.4": [
        ("cap-service-support-security", "Security & risk responsibilities",
         "L2 responsibilities block",
         "Vulnerability mgmt, threat assessments, risk assessments + mitigation"),
        ("cap-service-support-inventory", "Inventory management",
         "L3 1.4.4.1 (4 L4s)",
         "Manage Service Inventory DB + processes; audit; track; identify issues"),
        ("cap-service-support-test", "Test management",
         "L3 1.4.4.6",
         "Execute end-to-end service tests; orchestrate Product + Resource test composition"),
    ],
    "1.5.4": [
        ("cap-resource-support-security", "Security & risk responsibilities",
         "L2 responsibilities block",
         "Vulnerability mgmt, threat assessments, risk assessments + mitigation"),
        ("cap-resource-support-workforce", "Workforce management (establishment)",
         "L3 1.5.4.8 Manage Field Workforce",
         "Manage field workforce roster, skills, training (establishment side)"),
        ("cap-resource-support-inventory", "Inventory management",
         "L3 1.5.4.5 (3 L4s — PSR-asymm)",
         "Manage Resource Inventory DB + processes; track; identify issues"),
        ("cap-resource-support-test", "Test management",
         "L3 1.5.4.9",
         "Execute end-to-end resource tests; bottom of cross-PSR test composition"),
    ],
    "1.5.5": [
        ("cap-resource-order-workforce", "Workforce-related work orders (execution)",
         "L3 1.5.5.7 Manage Resource Work Order",
         "Allocate work orders to field workforce per resource order (execution side)"),
    ],
}

# ----------------------------------------------------------------------
# Page layout — declarative grid of (vertical_label, [service_l2_ids], [resource_l2_ids])
# ----------------------------------------------------------------------

S2R_GRID = [
    ("STRATEGY MGMT",   ["1.4.1"],                              ["1.5.1"]),
    ("CAPABILITY MGMT", ["1.4.2","1.4.12","1.4.16","1.4.19"],   ["1.5.2","1.5.14","1.5.18","1.5.19"]),
    ("BVD",             ["1.4.3","1.4.13","1.4.17"],            ["1.5.3","1.5.15","1.5.20"]),
]

OPS_GRID = [
    ("ORS",         ["1.4.4","1.4.14","1.4.15"],           ["1.5.4","1.5.7","1.5.16","1.5.17"]),
    ("FULFILLMENT", ["1.4.5"],                              ["1.5.5"]),
    ("ASSURANCE",   ["1.4.6","1.4.7","1.4.18"],            ["1.5.8","1.5.9","1.5.21"]),
    ("BILLING",     ["1.4.8"],                              ["1.5.10"]),
]

# Full vertical names — used in the Roadmap page's horizontal column headers.
# The short labels above are kept for the original Combined page's rotated/vertical
# labels (where compact text fits the cell shape better).
FULL_VERTICAL_NAMES = {
    "STRATEGY MGMT":   "STRATEGY MANAGEMENT",
    "CAPABILITY MGMT": "CAPABILITY MANAGEMENT",
    "BVD":             "BUSINESS VALUE DEVELOPMENT",
    "ORS":             "OPERATIONS READINESS & SUPPORT",
    "FULFILLMENT":     "FULFILLMENT",
    "ASSURANCE":       "ASSURANCE",
    "BILLING":         "BILLING",
}

# ----------------------------------------------------------------------
# Layout constants
# ----------------------------------------------------------------------

PAGE_MARGIN = 30
TITLE_HEIGHT = 50
HEADER_HEIGHT = 50
VLABEL_WIDTH = 80
DOMAIN_WIDTH = 720
COL_GAP = 20
ROW_GAP = 15
L2_HEIGHT_BASE = 108  # tall enough to fit ID + name + desc + anchor footer without clipping
L2_HEIGHT_PER_H5 = 56
L2_NAME_HEIGHT = 56  # space at top of L2 box reserved for name + desc + id
L2_PADDING = 8
H5_HEIGHT = 50
H5_GAP = 4
CELL_PADDING = 12

# ----------------------------------------------------------------------
# XML emission helpers
# ----------------------------------------------------------------------

def cell(id_, value, x, y, w, h, style, parent="1"):
    """Return an mxCell XML string (vertex). Escapes &, <, > and " in value.
    Converts literal \\n to &#10; (XML newline entity) so drawio renders them
    as line breaks rather than whitespace under html=1 mode."""
    safe_value = escape(value, {'"': "&quot;"}).replace("\n", "&#10;")
    return (
        f'        <mxCell id="{id_}" value="{safe_value}" '
        f'style="{style}" vertex="1" parent="{parent}">\n'
        f'          <mxGeometry x="{x}" y="{y}" '
        f'width="{w}" height="{h}" as="geometry"/>\n'
        f'        </mxCell>'
    )


def style_box(fill, stroke, font_size=12, font_color="#1A1A1A",
              font_style=0, container=False, vertical=False, align="center",
              valign="middle"):
    parts = [
        "rounded=0", "whiteSpace=wrap", "html=1",
        f"fillColor={fill}", f"strokeColor={stroke}",
        f"fontSize={font_size}", f"fontColor={font_color}",
        f"align={align}", f"verticalAlign={valign}",
    ]
    if font_style:
        parts.append(f"fontStyle={font_style}")
    if container:
        parts += ["container=1", "collapsible=0"]
    if vertical:
        parts.append("rotation=-90")
    return ";".join(parts) + ";"


def style_text(font_size=10, font_color="#333", font_style=0, align="left", valign="top"):
    parts = [
        "text", "html=1",
        "strokeColor=none", "fillColor=none",
        f"fontSize={font_size}", f"fontColor={font_color}",
        f"align={align}", f"verticalAlign={valign}",
        "whiteSpace=wrap",
    ]
    if font_style:
        parts.append(f"fontStyle={font_style}")
    return ";".join(parts) + ";"


# ----------------------------------------------------------------------
# Higher-level emit functions
# ----------------------------------------------------------------------

def emit_l2_box(idgen, l2_id, x, y, w, parent="1", stroke=None, compact=False):
    """Emit an L2 box with name/desc/id text inside, plus any H5 children
    nested as containers within. Returns (cells_xml, total_height).

    stroke: stroke color for the L2 box border + ID-text color (defaults to
    S2R_MID; pass OPS_MID for Operations-area L2s in the roadmap layout).
    compact: if True, use tighter A3-fit dimensions (smaller fonts + heights)."""
    if stroke is None:
        stroke = S2R_MID

    # Layout dimensions — switch to compact for the A3-fit Roadmap page
    if compact:
        l2_h_base = 88
        l2_name_h = 46
        h5_h = 38
        h5_g = 3
        font_id, font_name, font_desc, font_anchor = 8, 9, 7, 6
        font_h5_name, font_h5_desc, font_h5_src = 8, 7, 6
        line_id_h, line_name_h, line_desc_h = 12, 16, 12
        line_h5_name, line_h5_desc, line_h5_src = 12, 13, 11
    else:
        l2_h_base = L2_HEIGHT_BASE
        l2_name_h = L2_NAME_HEIGHT
        h5_h = H5_HEIGHT
        h5_g = H5_GAP
        font_id, font_name, font_desc, font_anchor = 9, 11, 8, 7
        font_h5_name, font_h5_desc, font_h5_src = 9, 7, 6
        line_id_h, line_name_h, line_desc_h = 14, 18, 14
        line_h5_name, line_h5_desc, line_h5_src = 14, 14, 14

    h5s = H5S.get(l2_id, [])
    body_h = l2_name_h + (len(h5s) * (h5_h + h5_g) if h5s else 0) + L2_PADDING
    box_h = max(l2_h_base, body_h)

    box_id = next(idgen)
    name = L2_NAME[l2_id]
    desc = L2_DESC[l2_id]
    anchor = L2_ANCHOR[l2_id]
    pid_label = l2_id + ("*" if name.endswith("*") else "")
    name_clean = name.rstrip("*")

    box_style = style_box(L2_FILL, stroke, font_size=10,
                          container=True, align="left", valign="top")
    out = [cell(box_id, "", x, y, w, box_h, box_style, parent=parent)]

    # Inside-the-L2 children use box_id as parent; positions are relative to the L2's geometry.
    id_label_id = next(idgen)
    out.append(cell(id_label_id, pid_label, 5, 3, w-10, line_id_h,
                    style_text(font_size=font_id, font_color=stroke, font_style=1, align="left"),
                    parent=box_id))
    name_id = next(idgen)
    out.append(cell(name_id, name_clean, 5, 3 + line_id_h, w-10, line_name_h,
                    style_text(font_size=font_name, font_color="#1A1A1A", font_style=1, align="left"),
                    parent=box_id))
    desc_id = next(idgen)
    out.append(cell(desc_id, desc, 5, 3 + line_id_h + line_name_h, w-10, line_desc_h,
                    style_text(font_size=font_desc, font_color=DESC_COLOR, font_style=2, align="left"),
                    parent=box_id))

    # H5 children — yellow containers stacked below, each with name+desc+src+anchor inside
    h5_y = l2_name_h
    for (h5_anchor, h5_name, h5_src, h5_desc) in h5s:
        h5_id = next(idgen)
        h5_style = style_box(H5_FILL, H5_STROKE, font_size=8,
                             container=True, align="left", valign="top")
        out.append(cell(h5_id, "", 5, h5_y, w-10, h5_h, h5_style, parent=box_id))
        h5_name_id = next(idgen)
        out.append(cell(h5_name_id, h5_name, 4, 1, w-18, line_h5_name,
                        style_text(font_size=font_h5_name, font_color="#6A4810", font_style=1, align="left"),
                        parent=h5_id))
        h5_desc_id = next(idgen)
        out.append(cell(h5_desc_id, h5_desc, 4, 1 + line_h5_name, w-18, line_h5_desc,
                        style_text(font_size=font_h5_desc, font_color="#6A4810", font_style=2, align="left"),
                        parent=h5_id))
        h5_src_id = next(idgen)
        out.append(cell(h5_src_id, h5_src + "  —  " + h5_anchor,
                        4, 1 + line_h5_name + line_h5_desc, w-18, line_h5_src,
                        style_text(font_size=font_h5_src, font_color="#999999", align="left"),
                        parent=h5_id))
        h5_y += h5_h + h5_g

    # Anchor ID footer (placed near bottom — leave 6px clearance for the box border)
    anchor_id = next(idgen)
    out.append(cell(anchor_id, anchor, 6, box_h - 18, w-12, 12,
                    style_text(font_size=7, font_color="#888888", align="left"),
                    parent=box_id))

    return "\n".join(out), box_h


def emit_grid(idgen, grid, area_dark, area_mid, area_cell, x_start, y_start, parent="1"):
    """Emit one matrix grid (header row + N vertical-label rows). Returns (xml, total_height)."""
    out = []
    # Domain headers
    svc_x = x_start + VLABEL_WIDTH + COL_GAP
    res_x = svc_x + DOMAIN_WIDTH + COL_GAP
    hdr_style = style_box(area_dark, area_dark, font_size=13, font_color="#FFFFFF", font_style=1)
    out.append(cell(next(idgen),
                    "SERVICE DOMAIN\nGB991 §1.1.1.5",
                    svc_x, y_start, DOMAIN_WIDTH, HEADER_HEIGHT, hdr_style))
    out.append(cell(next(idgen),
                    "RESOURCE DOMAIN\nGB991 §1.1.1.6",
                    res_x, y_start, DOMAIN_WIDTH, HEADER_HEIGHT, hdr_style))

    # Vertical-label rows
    cur_y = y_start + HEADER_HEIGHT + ROW_GAP
    for (vlabel, svc_l2s, res_l2s) in grid:
        # Per-side L2 box widths — split column into halves if 2+ L2s in cell
        n_svc = len(svc_l2s)
        n_res = len(res_l2s)
        # 2-column inner grid where space allows
        svc_cols = 2 if n_svc >= 2 else 1
        res_cols = 2 if n_res >= 2 else 1
        svc_w = (DOMAIN_WIDTH - 2*CELL_PADDING - (svc_cols-1)*ROW_GAP) // svc_cols
        res_w = (DOMAIN_WIDTH - 2*CELL_PADDING - (res_cols-1)*ROW_GAP) // res_cols

        # Pre-compute heights per L2 to know row height
        svc_heights = [
            L2_NAME_HEIGHT + (len(H5S.get(lid, []))*(H5_HEIGHT+H5_GAP) if H5S.get(lid) else 0)
            + L2_PADDING
            for lid in svc_l2s
        ]
        res_heights = [
            L2_NAME_HEIGHT + (len(H5S.get(lid, []))*(H5_HEIGHT+H5_GAP) if H5S.get(lid) else 0)
            + L2_PADDING
            for lid in res_l2s
        ]
        svc_heights = [max(L2_HEIGHT_BASE, h) for h in svc_heights]
        res_heights = [max(L2_HEIGHT_BASE, h) for h in res_heights]

        # 2-column packing: row 0 = (idx 0, idx 1), row 1 = (idx 2, idx 3), ...
        def packed_height(heights, cols):
            if not heights:
                return 0
            row_max = []
            for i in range(0, len(heights), cols):
                row_max.append(max(heights[i:i+cols]))
            return sum(row_max) + (len(row_max)-1)*ROW_GAP

        svc_packed_h = packed_height(svc_heights, svc_cols)
        res_packed_h = packed_height(res_heights, res_cols)
        cell_h = max(svc_packed_h, res_packed_h) + 2*CELL_PADDING

        # Vertical label cell (rotated text)
        vlabel_style = style_box(area_mid, area_mid, font_size=11, font_color="#FFFFFF",
                                 font_style=1, vertical=True)
        out.append(cell(next(idgen), vlabel, x_start, cur_y, VLABEL_WIDTH, cell_h, vlabel_style))

        # Service cell background
        svc_cell_style = style_box(area_cell, area_mid, font_size=8, container=True)
        svc_cell_id = next(idgen)
        out.append(cell(svc_cell_id, "", svc_x, cur_y, DOMAIN_WIDTH, cell_h, svc_cell_style))

        # Resource cell background
        res_cell_id = next(idgen)
        out.append(cell(res_cell_id, "", res_x, cur_y, DOMAIN_WIDTH, cell_h, svc_cell_style))

        # Place L2 boxes inside Service cell
        def place_l2s(l2_ids, heights, cols, w, cell_id):
            inner_y = CELL_PADDING
            row_max_h = 0
            for i, lid in enumerate(l2_ids):
                col = i % cols
                if col == 0 and i > 0:
                    inner_y += row_max_h + ROW_GAP
                    row_max_h = 0
                inner_x = CELL_PADDING + col * (w + ROW_GAP)
                xml, _ = emit_l2_box(idgen, lid, inner_x, inner_y, w,
                                     parent=cell_id, stroke=area_mid)
                out.append(xml)
                row_max_h = max(row_max_h, heights[i])

        place_l2s(svc_l2s, svc_heights, svc_cols, svc_w, svc_cell_id)
        place_l2s(res_l2s, res_heights, res_cols, res_w, res_cell_id)

        cur_y += cell_h + ROW_GAP

    total_h = cur_y - y_start
    return "\n".join(out), total_h


# ----------------------------------------------------------------------
# Page builders
# ----------------------------------------------------------------------

def build_page(name, body_xml, page_w, page_h):
    # Belt-and-braces white background:
    #   - mxGraphModel `background` attribute (older drawio versions)
    #   - mxGraphModel `pageBackground` attribute (newer drawio versions)
    #   - explicit white-fill rectangle as the first content cell (final fallback;
    #     ensures white renders even if the canvas theme is dark)
    bg_rect = (
        f'        <mxCell id="bg" value="" '
        f'style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=none;" '
        f'vertex="1" parent="1">\n'
        f'          <mxGeometry x="0" y="0" width="{page_w}" height="{page_h}" as="geometry"/>\n'
        f'        </mxCell>'
    )
    return f"""  <diagram id="{name.replace(' ','-')}" name="{escape(name)}">
    <mxGraphModel dx="1700" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0" background="#FFFFFF" pageBackground="#FFFFFF">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
{bg_rect}
{body_xml}
      </root>
    </mxGraphModel>
  </diagram>"""


def build_s2r_page(idgen):
    out = []
    # Title bar
    out.append(cell(next(idgen),
                    "Capability Map  —  Strategy-to-Readiness Lifecycle Area",
                    PAGE_MARGIN, PAGE_MARGIN, 1620, 30,
                    style_text(font_size=18, font_color=S2R_DARK, font_style=1, align="left", valign="middle")))
    out.append(cell(next(idgen),
                    "GB921 v25.5  ·  Service + Resource Domains × Strategy / Capability Mgmt / BVD verticals  ·  22 stable heat-map anchors (16 L2 + 6 H5)",
                    PAGE_MARGIN, PAGE_MARGIN+30, 1620, 18,
                    style_text(font_size=9, font_color="#555", align="left", valign="middle")))

    grid_xml, _ = emit_grid(idgen, S2R_GRID, S2R_DARK, S2R_MID, S2R_CELL,
                            x_start=PAGE_MARGIN,
                            y_start=PAGE_MARGIN + 60)
    out.append(grid_xml)
    return "\n".join(out)


def build_ops_page(idgen):
    out = []
    out.append(cell(next(idgen),
                    "Capability Map  —  Operations Lifecycle Area",
                    PAGE_MARGIN, PAGE_MARGIN, 1620, 30,
                    style_text(font_size=18, font_color=OPS_DARK, font_style=1, align="left", valign="middle")))
    out.append(cell(next(idgen),
                    "GB921 v25.5  ·  Service + Resource Domains × OFAB verticals  ·  25 stable heat-map anchors (17 L2 + 8 H5)",
                    PAGE_MARGIN, PAGE_MARGIN+30, 1620, 18,
                    style_text(font_size=9, font_color="#555", align="left", valign="middle")))
    grid_xml, _ = emit_grid(idgen, OPS_GRID, OPS_DARK, OPS_MID, OPS_CELL,
                            x_start=PAGE_MARGIN,
                            y_start=PAGE_MARGIN + 60)
    out.append(grid_xml)
    return "\n".join(out)


def build_combined_page(idgen):
    out = []
    out.append(cell(next(idgen),
                    "Combined Capability Map  —  TMF eTOM v25.5 OSS Layer  —  both Lifecycle Areas",
                    PAGE_MARGIN, PAGE_MARGIN, 1620, 30,
                    style_text(font_size=18, font_color="#1A1A1A", font_style=1, align="left", valign="middle")))
    out.append(cell(next(idgen),
                    "Service + Resource Domains × 7 verticals  ·  47 stable heat-map anchors total (33 L2 + 14 H5)",
                    PAGE_MARGIN, PAGE_MARGIN+30, 1620, 18,
                    style_text(font_size=9, font_color="#555", align="left", valign="middle")))

    # S2R band label
    band_y = PAGE_MARGIN + 60
    band_style = style_box(S2R_DARK, S2R_DARK, font_size=12, font_color="#FFFFFF", font_style=1, align="left")
    out.append(cell(next(idgen),
                    "  STRATEGY-TO-READINESS",
                    PAGE_MARGIN, band_y, 1620, 26, band_style))

    s2r_xml, s2r_h = emit_grid(idgen, S2R_GRID, S2R_DARK, S2R_MID, S2R_CELL,
                                x_start=PAGE_MARGIN,
                                y_start=band_y + 30)
    out.append(s2r_xml)

    ops_band_y = band_y + 30 + s2r_h + 15
    ops_band_style = style_box(OPS_DARK, OPS_DARK, font_size=12, font_color="#FFFFFF", font_style=1, align="left")
    out.append(cell(next(idgen),
                    "  OPERATIONS",
                    PAGE_MARGIN, ops_band_y, 1620, 26, ops_band_style))

    ops_xml, _ = emit_grid(idgen, OPS_GRID, OPS_DARK, OPS_MID, OPS_CELL,
                           x_start=PAGE_MARGIN,
                           y_start=ops_band_y + 30)
    out.append(ops_xml)
    return "\n".join(out)


# ----------------------------------------------------------------------
# Roadmap layout — verticals across the top, domains down the side
# ----------------------------------------------------------------------

# Roadmap-specific layout constants — sized to fit drawio's A3 landscape preset (1654x1169)
ROAD_DOMAIN_LABEL_W = 90
ROAD_COL_W = 207
ROAD_BAND_H = 22
ROAD_HDR_H = 36
ROAD_CELL_GAP = 5
ROAD_CELL_PADDING = 5
ROAD_L2_GAP = 5
# Compact L2 dimensions used in roadmap (mirror the compact branch in emit_l2_box)
ROAD_L2_HEIGHT_BASE = 88
ROAD_L2_NAME_HEIGHT = 46
ROAD_H5_HEIGHT = 38
ROAD_H5_GAP = 3


def stacked_height(l2_ids, compact=False):
    """Height needed to stack L2s vertically inside a roadmap cell."""
    if compact:
        l2_h_base, l2_name_h, h5_h, h5_g = (
            ROAD_L2_HEIGHT_BASE, ROAD_L2_NAME_HEIGHT, ROAD_H5_HEIGHT, ROAD_H5_GAP
        )
        cell_pad = ROAD_CELL_PADDING
        row_gap = ROAD_L2_GAP
    else:
        l2_h_base, l2_name_h, h5_h, h5_g = (
            L2_HEIGHT_BASE, L2_NAME_HEIGHT, H5_HEIGHT, H5_GAP
        )
        cell_pad = CELL_PADDING
        row_gap = ROW_GAP

    if not l2_ids:
        return l2_h_base + 2 * cell_pad
    total = 0
    for lid in l2_ids:
        h5_count = len(H5S.get(lid, []))
        l2_h = max(l2_h_base,
                   l2_name_h + h5_count * (h5_h + h5_g) + L2_PADDING)
        total += l2_h
    total += (len(l2_ids) - 1) * row_gap
    return total + 2 * cell_pad


def emit_grid_roadmap(idgen, x_start, y_start):
    """Roadmap-orientation grid: 7 vertical columns across, 2 domain rows down.
    S2R verticals (3) on the left half; Operations verticals (4) on the right.
    Returns (xml, total_width, total_height)."""
    out = []
    n_s2r = len(S2R_GRID)
    n_ops = len(OPS_GRID)
    all_grids = S2R_GRID + OPS_GRID

    cols_x_start = x_start + ROAD_DOMAIN_LABEL_W + ROAD_CELL_GAP

    # Lifecycle Area band labels (row 1)
    s2r_band_w = n_s2r * ROAD_COL_W + (n_s2r - 1) * ROAD_CELL_GAP
    ops_band_w = n_ops * ROAD_COL_W + (n_ops - 1) * ROAD_CELL_GAP

    band_style_s2r = style_box(S2R_DARK, S2R_DARK, font_size=11,
                               font_color="#FFFFFF", font_style=1, align="center")
    out.append(cell(next(idgen),
                    "STRATEGY-TO-READINESS",
                    cols_x_start, y_start, s2r_band_w, ROAD_BAND_H, band_style_s2r))

    ops_band_x = cols_x_start + s2r_band_w + ROAD_CELL_GAP
    band_style_ops = style_box(OPS_DARK, OPS_DARK, font_size=11,
                               font_color="#FFFFFF", font_style=1, align="center")
    out.append(cell(next(idgen),
                    "OPERATIONS",
                    ops_band_x, y_start, ops_band_w, ROAD_BAND_H, band_style_ops))

    # Vertical column headers (row 2) — full vertical names + GB991 ref on separate lines
    hdr_y = y_start + ROAD_BAND_H + 3
    for i, (vname, _, _) in enumerate(all_grids):
        is_s2r = i < n_s2r
        hdr_color = S2R_MID if is_s2r else OPS_MID
        hdr_style = style_box(hdr_color, hdr_color, font_size=9,
                              font_color="#FFFFFF", font_style=1)
        col_x = cols_x_start + i * (ROAD_COL_W + ROAD_CELL_GAP)
        full_name = FULL_VERTICAL_NAMES.get(vname, vname)
        out.append(cell(next(idgen),
                        full_name + "\nGB991 §1.1.2.2",
                        col_x, hdr_y, ROAD_COL_W, ROAD_HDR_H, hdr_style))

    # Pre-compute row heights from densest cell per row (compact mode)
    svc_heights = [stacked_height(svc_l2s, compact=True) for (_, svc_l2s, _) in all_grids]
    res_heights = [stacked_height(res_l2s, compact=True) for (_, _, res_l2s) in all_grids]
    svc_row_h = max(svc_heights)
    res_row_h = max(res_heights)

    cells_y = hdr_y + ROAD_HDR_H + 3

    # Domain row labels (left edge, span full row height per domain).
    # Three centered lines: domain name, GB991 ref, description.
    dlabel_style = style_box("#444444", "#444444", font_size=10,
                             font_color="#FFFFFF", font_style=1, align="center")
    out.append(cell(next(idgen),
                    "SERVICE DOMAIN\n\nGB991 §1.1.1.5\n\n\"What is sold\" — services realizing Product offerings",
                    x_start, cells_y, ROAD_DOMAIN_LABEL_W, svc_row_h, dlabel_style))
    out.append(cell(next(idgen),
                    "RESOURCE DOMAIN\n\nGB991 §1.1.1.6\n\n\"What runs underneath\" — infrastructure realizing Services",
                    x_start, cells_y + svc_row_h + ROAD_CELL_GAP,
                    ROAD_DOMAIN_LABEL_W, res_row_h, dlabel_style))

    # Cells: 2 rows × 7 columns. For each (domain, vertical) intersection,
    # create a cell container and stack L2 boxes inside vertically.
    rows = [
        ("svc", cells_y, svc_row_h),
        ("res", cells_y + svc_row_h + ROAD_CELL_GAP, res_row_h),
    ]
    for (domain_key, row_y, row_h) in rows:
        for i, (vname, svc_l2s, res_l2s) in enumerate(all_grids):
            l2_ids = svc_l2s if domain_key == "svc" else res_l2s
            is_s2r = i < n_s2r
            cell_color = S2R_CELL if is_s2r else OPS_CELL
            cell_stroke = S2R_MID if is_s2r else OPS_MID

            col_x = cols_x_start + i * (ROAD_COL_W + ROAD_CELL_GAP)
            cell_style = style_box(cell_color, cell_stroke, font_size=8, container=True)
            cell_id = next(idgen)
            out.append(cell(cell_id, "", col_x, row_y, ROAD_COL_W, row_h, cell_style))

            # Stack L2s vertically inside the cell (compact mode)
            l2_w = ROAD_COL_W - 2 * ROAD_CELL_PADDING
            inner_y = ROAD_CELL_PADDING
            for lid in l2_ids:
                xml, l2_h = emit_l2_box(idgen, lid, ROAD_CELL_PADDING, inner_y, l2_w,
                                        parent=cell_id, stroke=cell_stroke,
                                        compact=True)
                out.append(xml)
                inner_y += l2_h + ROAD_L2_GAP

    total_w = ROAD_DOMAIN_LABEL_W + ROAD_CELL_GAP + len(all_grids) * ROAD_COL_W \
              + (len(all_grids) - 1) * ROAD_CELL_GAP
    total_h = (cells_y - y_start) + svc_row_h + ROAD_CELL_GAP + res_row_h
    return "\n".join(out), total_w, total_h


# Footer — mirrors the user-supplied "header strip" pattern (Document / Author / Version / Last Updated)
FOOTER_DARK = "#3D3D3D"
FOOTER_LABEL_BG = "#5BB6E8"
FOOTER_CONTENT_BG = "#FFFFFF"
FOOTER_BORDER = "#A0A0A0"


def emit_footer(idgen, x, y, w, h, fields):
    """Emit a single-row footer strip: dark filler on the left, then alternating
    blue label + white content cells for each (label, value) tuple in fields.
    Returns the XML string."""
    out = []
    label_w = 80
    content_w = 130
    pair_w = label_w + content_w
    n_pairs = len(fields)
    pairs_total_w = n_pairs * pair_w
    filler_w = w - pairs_total_w
    if filler_w < 0:
        filler_w = 0  # safety; would mean too many pairs for the width

    cur_x = x
    # Dark filler (left)
    if filler_w > 0:
        out.append(cell(next(idgen), "",
                        cur_x, y, filler_w, h,
                        style_box(FOOTER_DARK, FOOTER_DARK, font_size=8)))
        cur_x += filler_w

    # Label + content pairs
    for (label, value) in fields:
        out.append(cell(next(idgen), label,
                        cur_x, y, label_w, h,
                        style_box(FOOTER_LABEL_BG, FOOTER_LABEL_BG,
                                  font_size=9, font_color="#FFFFFF", font_style=1,
                                  align="center", valign="middle")))
        cur_x += label_w
        out.append(cell(next(idgen), value,
                        cur_x, y, content_w, h,
                        style_box(FOOTER_CONTENT_BG, FOOTER_BORDER,
                                  font_size=9, font_color="#1A1A1A",
                                  align="center", valign="middle")))
        cur_x += content_w

    return "\n".join(out)


def build_roadmap_page(idgen):
    """Roadmap page sized for drawio's A3 landscape preset (1654×1169 pt).
    Centered title + matrix + footer."""
    PAGE_W = 1654
    PAGE_H = 1169
    margin = 14
    body_w = PAGE_W - 2 * margin

    out = []

    # Title (centered)
    out.append(cell(next(idgen),
                    "OSS Capability Map — Roadmap Layout",
                    margin, margin, body_w, 24,
                    style_text(font_size=16, font_color="#1A1A1A", font_style=1,
                               align="center", valign="middle")))
    # Subtitle (centered)
    out.append(cell(next(idgen),
                    "Verticals across (Strategy → Capability → BVD → ORS → Fulfillment → Assurance → Billing)  ·  "
                    "Domains down (Service / Resource)  ·  47 stable heat-map anchors",
                    margin, margin + 24, body_w, 14,
                    style_text(font_size=8, font_color="#555",
                               align="center", valign="middle")))

    # Matrix
    matrix_y = margin + 42
    grid_xml, _, _ = emit_grid_roadmap(idgen,
                                       x_start=margin,
                                       y_start=matrix_y)
    out.append(grid_xml)

    # Footer at bottom
    footer_h = 26
    footer_y = PAGE_H - margin - footer_h
    fields = [
        ("Document", "OSS Capability Map"),
        ("Author", "Adam Moyes"),
        ("Version", "1.0"),
        ("Last Updated", "11 May 2026"),
    ]
    out.append(emit_footer(idgen, margin, footer_y, body_w, footer_h, fields))

    return "\n".join(out)


# ----------------------------------------------------------------------
# Top-level: emit the .drawio file
# ----------------------------------------------------------------------

def main():
    # Build pages with separate ID counters per page
    # (drawio requires unique IDs only within a page)
    s2r_body = build_s2r_page(count(2))
    ops_body = build_ops_page(count(2))
    comb_body = build_combined_page(count(2))
    road_body = build_roadmap_page(count(2))

    pages = []
    # Roadmap page — drawio's A3 landscape preset (1654 x 1169 pt) — page 1
    pages.append(build_page("Roadmap", road_body, 1654, 1169))
    # S2R page — A3 landscape preset
    pages.append(build_page("S2R area", s2r_body, 1654, 1169))
    # Operations page — A3 landscape preset, extended height for dense ORS row
    pages.append(build_page("Operations area", ops_body, 1654, 1400))
    # Combined page — A2 landscape preset (2339 x 1654)
    pages.append(build_page("Combined", comb_body, 2339, 1654))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<mxfile host="capability-map-generator" agent="python-build_drawio.py" '
        f'modified="{now}" version="22.0.0" type="device">\n'
        + "\n".join(pages) +
        "\n</mxfile>\n"
    )

    OUT.write_text(xml)
    print(f"wrote {OUT.name} ({OUT.stat().st_size:,} bytes, {len(pages)} pages)")


if __name__ == "__main__":
    main()
