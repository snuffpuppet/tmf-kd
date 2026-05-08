# TMF Knowledge Base — Working Context

You are continuing work on a TMF Knowledge Base project. This document is the
complete handoff. Read it fully before acting.

## Goal

Build a TMF authoritative knowledge base in markdown, viewable in Obsidian,
that serves as the *only* permitted source of TMF knowledge for this project.
Training-data recall of TMF material is forbidden; if a fact is not in the
wiki, it does not exist for project purposes. Uncertainty surfaces as
explicit open questions, never as inferred answers.

A future phase (deliberately deferred) will add a project layer for
current-state team/process mapping. For v1 we are building only the TMF
authoritative corpus and the schema (CLAUDE.md) that governs it.

## Pattern

The project follows Karpathy's "LLM Wiki" pattern (April 2026 gist) with
adaptations for normative — not descriptive — corpus discipline:

- Three layers: raw sources (immutable), wiki (LLM-maintained markdown),
  schema (CLAUDE.md, the constitution).
- Operations: ingest, query, lint.
- Obsidian as the IDE; Claude Code as the maintainer.

Adaptations from Karpathy's pattern, because TMF is a normative corpus:

1. Distillation preserves TMF terminology *exactly*. No paraphrasing of
   canonical resource names, no smoothing of ambiguity, no inferring intent.
2. Training-data contamination is explicitly forbidden. The schema must
   make this uncompromising.
3. Ambiguities surface to `wiki/open-questions.md` rather than being
   resolved by the LLM.
4. A deterministic linter enforces page-type anatomy and link integrity.

## Scope

eTOM Service & Resource domains. Strategy/Infrastructure/Product Lifecycle
Management is out of scope. Operations, Fulfilment, Assurance, Billing
verticals are in scope where they touch Service or Resource domains.

In-scope L2 process groups:
- Service Configuration & Activation
- Service Problem Management
- Service Quality Management
- Service Guiding & Mediation
- Resource Provisioning
- Resource Trouble Management
- Resource Performance Management
- Resource Mediation & Reporting
- Resource Data Collection & Distribution

In-scope APIs: TMF638, TMF639, TMF641, TMF645, TMF633, TMF634, plus TMF630
as cross-cutting design conventions.

## Repository structure
tmf-kb/
├── CLAUDE.md                    # Schema — the constitution (write first)
├── raw/
│   ├── tmf/                     # TMF specs (user will populate)
│   │   ├── etom/
│   │   ├── sid/
│   │   └── apis/
│   └── tmf-adjacent/            # MEF, ODA, etc. — secondary authority
├── wiki/
│   ├── index.md                 # Catalog, categorised
│   ├── log.md                   # Append-only ingest/lint log
│   ├── etom/
│   │   ├── service-domain/
│   │   ├── resource-domain/
│   │   └── _index.md
│   ├── sid/
│   │   ├── service-abe.md
│   │   ├── resource-abe.md
│   │   ├── common-abe.md
│   │   └── _index.md
│   ├── apis/
│   │   ├── tmf630-design-guidelines.md
│   │   ├── tmf633-service-catalog.md
│   │   ├── tmf634-resource-catalog.md
│   │   ├── tmf638-service-inventory.md
│   │   ├── tmf639-resource-inventory.md
│   │   ├── tmf641-service-ordering.md
│   │   ├── tmf645-service-qualification.md
│   │   └── _index.md
│   ├── views/                   # Practitioner cross-cuts (e.g.
│   │   │                          service-activation-end-to-end.md).
│   │   │                          Derivative; cite, don't authorise.
│   │   └── _index.md
│   └── open-questions.md        # Ambiguities escalated to user
├── lint/
│   ├── lint.py
│   └── lint_checks.md
└── project/                     # Empty for v1. Reserved.
## Versioning policy

- Single version per spec, recorded in frontmatter (spec ID, version,
  retrieval date).
- eTOM: latest available version.
- SID and APIs: latest generally-available versions (not pre-release).
- eTOM/SID/API version mismatches are expected and acceptable; record them
  honestly. Where an older API references obsolete eTOM process IDs,
  resolve to current in the wiki and note the original reference. Do not
  paper over mismatches — file as open questions if material.

## Authority tiers

- `raw/tmf/` — primary authority. Wiki claims must cite a file here.
- `raw/tmf-adjacent/` — secondary authority (MEF, ODA, etc.). Cited
  differently; pages clearly marked as adjacent. Empty initially; user
  will populate as needed.

