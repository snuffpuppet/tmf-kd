# TMF Knowledge Base

A normative TMF (TM Forum) reference corpus, built to support mapping work from
current-state monolithic OSS systems toward TMF target-state architecture organised
on the **PSR (Product, Service, Resource)** modelling principle, with explicit
production-vs-commercial separation.

## What's in here

The corpus represents three architectural layers plus foundations, every claim
backed by verbatim citation from a primary TMF source:

| Layer | Source | Pages |
|-------|--------|-------|
| Foundations (concepts, principles, domains, lifecycle) | GB991 v25.5 | 7 |
| Process — operational L2 process groups | GB921 v25.5 (Excel master) | 29 across 3 domains |
| Data — Aggregate Business Entities (ABEs) | GB922 (Product, Service, Common, Resource) | 56 across 4 categories |
| Component — ODA Functional Blocks | GB1022 v1.1.0 + IG1167 v6.0.0 summary | 6 |

**Total:** 117 wiki pages, lint clean.

Top-level docs:

- **`README.md`** (this file) — human overview
- **`AGENTS.md`** — orientation for AI agents resuming work
- **`TODO.md`** — outstanding tasks
- **`CLAUDE.md`** — agent constitution (verbatim discipline, anatomies, lint rules)

## How to use it

### Browse in Obsidian

