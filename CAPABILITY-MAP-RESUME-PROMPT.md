# Resume prompt — OSS Capability Map refinement

Drop this entire file into a fresh session as your opening message, then issue
the refinement instruction. The agent will orient itself and follow the
established conventions without needing them re-explained.

---

You are continuing work on the **OSS Capability Map** in the TMF Knowledge Base
at `/Users/adam/projects/tmf-kd`. The capability map renders all 47 stable
heat-map anchors (33 eTOM L2 process groups + 14 H5 sub-capabilities) across
both Lifecycle Areas of GB991 §1.1.2 (Strategy-to-Readiness + Operations) for
the Service and Resource Domains.

## ORIENT BEFORE ANY CHANGE — read these files end-to-end, in order

1. **`CLAUDE.md`** at the project root — binding constitution. Note especially:
   §1 verbatim discipline (no paraphrasing of TMF normative text), §10.3 (no
   embellishment of names), §10.4 `project/` security boundary (do NOT read or
   write that folder), §13 Obsidian wikilink conventions.
2. **This file** in full.
3. **`wiki/views/diagrams/`** directory listing — see what's there.
4. **`wiki/views/capability-map.md`** + **`wiki/views/capability-map-s2r.md`**
   `## Visual exports` sections — they index every artefact in `diagrams/`.
5. **`wiki/log.md`** — recent design iterations on the capability-map diagrams.
   Use `grep -n 'DIAGRAMS —' wiki/log.md | tail -10` to index recent diagram
   entries, then read the relevant slices via `Read` with `offset`/`limit` —
   this is much cheaper than `tail -300` (which can blow the tool-output cap).
6. Run `python3 lint/lint.py` — must report `PASS — 147 page(s) checked, 0
   findings.` If it doesn't, fix the lint failure before any other work.

## CORE DIRECTIVE — always export PDF and PNG

Whenever you change ANY of the following, regenerate the corresponding rendered
outputs in the same turn, before committing:

| Source you changed | Regenerate command |
|---|---|
| Any `*.html` file in `wiki/views/diagrams/` | `bash wiki/views/diagrams/render.sh` (regenerates PDF + PNG for every entry in the script's `TARGETS` array — currently 4 HTML files) |
| `_build_drawio.py` | `python3 wiki/views/diagrams/_build_drawio.py` (regenerates `capability-map.drawio`) |
| `_apply_l2_descriptions.py` or `_apply_h5_descriptions.py` | Run that script, then `bash render.sh` to refresh exports |

**Never commit a change to a generator or HTML file without also committing the
regenerated PDF/PNG/.drawio outputs.** The render pipeline is the contract.

To verify a `.drawio` page visually before committing:
```bash
drawio --export --format png --page-index 1 \
  --output /tmp/preview.png \
  wiki/views/diagrams/capability-map.drawio
```

## Files in `wiki/views/diagrams/`

### Sources (edit these)
- **`_build_drawio.py`** — Python generator for `capability-map.drawio`. Holds
  L2/H5 data dicts (`L2_NAME`, `L2_DESC`, `L2_ANCHOR`, `H5S`, `S2R_GRID`,
  `OPS_GRID`, `FULL_VERTICAL_NAMES`) and layout functions (`emit_l2_box`,
  `emit_grid_roadmap`, `emit_footer`, `build_roadmap_page`).
- **`_apply_l2_descriptions.py`**, **`_apply_h5_descriptions.py`** — apply
  description dictionaries to the HTML files (idempotent; insert `<div
  class="*-desc">` lines after each name).
- **`capability-map-s2r.html`**, **`capability-map.html`**,
  **`capability-map-combined.html`**, **`capability-map-roadmap.html`** —
  hand-built HTML sources, one per view. These are NOT generated from
  `_build_drawio.py`; they're independent.
- **`render.sh`** — Chrome-headless render script; regenerates PDF + PNG for
  every HTML in the `TARGETS` array.

This prompt file lives at the **repo root** as `CAPABILITY-MAP-RESUME-PROMPT.md`
(not inside `wiki/views/diagrams/`).

### Rendered artefacts (regenerate, don't hand-edit)
- `*.pdf` — print-quality, A2/A3 landscape per the HTML's `@page` rule
- `*.png` — 2× DPI for screen / Obsidian embedding
- `capability-map.drawio` — single-page editable draw.io file (Roadmap
  layout only; per-area views deprecated from .drawio per user direction)

## Established design decisions — do not relitigate

### `capability-map.drawio` (single Roadmap page)
- **A3 landscape** at drawio's preset dimensions (`1654×1169` pt, NOT
  `1684×1190` which is closer to A2). Matches drawio's `gPresetPageFormats.a3`.
- **Triple-redundant white background**: `background="#FFFFFF"` +
  `pageBackground="#FFFFFF"` attributes on `mxGraphModel` + explicit white
  rectangle as the first cell on the page (`id="bg"`). Survives any drawio
  theme.
- **Roadmap orientation**: 7 vertical columns across the top (3 S2R + 4
  Operations) under two Lifecycle Area band labels; 2 domain rows (Service /
  Resource) down the left side.
- **Verbatim TMF terms in bands** — *"STRATEGY-TO-READINESS"* and
  *"OPERATIONS"* only. No "LIFECYCLE AREA" suffix or descriptive em-dash
  phrases (CLAUDE.md §1 verbatim discipline).