## Trilateral linking discipline

Every API wiki page must link to:
- The eTOM L2/L3 processes it supports
- The SID ABE entities it exposes

Every eTOM L2 wiki page must link to:
- The SID entities its processes manipulate
- The APIs that realise its processes

Every SID ABE page must link to:
- The APIs that expose it
- The eTOM processes that manipulate it

The linter enforces this. Pages without trilateral links fail lint.

## Page-type anatomy (to be finalised in CLAUDE.md)

Each page type has a fixed structure with frontmatter (spec ID, version,
retrieval date, source path in raw/, page type) and required sections.
Templates to be defined for: eTOM L2 page, SID ABE page, API page,
view page. The linter validates page anatomy against these templates.

## Source materials — download list

User is downloading from TMF (account required). Tiered list previously
agreed:

Tier 1 (essential for v1):
- GB921 eTOM, latest, including Service Domain and Resource Domain Addenda
- GB922 SID Service ABE, Resource ABE, Common Business Entities
- TMF638, TMF639, TMF641, TMF645, TMF633, TMF634 (User Guide,
  Specification, Swagger for each)
- TMF630 Design Guidelines

Tier 2 (TMF-adjacent, into raw/tmf-adjacent/):
- ODA Functional Architecture (IG1167 or equivalent)
- MEF 6.x, 10.x, 55 (relevant to user's Access/Delivery work)

Tier 3: deferred. (TAM, full ODA component specs, TMF640 unless service
activation enters scope, other Open APIs out of current Service/Resource
boundary.)

## Decisions made

1. Karpathy 3-layer pattern adopted, with normative-corpus adaptations.
2. Single-version-per-spec with frontmatter recording.
3. Two-tier authority structure (TMF / TMF-adjacent) from day one.
4. Trilateral linking (eTOM ↔ SID ↔ API) enforced by linter.
5. Practitioner-oriented `views/` folder alongside authoritative structure.
6. Ambiguity surfaces to `open-questions.md`, never resolved by LLM.
7. `project/` layer reserved but explicitly out of scope for v1.

## Open questions / deferred decisions

- Page-type templates: not yet drafted. First task after CLAUDE.md.
- Linter rules: shape agreed, specifics not drafted.
- Whether to add TMF640 to Tier 1 — depends on whether service activation
  process mapping enters early scope.
- Workflow for handling TMF spec revisions when they're released — defer
  until first revision encountered.

## What to do first (in order)

1. Confirm structure above is created (mkdir the tree if not present).
2. Draft `CLAUDE.md`. This is the highest-stakes file. It must:
   - Forbid TMF training-data recall absolutely. Agent must read raw/ or
     wiki/ files; if a fact is not in those files, the agent says so and
     does not infer.
   - Define the ingest workflow (raw → wiki, with trilateral linking).
   - Define the query workflow (read wiki, cite pages, refuse to answer
     beyond the wiki's content).
   - Define the lint workflow.
   - Define page-type anatomies for eTOM L2, SID ABE, API, view.
   - Define frontmatter schema.
   - Define the open-questions discipline.
   - Define index.md and log.md update obligations.
   Draft it, present it to the user for review, iterate.
3. After CLAUDE.md is settled, draft page-type templates as separate
   files in a templates/ folder (or inlined in CLAUDE.md, user to choose).
4. After templates settled, draft the linter (Python, simple, deterministic).
5. Only then begin ingestion of any TMF source. The first ingest is a
   small one (TMF630 is a good candidate — short, foundational,
   exercises the page-type machinery).

## What NOT to do

- Do not begin ingestion before CLAUDE.md, templates, and linter are
  settled. The wiki built before the discipline is set will be wrong.
- Do not rely on training data for any TMF claim, even "obvious" ones.
- Do not fabricate cross-references. If a TMF document doesn't tell you
  which eTOM process an API supports, file an open question.
- Do not paraphrase canonical resource names, status enums, or
  attribute names. Preserve verbatim.
- Do not populate the project/ folder. It is reserved for a later phase.

## Tone and working style preference

User prefers direct, frank, practical engagement. Pushes back when wrong.
Values getting decisions made over hedging. Values explicit reasoning over
confident assertions. When uncertain, say so and ask. When making a
recommendation, give the recommendation and the reasoning, not a menu of
options without a lean.