The corpus is designed for [Obsidian](https://obsidian.md/). Open the project
root as a vault — wikilinks resolve, the graph view becomes meaningful, frontmatter
renders.

Start at `wiki/index.md` for the top-level catalogue.

### Run the linter

```bash
python3 lint/lint.py
```

Should print `PASS — 117 page(s) checked, 0 findings.` The linter checks
frontmatter, page anatomy, trilateral linking (eTOM ↔ SID ↔ ODA), bidirectional
consistency, wikilink resolution, and source-file existence.

### Use it for mapping work

Navigate the wiki to find:

- **eTOM L2 processes** that resemble functions in your monolith
  (`wiki/etom/{service,resource,product}-domain/`)
- **SID ABEs** representing the data your monolith manipulates
  (`wiki/sid/{product,service,resource,common}/`)
- **ODA Functional Blocks** representing the target-state component decomposition
  (`wiki/oda/functional-blocks/`)
- **Foundation concepts** establishing the canonical vocabulary
  (`wiki/foundations/`)

Open questions live in `wiki/open-questions.md` (39 filed during v1).

## Setup

Required tools:

- **macOS:** `brew install poppler` — provides `pdftotext` and `pdfinfo` for PDF
  extraction
- **Python 3** with `pyyaml`, `pandas`, `openpyxl`:
  ```bash
  pip3 install pyyaml pandas openpyxl
  # (Homebrew Python may require --break-system-packages)
  ```
- **Obsidian** (optional but strongly recommended for browsing)

## Project structure

```
.
├── README.md         ← you are here
├── AGENTS.md         ← orientation for AI agents resuming work
├── TODO.md           ← outstanding tasks
├── CLAUDE.md         ← agent constitution (binding discipline)
├── .gitignore
├── raw/              ← TMF source material
│   ├── tmf/          ← primary TMF sources (immutable; source of truth)
│   │   ├── etom/     ← GB921 Excel + decomposition PDFs
│   │   ├── sid/      ← GB922 (Product, Service, Common, Resource)
│   │   ├── oda/      ← GB1022, IG1167
│   │   └── foundations/   ← GB991
│   ├── tmf-adjacent/ ← MEF, ETSI, ITU (initially empty)
│   └── extracted/    ← markdown working copies (regenerable from raw/tmf/)
├── wiki/             ← the corpus content (read in Obsidian)
│   ├── index.md      ← top-level catalogue
│   ├── log.md        ← append-only event history
│   ├── open-questions.md
│   ├── etom/         ← process layer (eTOM L2s by domain)
│   ├── sid/          ← data layer (ABEs by category)
│   ├── oda/          ← component layer (ODA Functional Blocks)
│   ├── foundations/  ← cross-framework concepts (GB991)
│   └── views/        ← practitioner cross-cuts (derivative; empty in v1)
├── lint/             ← deterministic linter (Python)
├── templates/        ← page templates (one per page type)
└── project/          ← SECURITY BOUNDARY — empty by design (see below)
```

## Adding a new TMF document — the ingest process

When you obtain a new TMF specification (PDF or xlsx), use this workflow.

### Step 1 — place the file

Drop it into the appropriate `raw/tmf/` subdirectory:

| Document type                                     | Subdirectory          |
|---------------------------------------------------|-----------------------|
| eTOM (GBxxx process documents — GB921, addenda)   | `raw/tmf/etom/`       |
| SID (GB922 ABE documents)                         | `raw/tmf/sid/`        |
| ODA (GB1022, IG11xx)                              | `raw/tmf/oda/`        |
| Cross-framework / foundational (GB991-style)      | `raw/tmf/foundations/`|
| Adjacent standards (MEF, ETSI, ITU)               | `raw/tmf-adjacent/`   |

### Step 2 — instruct an AI agent (Claude Code)

A simple prompt works:

> I've added `raw/tmf/etom/GB921F_..._v25.5.pdf` to the corpus. Please ingest it
> following the workflow in `AGENTS.md`.

For Excel files specifically:

> I've added the GB921F Excel master to `raw/tmf/etom/`. Please ingest using the
> openpyxl pattern documented in `AGENTS.md` and prior `wiki/log.md` entries.

If you want the agent to start fresh after a context clear, see the resume prompt
in `AGENTS.md` ("First three things to do in a new session").

### Step 3 — what the agent does

Per the settled workflow (full detail in `AGENTS.md` "How to ingest more material"):

1. **Verify scope and GA status** — checks PDF metadata for "Release Status:
   Production". For pre-release/draft, pauses and asks. Out-of-scope material is
   declined.
2. **Extracts** to `raw/extracted/` mirroring the source path:
   - PDF → `pdftotext -layout source.pdf raw/extracted/.../source.md`
   - Excel → Python script (openpyxl) producing markdown table per sheet
3. **Identifies page type** — `etom-l2`, `sid-abe`, `oda-component`, `foundation`,
   or `view` (per CLAUDE.md §5).
4. **Writes wiki pages** by copying the relevant `templates/{type}.md` and filling
   verbatim from source — IDs, names, attributes copied exactly, never paraphrased.
   Citations (`— SOURCE-ID §X.Y, p. NN`) at the end of quoted blocks.
5. **Populates trilateral cross-references** (eTOM ↔ SID ↔ ODA). Where the source
   doesn't establish a link, files an open question rather than guessing.
   Bidirectional consistency required (an ODA → SID link means the SID page needs
   a back-link to the ODA component).
6. **Updates** `wiki/index.md`, the relevant `_index.md` files, and appends an
   entry to `wiki/log.md` describing what was ingested, what was skipped, and any
   open questions filed.
7. **Runs the linter** — `python3 lint/lint.py` must PASS before declaring the
   ingest complete. Fixes any issues surfaced.

### Step 4 — review and commit

Once the agent reports completion:

```bash
python3 lint/lint.py        # confirm it passes
git status                  # review what was added/changed
git add -A
git commit -m "Ingest <document name> — <brief summary>"
```

The agent will typically draft a comprehensive commit message if asked.

### What the agent will pause to ask about

- **Pre-release / draft documents** (PDF metadata not "Production")
- **Schema changes** — any new page type, new frontmatter field, or anatomy
  variation needs explicit confirmation
- **Scope ambiguity** — if it's not clear whether material falls in the in-scope
  PSR layers or should be skipped
- **Version mismatches** — if the new document references obsolete IDs from another
  spec, the agent surfaces options rather than silently resolving
- **User-decision open questions** — anything that requires your judgement rather
  than verbatim source extraction

## Discipline: what makes this corpus normative

The defining constraint: **TMF facts come exclusively from cited sources.**
Training-data recall is forbidden. If something isn't in `raw/` or `wiki/`, it
doesn't exist for project purposes. Ambiguities surface as open questions in
`wiki/open-questions.md` rather than being inferred away.

This means:

- Every wiki page cites a specific raw source (PDF or Excel) by section/page number
- Canonical names, IDs, attributes, status enums are preserved verbatim — never
  paraphrased
- Cross-references (eTOM ↔ SID ↔ ODA "trilateral linking") only exist when the
  source establishes them
- Version mismatches across specs are recorded honestly, not papered over
- A deterministic linter enforces page anatomy, link integrity, and bidirectional
  consistency

Full discipline lives in **`CLAUDE.md`** — read it before maintaining the corpus or
asking any AI agent to work on it.

## The `project/` security boundary

`project/` is reserved but **must not be populated by AI agents**. The user's
current-state company data goes here, mapped against the corpus locally. Reading
`project/` would put company data into LLM context, which is disallowed. The agent
constitution (CLAUDE.md §10.4) forbids any agent interaction with this directory.

The corpus is the reference; mapping work happens locally; company data stays out
of any cloud LLM.

## Status

v1 corpus complete. 117 wiki pages, lint clean, 39 open questions filed.

Outstanding work — depth, sweeps, decision points — is tracked in **`TODO.md`**.

## For AI agents

If you're an AI agent picking up this project:

1. Read **`AGENTS.md`** for orientation, working style, and the settled ingest
   workflow
2. Read **`CLAUDE.md`** for binding discipline rules
3. Read **`wiki/log.md`** for the most recent ingest events (worked examples of
   the ingest pattern)
4. Pick a task from **`TODO.md`**

## Acknowledgements

The wiki content reproduces verbatim excerpts from TM Forum specifications.
TM Forum specifications are © TM Forum and distributed under their IPR Mode
(commonly RAND). Consult source documents in `raw/tmf/` for specific copyright
notices.

Corpus design and structure are inspired by Andrej Karpathy's "LLM Wiki" pattern
(April 2026), with normative-corpus adaptations for TMF's verbatim-discipline
requirements.
