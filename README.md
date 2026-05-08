# TMF Knowledge Base

A normative TMF (TM Forum) reference corpus, built to support mapping work from
current-state monolithic OSS systems toward TMF target-state architecture organised
on the **PSR (Product, Service, Resource)** modelling principle, with explicit
production-vs-commercial separation.

## What's in here

The repository has two parts:

- **`tmf-kb/`** — the corpus itself (117 wiki pages, lint clean)
- Top-level docs (`README.md`, `AGENTS.md`, `TODO.md`) — orientation for humans, AI
  agents resuming work, and the outstanding task list respectively

The corpus represents three architectural layers plus foundations, every claim
backed by verbatim citation from a primary TMF source:

| Layer | Source | Pages |
|-------|--------|-------|
| Foundations (concepts, principles, domains, lifecycle) | GB991 v25.5 | 7 |
| Process — operational L2 process groups | GB921 v25.5 (Excel master) | 29 across 3 domains |
| Data — Aggregate Business Entities (ABEs) | GB922 (Product, Service, Common, Resource) | 56 across 4 categories |
| Component — ODA Functional Blocks | GB1022 v1.1.0 + IG1167 v6.0.0 summary | 6 |

## How to use it

### Browse in Obsidian

The corpus is designed for [Obsidian](https://obsidian.md/). Open `tmf-kb/` as a
vault — wikilinks resolve, the graph view becomes meaningful, frontmatter renders.

Start at `tmf-kb/wiki/index.md` for the top-level catalogue.

### Run the linter

```bash
cd tmf-kb
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

Open questions live in `tmf-kb/wiki/open-questions.md` (39 filed during v1).

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
├── README.md              ← you are here
├── AGENTS.md              ← orientation for AI agents resuming work
├── TODO.md                ← outstanding tasks
├── .gitignore
└── tmf-kb/                ← the corpus
    ├── CLAUDE.md          ← agent constitution (verbatim discipline, anatomies, lint rules)
    ├── raw/
    │   ├── tmf/           ← primary TMF sources (immutable; source of truth)
    │   ├── tmf-adjacent/  ← adjacent standards (initially empty)
    │   └── extracted/     ← markdown working copies (regenerable from raw/tmf/)
    ├── wiki/
    │   ├── index.md       ← top-level catalogue
    │   ├── log.md         ← append-only event history
    │   ├── open-questions.md
    │   ├── etom/          ← process layer (eTOM L2s by domain)
    │   ├── sid/           ← data layer (ABEs by category)
    │   ├── oda/           ← component layer (ODA Functional Blocks)
    │   ├── foundations/   ← cross-framework concepts (GB991)
    │   └── views/         ← practitioner cross-cuts (derivative; empty in v1)
    ├── lint/              ← deterministic linter (Python)
    ├── templates/         ← page templates (one per page type)
    └── project/           ← SECURITY BOUNDARY — empty by design (see below)
```

## Discipline: what makes this corpus normative

The defining constraint: **TMF facts come exclusively from cited sources.**
Training-data recall is forbidden. If something isn't in `raw/` or `wiki/`, it
doesn't exist for project purposes. Ambiguities surface as open questions in
`tmf-kb/wiki/open-questions.md` rather than being inferred away.

This means:

- Every wiki page cites a specific raw source (PDF or Excel) by section/page number
- Canonical names, IDs, attributes, status enums are preserved verbatim — never
  paraphrased
- Cross-references (eTOM ↔ SID ↔ ODA "trilateral linking") only exist when the
  source establishes them
- Version mismatches across specs are recorded honestly, not papered over
- A deterministic linter enforces page anatomy, link integrity, and bidirectional
  consistency

Full discipline lives in **`tmf-kb/CLAUDE.md`** — read it before maintaining the
corpus or asking any AI agent to work on it.

## The `project/` security boundary

`tmf-kb/project/` is reserved but **must not be populated by AI agents**. The user's
current-state company data goes here, mapped against the corpus locally. Reading
`project/` would put company data into LLM context, which is disallowed. The agent
constitution (CLAUDE.md §10.4) forbids any agent interaction with this directory.

The corpus is the reference; mapping work happens locally; company data stays out
of any cloud LLM.

## Status

v1 corpus complete. 117 wiki pages, lint clean, 39 open questions filed. Two
commits: initial v1 build (`fdf60b0`) and HANDOFF rewrite (`a3e5048`).

Outstanding work — depth, sweeps, decision points — is tracked in **`TODO.md`**.

## For AI agents

If you're an AI agent picking up this project:

1. Read **`AGENTS.md`** for orientation, working style, and the settled ingest
   workflow
2. Read **`tmf-kb/CLAUDE.md`** for binding discipline rules
3. Read **`tmf-kb/wiki/log.md`** for the most recent ingest events (worked examples
   of the ingest pattern)
4. Pick a task from **`TODO.md`**

## Acknowledgements

The wiki content reproduces verbatim excerpts from TM Forum specifications.
TM Forum specifications are © TM Forum and distributed under their IPR Mode
(commonly RAND). Consult source documents in `tmf-kb/raw/tmf/` for specific
copyright notices.

Corpus design and structure are inspired by Andrej Karpathy's "LLM Wiki" pattern
(April 2026), with normative-corpus adaptations for TMF's verbatim-discipline
requirements.
