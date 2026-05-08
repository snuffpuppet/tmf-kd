# AGENTS.md — Orientation for AI Agents Resuming Work

You are continuing an in-progress project. The v1 corpus is built and committed.
This file orients you. Read it fully, then `CLAUDE.md` (the binding
constitution), then check `wiki/log.md` (event history) before acting.

For the **outstanding task list**, see `TODO.md`.
For **human-facing project context**, see `README.md`.

## In one paragraph

This project is a TMF authoritative knowledge base in markdown, viewable in Obsidian.
It serves the user's mapping goal: current-state monolithic OSS → TMF target state
organised on the **PSR (Product, Service, Resource) modelling principle**, with
explicit production-vs-commercial separation. Three architectural layers are
represented: process (eTOM), data (SID), component (ODA), with foundational concepts
above. The corpus is built; v1 ingests are complete; remaining work is depth and
sweep, not new structure. The user cannot share company data with cloud LLMs, so the
corpus serves as a self-contained reference they consult during their own analytical
work — `project/` is therefore a permanent security boundary and is empty by
design.

## First three things to do in a new session

1. **Read `CLAUDE.md` in full.** It is the constitution — verbatim discipline,
   training-data prohibition, page-type anatomies, ingest workflow, lint rules,
   forbidden actions. It overrides default Claude behaviour wherever it speaks.
2. **Read `wiki/log.md`** end-to-end. It is the append-only audit trail of
   every ingest event, every schema decision, every deferral. It tells you exactly
   where you left off. The most recent entry is the v1 completion summary.
3. **Run the linter:** `python3 lint/lint.py`. Should print
   `PASS — 117 page(s) checked, 0 findings.` If it doesn't, something has drifted
   since the v1 commit and that is your first task.

After those three, read `wiki/open-questions.md` for the 39 OQs filed during
v1 — many are deferral markers that point at items in `TODO.md`.

## Current state (v1 complete, committed)

- 117 wiki pages, lint clean
- 7 foundation pages from GB991
- 56 SID ABE pages from GB922 (4 categories: Product, Service, Resource, Common)
- 29 eTOM L2 pages from GB921 Excel master (3 domains × OFAB verticals)
- 6 ODA Functional Block pages from GB1022 + IG1167 summary in `wiki/oda/_index.md`
- 39 open questions filed (`wiki/open-questions.md`)
- Initial trilateral sweep done — 16 eTOM/SID pages have reciprocal ODA back-links
- Git committed at the repo root

The corpus is **structurally complete and analytically usable**. The user can already
do meaningful PSR mapping work navigating the wiki in Obsidian.

## How to ingest more material (if user adds source files)

The settled workflow:

1. **Verify source** — confirm in scope per CLAUDE.md §3, GA status from PDF metadata
   ("Release Status: Production"). For pre-release, ask user. For Excel files use
   `pandas` + `openpyxl` (already installed).
2. **Extract** — `pdftotext -layout <src.pdf> <dst.md>` mirrors source path under
   `raw/extracted/`. Excel: Python script using openpyxl producing markdown table.
3. **Identify page type** — `etom-l2`, `sid-abe`, `oda-component`, `foundation`, or
   `view` (CLAUDE.md §5).
4. **Write pages** — copy the relevant `templates/{type}.md`, fill verbatim. Citation
   format `— SOURCE-ID §X.Y, p. NN` at end of quoted blocks.
5. **Trilateral sections** — populate where sources are explicit; file an open
   question and use `See open-questions.md — OQ-NNN` (or wikilink format
   `See [[wiki/open-questions#OQ-NNN]]`) where uncertain. **Bidirectional sweep is
   real work** — when you add an ODA→SID link, the SID page needs a back-link.
6. **Update** `wiki/index.md`, the relevant `_index.md`, append to `wiki/log.md`.
7. **Lint** — `python3 lint/lint.py` must PASS before declaring complete.

Worked examples: the v1 log entries in `wiki/log.md` are documented ingest
events. The Python scripts I used to generate eTOM L2 pages from Excel are not
preserved as files (one-off generation), but the pattern is straightforward to
reproduce from the log entries' notes.

## What you must not do

The constitution in `CLAUDE.md` is binding. The non-negotiable items, in
priority of severity:

1. **No training-data recall for TMF facts.** If a fact isn't in `raw/` or `wiki/`,
   it doesn't exist for this project. Say "not in corpus", file an OQ. This rule is
   the entire reason the corpus exists; violating it once corrupts the trust model.
2. **Never read or write `project/`.** It is a security boundary, not a
   deferral. Reading `project/` would put company data in the LLM context, which
   the user has explicitly disallowed. CLAUDE.md §10.4.
3. **Don't modify `raw/`.** The only legitimate write target inside `raw/`
   is `raw/extracted/`. PDFs are immutable.
4. **Don't paraphrase canonical names, IDs, enums, attributes.** Verbatim or open
   question. Even obvious-looking smoothing corrupts the corpus.
5. **Don't resolve open questions yourself.** They escalate to the user. You can
   propose resolutions in your own message, but don't close OQs in
   `wiki/open-questions.md` without user direction.

## Working style — what the user expects

- **Be direct.** State conclusions before reasoning. When you have a recommendation,
  give it; don't present a menu of options. The user prefers decisions made over
  hedging.
- **Push back when wrong.** The user does. They expect the same in return. If a
  request would corrupt the corpus discipline, refuse and propose a compliant
  alternative.
- **Surface decisions you cannot make autonomously.** Schema additions, scope
  expansions, OQ resolutions are user calls. Use the AskUserQuestion tool for
  binary or multi-option choices. Don't ask about minor logistics.
- **The user has often said "continue" across many turns.** Take that as approval
  to maintain momentum on the established pattern. If you hit something genuinely
  blocking or ambiguous, surface it concisely and ask. Otherwise proceed.
- **Acknowledge mistakes promptly.** If you stated a TMF fact from training data,
  fabricated a cross-reference, or made a schema decision the user pushed back on,
  fix it cleanly and note it. Don't argue.
- **Keep messages tight.** Long messages of exploration text aren't valuable. Show
  outputs, decisions, and next-step questions.

## File map (quick reference)

- `CLAUDE.md` — the constitution. Read it first.
- `wiki/index.md` — top-level catalogue by category.
- `wiki/log.md` — append-only event history. Last entry tells you where you are.
- `wiki/open-questions.md` — 39 OQs.
- `templates/` — page templates (etom-l2, sid-abe, oda-component, foundation, view).
- `lint/lint.py` — deterministic linter. Run before declaring any ingest complete.
- `lint/lint_checks.md` — lint rules in prose.
- `raw/tmf/` — source PDFs and Excel (immutable). Do not modify.
- `raw/extracted/` — markdown working copies (regenerable).
- `wiki/{etom,sid,oda,foundations,views}/` — the corpus content.
- `project/` — DO NOT TOUCH. Security boundary.

## Tooling already installed

- `pdftotext -layout` from poppler (Homebrew) — PDF extraction (CLAUDE.md §2)
- `pandas` 3.0.2 + `openpyxl` 3.1.5 (via `pip --break-system-packages`) — Excel
  extraction
- `pyyaml` — required by linter
- Python 3 (Homebrew)

If extraction fails due to missing tools after a system change, reinstall via the
same paths and verify by re-running `python3 lint/lint.py`.
