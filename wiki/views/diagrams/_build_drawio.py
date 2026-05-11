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
L2_HEIGHT_BASE = 90
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
    """Return an mxCell XML string (vertex)."""
    safe_value = escape(value)
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

def emit_l2_box(idgen, l2_id, x, y, w, parent="1"):
    """Emit an L2 box with name/desc/id text inside, plus any H5 children
    nested as containers within. Returns (cells_xml, total_height)."""
    h5s = H5S.get(l2_id, [])
    body_h = L2_NAME_HEIGHT + (len(h5s) * (H5_HEIGHT + H5_GAP) if h5s else 0) + L2_PADDING
    box_h = max(L2_HEIGHT_BASE, body_h)

    box_id = next(idgen)
    name = L2_NAME[l2_id]
    desc = L2_DESC[l2_id]
    anchor = L2_ANCHOR[l2_id]
    pid_label = l2_id + ("*" if name.endswith("*") else "")
    name_clean = name.rstrip("*")

    # The L2 box itself — container, white fill, mid-color stroke.
    # Stroke color depends on which area this L2 lives in (set by caller via parent placement;
    # for simplicity we use S2R_MID universally here and override in the combined builder).
    box_style = style_box(L2_FILL, S2R_MID, font_size=10,
                          container=True, align="left", valign="top")
    out = [cell(box_id, "", x, y, w, box_h, box_style, parent=parent)]

    # Inside-the-L2 children use box_id as parent; positions are relative to the L2's geometry.
    # Header: ID line (small monospace-style, top-left)
    id_label_id = next(idgen)
    out.append(cell(id_label_id, pid_label, 6, 4, w-12, 14,
                    style_text(font_size=9, font_color=S2R_MID, font_style=1, align="left"),
                    parent=box_id))
    # Name
    name_id = next(idgen)
    out.append(cell(name_id, name_clean, 6, 18, w-12, 18,
                    style_text(font_size=11, font_color="#1A1A1A", font_style=1, align="left"),
                    parent=box_id))
    # Desc
    desc_id = next(idgen)
    out.append(cell(desc_id, desc, 6, 36, w-12, 14,
                    style_text(font_size=8, font_color=DESC_COLOR, font_style=2, align="left"),
                    parent=box_id))

    # H5 children — yellow containers stacked below, each with name+desc+src+anchor inside
    h5_y = L2_NAME_HEIGHT
    for (h5_anchor, h5_name, h5_src, h5_desc) in h5s:
        h5_id = next(idgen)
        h5_style = style_box(H5_FILL, H5_STROKE, font_size=8,
                             container=True, align="left", valign="top")
        out.append(cell(h5_id, "", 6, h5_y, w-12, H5_HEIGHT, h5_style, parent=box_id))
        # H5 children
        h5_name_id = next(idgen)
        out.append(cell(h5_name_id, h5_name, 4, 2, w-20, 14,
                        style_text(font_size=9, font_color="#6A4810", font_style=1, align="left"),
                        parent=h5_id))
        h5_desc_id = next(idgen)
        out.append(cell(h5_desc_id, h5_desc, 4, 16, w-20, 14,
                        style_text(font_size=7, font_color="#6A4810", font_style=2, align="left"),
                        parent=h5_id))
        h5_src_id = next(idgen)
        out.append(cell(h5_src_id, h5_src + "  —  " + h5_anchor, 4, 32, w-20, 14,
                        style_text(font_size=6, font_color="#999999", align="left"),
                        parent=h5_id))
        h5_y += H5_HEIGHT + H5_GAP

    # Anchor ID footer (placed at bottom — relative to L2 box)
    anchor_id = next(idgen)
    out.append(cell(anchor_id, anchor, 6, box_h - 14, w-12, 12,
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
                xml, _ = emit_l2_box(idgen, lid, inner_x, inner_y, w, parent=cell_id)
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
    return f"""  <diagram id="{name.replace(' ','-')}" name="{escape(name)}">
    <mxGraphModel dx="1700" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
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
                    "  STRATEGY-TO-READINESS LIFECYCLE AREA — what to build / how to deliver",
                    PAGE_MARGIN, band_y, 1620, 26, band_style))

    s2r_xml, s2r_h = emit_grid(idgen, S2R_GRID, S2R_DARK, S2R_MID, S2R_CELL,
                                x_start=PAGE_MARGIN,
                                y_start=band_y + 30)
    out.append(s2r_xml)

    ops_band_y = band_y + 30 + s2r_h + 15
    ops_band_style = style_box(OPS_DARK, OPS_DARK, font_size=12, font_color="#FFFFFF", font_style=1, align="left")
    out.append(cell(next(idgen),
                    "  OPERATIONS LIFECYCLE AREA — day-to-day customer operations",
                    PAGE_MARGIN, ops_band_y, 1620, 26, ops_band_style))

    ops_xml, _ = emit_grid(idgen, OPS_GRID, OPS_DARK, OPS_MID, OPS_CELL,
                           x_start=PAGE_MARGIN,
                           y_start=ops_band_y + 30)
    out.append(ops_xml)
    return "\n".join(out)


# ----------------------------------------------------------------------
# Top-level: emit the .drawio file
# ----------------------------------------------------------------------

def main():
    counter = count(2)  # 0 and 1 are reserved for root/parent

    # Build pages with separate ID counters per page (drawio requires unique IDs only within a page)
    s2r_body = build_s2r_page(count(2))
    ops_body = build_ops_page(count(2))
    comb_body = build_combined_page(count(2))

    pages = []
    # S2R page — A3 landscape (1684 x 1190 pt at 1 pt/px)
    pages.append(build_page("S2R area", s2r_body, 1684, 1190))
    # Operations page — A3 landscape
    pages.append(build_page("Operations area", ops_body, 1684, 1400))
    # Combined page — A2 landscape (2384 x 1684)
    pages.append(build_page("Combined", comb_body, 2384, 1684))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<mxfile host="capability-map-generator" agent="python-build_drawio.py" '
        f'modified="{now}" version="22.0.0" type="device">\n'
        + "\n".join(pages) +
        "\n</mxfile>\n"
    )

    OUT.write_text(xml)
    print(f"wrote {OUT.name} ({OUT.stat().st_size:,} bytes, 3 pages)")


if __name__ == "__main__":
    main()