- **Full vertical names in column headers** via `FULL_VERTICAL_NAMES` mapping
  (e.g. `BVD` → `BUSINESS VALUE DEVELOPMENT`). Short labels stay in the data
  for any future use in rotated/vertical labels.
- **Compact-mode L2 boxes** for A3 fit:
    - 2-line height allocation for L2 name (28pt) and L2 desc (24pt) so
      wrapped text never overlaps the next cell
    - 2-line height allocation for H5 desc (26pt)
    - L2 anchor footer + H5 source line both DROPPED in compact mode (info
      preserved on the wiki source pages)
    - Constants: `ROAD_L2_HEIGHT_BASE=72`, `ROAD_L2_NAME_HEIGHT=70`,
      `ROAD_H5_HEIGHT=44`, `ROAD_H5_GAP=3`, `ROAD_CELL_PADDING=4`,
      `ROAD_L2_GAP=3`
- **L2 box border colour** matches Lifecycle Area (blue `#2A5298` for S2R,
  green `#2A8268` for Ops); cell backgrounds tinted similarly.
- **Centred title** `OSS Capability Map — Roadmap Layout` at top.
- **Footer** at bottom: dark filler (`#3D3D3D`, **no text** — purely visual
  delimiter) + 4 alternating blue (`#5BB6E8`) label / white content pairs:
  `Document = OSS Capability Map`, `Author = Adam Moyes`, `Version = 1.0`,
  `Last Updated = <date>`.
- **Legend / note strip** between matrix bottom and footer:
    - Light blue-gray fill (`#EEF2F7`), subtle gray border (`#C8D4E0`)
    - Italic dark-blue text (`#3A4A5E`) at 9pt
    - Thick blue left-edge bar (`#5BB6E8`, 4pt wide) — info-callout indicator
    - Note text cell starts at `x = margin + bar_w` (NOT overlapping the bar);
      `spacingLeft=12` adds internal padding so the ⓘ icon has breathing room
    - Currently explains the `*` on multi-vertical L2 IDs (see below)
- **Multi-vertical `*` convention**: GB921 v25.5's `Vertical Group` field places
  some L2s under more than one vertical. The diagram renders each L2 once under
  its primary vertical and suffixes the L2 ID with `*` to flag the multi-vertical
  status. Currently two L2s carry it: **`1.5.5*`** Resource Order Management
  (Fulfillment + Operations Readiness & Support) and **`1.5.7*`** Resource Data
  Management (all four OFAB verticals — Assurance + Billing + Fulfillment + ORS).
  The asterisks are baked into `L2_NAME` values in `_build_drawio.py` and parsed
  out in the rendering loop; the legend strip on the Roadmap page documents them
  for the reader.
- **Newline rendering**: `cell()` helper converts `\n` → `&#10;` so multi-line
  values render as actual line breaks under `html=1` mode.

### HTML renders (separate from .drawio; per-area + combined + roadmap)
- 4 HTML files; each has `@page { size: A3 landscape; }` (or A2 for the
  area-stacked combined view)
- Boxes-in-boxes layout via CSS Grid; H5s nested visually inside parent L2
- Same description data as .drawio (sourced from `_apply_*.py` dicts)
- Cross-Lifecycle composability marked with `⇄` pills on participating cells
  (Test maturity row, Anomaly pair, Catalog 4-L2 lifecycle)
- Domain-header descriptions are obvious and have been removed (don't add them
  back)

## Workflow conventions

- **Verbatim discipline (CLAUDE.md §1)**. Don't paraphrase TMF names. Don't add
  "LIFECYCLE AREA" or other embellishment. If unsure whether something is
  TMF-canonical, check the source PDF/Excel under `raw/`.
- **Branch → commit → merge → push** for any meaningful change:
  ```bash
  git checkout -b <feature-branch>
  git add -A && git commit -F /tmp/commit-msg.txt
  git checkout main && git merge --no-ff <feature-branch> -F /tmp/merge-msg.txt
  git branch -d <feature-branch>
  rm /tmp/commit-msg.txt /tmp/merge-msg.txt
  git push origin main
  ```
  Use a message file (`/tmp/commit-msg.txt`) instead of inline `-m` to avoid
  shell-quoting issues with apostrophes.
- **Commit message footer**: `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`
- **Lint must pass**: `python3 lint/lint.py` before declaring done.
- **Add a `wiki/log.md` entry** for any meaningful corpus change. Use the
  pattern `## YYYY-MM-DDTHH:MMZ — DIAGRAMS — <short summary>` followed by
  Pages created/updated, Lint result, Notes.
- **Don't use Plan mode** for simple refinement. Just propose tightly, get
  sign-off if non-trivial, do the change, commit.

## Final sanity check before declaring done

1. `python3 lint/lint.py` → PASS
2. Every modified HTML / `_build_drawio.py` has its corresponding regenerated
   PDF / PNG / `.drawio` committed in the same commit
3. Log entry added to `wiki/log.md`
4. Branch deleted, working tree clean, `git status` shows in sync with origin

## Now do this

1. Read the orientation files listed above (`CLAUDE.md`, this file, the wiki
   view pages, `wiki/log.md` tail). Run lint.
2. Confirm orientation done in 4–6 lines: current corpus state, latest
   capability-map design state, lint result.
3. Wait for the user's refinement instruction.
