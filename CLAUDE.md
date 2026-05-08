# TMF Knowledge Base — Agent Constitution

This file governs all agent behaviour in this repository. It takes precedence over default
Claude Code behaviour in every area it addresses.

The corpus is a TMF-authoritative reference for analytical work. The goal is process
mapping from a current-state monolithic OSS toward TMF target-state architecture organised
on the **PSR (Product, Service, Resource)** modelling principle. The knowledge base
represents this principle at three architectural layers — process (eTOM), data (SID), and
component (ODA) — and forms the reference vocabulary the user maps their internal systems
against.

---

## 1. The Cardinal Rule — Training-Data Prohibition

**TMF knowledge from training data is forbidden. No exceptions.**

If a TMF fact (process name, process ID, SID entity, ODA component, attribute name, status
enum, version number, cross-reference, or any other normative claim about TMF specifications)
is not present in a file under `raw/` or `wiki/`, it does not exist for the purposes of this
project.

The agent MUST NOT:
- State a TMF fact from memory, even if "certain" it is correct.
- Infer a cross-reference not stated in a raw source file.
- Fill in a gap by reasoning about what "must" be true.
- Paraphrase or reconstruct a canonical name, ID, enum, or attribute.
- Assume a mapping between an eTOM process, a SID entity, or an ODA component unless a raw
  source makes it explicit.

When a fact is not in the corpus, the agent says:
> "This is not in the corpus. I cannot answer from raw/ or wiki/. Filing an open question if
> appropriate."

This rule is uncompromising. Its purpose is to prevent training-data contamination from
corrupting a normative knowledge base. A wrong fact stated confidently is worse than an
acknowledged gap.

---

## 2. Authority Model

### Primary authority — `raw/tmf/`
Wiki claims MUST cite a file in `raw/tmf/`. If no such file exists, the claim cannot be made.

Subdirectories:
- `raw/tmf/etom/` — GB921 eTOM specifications and addenda
- `raw/tmf/sid/` — GB922 SID specifications
- `raw/tmf/oda/` — ODA Functional Architecture and component documents (e.g. IG1167)

### Secondary authority — `raw/tmf-adjacent/`
Adjacent standards if they become useful (initially empty; user populates). Wiki pages
drawing on these sources must be marked with `authority: adjacent` in frontmatter and may
not override claims from primary sources.

### Conflict between primary and adjacent
If an adjacent source contradicts a primary source, the primary source wins. The
contradiction itself is filed as an open question for awareness — it is not silently
ignored, and it is not resolved by editing the wiki to favour either side.

### Raw is immutable
Files in `raw/` MUST NOT be modified, renamed, deleted, or reorganised by the agent. The
agent's only legitimate write target inside `raw/` is `raw/extracted/` (see below). If a raw
source is wrong (typo, broken PDF), the agent files an open question and asks the user.

### Extracted working copies — `raw/extracted/`
TMF specs are PDFs. The Read tool can read PDFs but page-by-page; long specs are unworkable
that way. Before any ingest, the agent extracts the PDF to a markdown working copy under
`raw/extracted/`, mirroring the source path:

| Source file | Extracted copy |
|-------------|----------------|
| `raw/tmf/etom/GB921-eTOM-v22.5.pdf` | `raw/extracted/tmf/etom/GB921-eTOM-v22.5.md` |
| `raw/tmf/oda/IG1167-ODA-Functional-Architecture-v8.0.pdf` | `raw/extracted/tmf/oda/IG1167-ODA-Functional-Architecture-v8.0.md` |

Rules:
- The PDF is the source of truth. The extracted markdown is a working copy.
- Wiki frontmatter records both: `source_paths` (the PDFs) and `source_extract_paths` (the
  markdown). Citations in body text reference the PDF.
- Extraction quality is variable. Tables, footnotes, multi-column layouts, and figure
  captions may be lossy. If extraction is suspicious for a normative claim, the agent
  re-reads the PDF pages directly to confirm and notes any discrepancy as an open question.
- Extracted markdown is regenerated, not hand-edited. If a fix is needed, fix the extraction
  command and regenerate.
- **Extraction tool:** `pdftotext -layout` from poppler (macOS: `brew install poppler`).
  Layout-preserving mode keeps rough column structure for multi-column TMF documents.
  Command: `pdftotext -layout <source.pdf> <extracted.md>`. Settled 2026-05-08 during
  IG1167 assessment.

### The wiki — `wiki/`
Derived from raw sources. The wiki summarises and cross-links; it never adds or infers.
Every factual claim in a wiki page must be traceable to a specific raw source file.

---

## 3. Corpus Scope

The corpus represents PSR (Product, Service, Resource) at three architectural layers.

### eTOM (process layer)

In scope:
- **Service Domain L2 process groups:** Service Configuration & Activation, Service Problem
  Management, Service Quality Management, Service Guiding & Mediation
- **Resource Domain L2 process groups:** Resource Provisioning, Resource Trouble Management,
  Resource Performance Management, Resource Mediation & Reporting, Resource Data Collection
  & Distribution
- **Operational Product L2 process groups** that intersect Operations/Fulfilment/Assurance/
  Billing verticals — specific L2 list to be enumerated against GB921 at ingest. Expected
  coverage area includes customer order handling and billing/revenue management at the
  operational level. The exact L2s and their canonical eTOM groupings are determined from
  GB921 verbatim, not inferred.
- **OFAB verticals** (Operations, Fulfilment, Assurance, Billing) in scope where they
  intersect Product, Service, or Resource

Out of scope:
- The **Strategy / Infrastructure / Product Lifecycle Management (SIP) vertical** — this is
  strategic, not operational. The goal is mapping operational processes.

### SID (data layer)
- **Product ABE** entities
- **Service ABE** entities
- **Resource ABE** entities
- **Common Business Entities** (cross-cutting, supports all three layers)

### ODA (component layer)
- **All ODA functional domains** and their constituent components, as enumerated in the
  ingested ODA documents.
- Domain naming is taken verbatim from the source — the agent does not assume domain names
  or component groupings without source evidence.

### Out of scope for v1
- TMF Open APIs (TMF638/639/641/645/633/634) and TMF630 design conventions — these are the
  interface layer downstream of ODA components, not load-bearing for process / component
  mapping at v1.
- `project/` folder — see security boundary in §10.

### Partial ingestion
A single raw document (e.g. GB921) typically contains both in-scope and out-of-scope
material. The agent ingests only in-scope content. Skipped material is mentioned in the log
entry for the ingest, with section references, so the boundary is auditable.

When asked about out-of-scope material, the agent says so and declines to add it to the
corpus.

### Version selection policy
- **eTOM:** latest available version.
- **SID and ODA:** latest *generally-available* version. Pre-release/draft versions MUST
  NOT be ingested without explicit user confirmation. If a raw file appears to be
  pre-release (filename or document header indicates draft/pre-release/RC), the agent
  pauses ingest and asks the user before proceeding.
- Single version per spec. If a newer version of an already-ingested spec is added later,
  the agent flags this and asks the user how to proceed.
- eTOM/SID/ODA version mismatches across specs are expected and acceptable; record them
  honestly in frontmatter. Where an older document references obsolete IDs in another spec,
  resolve to the current ID in the wiki and note the original reference (see §7).

---

## 4. Workflows

### 4.1 Ingest Workflow

Triggered when the user places a new source file in `raw/` and asks for ingestion.

**Steps (in order — do not skip or reorder):**

1. **Verify the source is in scope and GA.**
   - Confirm the spec falls within §3 In-Scope.
   - Confirm the version is GA, not pre-release. If pre-release, ask user before proceeding.
   - If out-of-scope, decline and explain.

2. **Extract the PDF to `raw/extracted/`** (if not already present).
   - Mirror the source path under `raw/extracted/`.
   - Record any extraction warnings in the log entry.

3. **Read the extracted markdown.** Do not rely on memory of the document's contents.
   - For normative claims, cross-check against the PDF page directly using the Read tool's
     page parameter. Extracted markdown is convenient but PDFs are authoritative.

4. **Identify page type(s) to produce.**
   - GB921 produces eTOM L2 pages (one per in-scope L2).
   - GB922 produces SID ABE pages (one per ABE entity).
   - ODA documents produce ODA component pages (one per component) plus domain
     subdirectories as needed.
   - View pages are never produced from raw sources directly (see §5.4).

5. **Create wiki page(s)** following the anatomy for the applicable page type (§5).
   - Copy canonical names, IDs, and attributes verbatim from the source.
   - Do not paraphrase, smooth, or summarise normative terms.
   - Write the frontmatter exactly per the schema (§6).

6. **Populate trilateral links** (§7):
   - For each required link direction, search existing wiki pages for the target.
   - If the target wiki page exists, link it using Obsidian wikilink syntax (§13).
   - If the link cannot be determined from the raw source, do NOT guess — file an open
     question and use the `See open-questions.md — OQ-{NNN}` placeholder.

7. **Update `wiki/open-questions.md`** with any ambiguities encountered (§8).

8. **Update `wiki/index.md`**: add the new page(s) to the appropriate category section.
   Update relevant `_index.md` files (eTOM domain, SID category, ODA domain) with entries
   for new pages.

9. **Append to `wiki/log.md`**: record the ingest event (§9), including any partial-ingest
   skips with section references.

10. **Run the linter** (`python lint/lint.py`) and fix any failures before declaring the
    ingest complete.

### 4.2 Query Workflow

Triggered when the user asks a question about TMF content.

**Steps:**

1. **Read the relevant wiki pages.** Use `wiki/index.md` and inter-page links to find them.
   If the wiki doesn't have the answer, say so explicitly.

2. **Answer from the wiki only.** Cite the specific wiki page(s) and, where possible, the
   raw source section that underlies the wiki claim.

3. **Do not synthesise beyond what the wiki contains.** If the question requires a
   connection not already made in the wiki, acknowledge the gap rather than bridging it
   with inference.

4. **Do not use training data.** Even if you believe a cross-reference is "obviously"
   correct, if it isn't in the wiki, it is an open question.

5. **If the question reveals a corpus gap**, offer to file an open question.

### 4.3 Lint Workflow

The linter runs:
- After every ingest (mandatory)
- On explicit user request (`python lint/lint.py`)

Lint failures must be resolved before the ingest is marked complete. The linter checks:
- Page-type anatomy: required sections present per type (§5)
- Frontmatter: required fields present and correctly typed (§6)
- Trilateral links: all required directions populated or flagged with `OQ-{NNN}` (§7)
- Bidirectional consistency: if A links to B in a trilateral relationship, B's reciprocal
  section must link back to A. Asymmetric links are lint errors.
- Internal links: all `[[...]]` wikilinks resolve to an existing wiki page
- Log entries: `wiki/log.md` has been updated since the last ingest
- Source files exist: every `source_paths` entry corresponds to a real file in `raw/`

Full lint rules are in `lint/lint_checks.md`.

---

## 5. Page-Type Anatomies

Templates live in `templates/`. Use them when creating pages. The anatomy below is
normative; the templates are the implementation. If there is a conflict, this section wins.

Page types: `etom-l2`, `sid-abe`, `oda-component`, `foundation`, `view`.

### 5.1 eTOM L2 Page

**File location:** `wiki/etom/{service-domain|resource-domain|...}/{kebab-case-l2-name}.md`

eTOM domain subdirectories beyond `service-domain/` and `resource-domain/` are created at
ingest time using the verbatim naming from GB921.

**Granularity:** One page per L2 process group. L3 processes are listed within the L2 page,
not given separate pages, in v1.

**Required sections (in this order):**

```
# {L2 Process Name}        ← exact name from GB921, verbatim

## Overview
{One paragraph maximum. What the process group does, in the words of the spec.
 Cite the source section. No synthesis.}

## L3 Processes
{Bulleted list of all L3 processes under this L2, verbatim names and IDs from GB921.
 If the source does not list L3 processes, say so; do not infer.}

## SID Entities Manipulated
{Wikilinks to SID ABE entity pages. If not determinable from raw source: file open question,
 write "See open-questions.md — OQ-{NNN}"}

## ODA Components That Realise This Process
{Wikilinks to ODA component pages. If not determinable from raw source: file open question,
 write "See open-questions.md — OQ-{NNN}"}

## Open Questions
{Local open questions specific to this page. Short-form; full text in open-questions.md.}
```

### 5.2 SID ABE Page

**File location:** One file per ABE, organised by category:
- `wiki/sid/product/{kebab-case-abe-name}.md` (ABEs under Product)
- `wiki/sid/service/{kebab-case-abe-name}.md` (ABEs under Service)
- `wiki/sid/resource/{kebab-case-abe-name}.md` (ABEs under Resource)
- `wiki/sid/common/{kebab-case-abe-name}.md` (ABEs under Common Business Entities)

**Granularity (v1 decision, 2026-05-08).** One wiki page per top-level ABE (the chapter-level
ABE in GB922). Constituent Business Entities (BEs) and nested sub-ABEs become sub-sections
within the ABE page. Anchored wikilinks resolve specific BEs and sub-ABEs:
`[[wiki/sid/product/product-specification-abe#AtomicProductSpecification]]`. Per-BE pages
were considered but rejected for v1 — Product alone has 100+ BEs across 12 ABEs; per-BE
granularity would mean hundreds of pages and is over-engineered for the current goal.
Future v2 may split into per-BE pages if mapping work demands finer granularity.

The four category landing pages (`wiki/sid/product-abe.md`, `wiki/sid/service-abe.md`,
`wiki/sid/resource-abe.md`, `wiki/sid/common-abe.md`) act as indices that list and link the
ABEs in their category; they do not themselves carry normative content for individual
ABEs.

**Required sections (in this order, for entity pages):**

```
# {Entity Name}            ← exact name from GB922, verbatim

## Overview
{What this entity represents. Verbatim or very close to source. Cite section.}

## Key Attributes
{Table or bulleted list of key attributes with types, verbatim from GB922.
 Do not omit or rename attributes. If the source is ambiguous, note it.}

## Relationships
{Key associations to other ABE entities, as stated in the source. Verbatim names.
 Use wikilinks where target entity pages exist.}

## ODA Components That Own This Entity
{Wikilinks to ODA component pages that hold authoritative ownership of this entity.
 If not determinable: file open question.}

## eTOM Processes That Manipulate This Entity
{Wikilinks to eTOM L2 wiki pages. If not determinable: file open question.}

## Open Questions
{Local open questions specific to this page.}
```

### 5.3 ODA Component Page

**File location:** `wiki/oda/{kebab-case-domain}/{kebab-case-component-name}.md`

ODA domain subdirectories are created at ingest time using the verbatim domain naming from
the source. Domain landing pages (`wiki/oda/{domain}/_index.md`) act as indices.

**Granularity:** One page per ODA component.

**Required sections (in this order):**

```
# {Component Name}         ← exact name from source, verbatim

## Overview
{Purpose and scope of the component. Cite source. Verbatim where normative.}

## Responsibilities
{Functional responsibilities — what the component does. Bulleted list of capabilities,
 verbatim where stated in the source.}

## SID Entities Owned
{Wikilinks to SID ABE entity pages this component is the authoritative owner of.
 If not determinable from raw source: "See open-questions.md — OQ-{NNN}".}

## eTOM Processes Realised
{Wikilinks to eTOM L2 wiki pages whose processes this component implements.
 If not determinable: "See open-questions.md — OQ-{NNN}".}

## Component Dependencies
{Wikilinks to other ODA component pages this component depends on or interacts with.
 Within-ODA navigational; not subject to trilateral linting. Verbatim where the source
 establishes the dependency; otherwise leave empty rather than infer.}

## Open Questions
{Local open questions specific to this page.}
```

### 5.4 Foundation Page

**File location:** `wiki/foundations/{kebab-name}.md`

Foundation pages capture cross-framework concepts, definitions, and principles from
documents like GB991 (Core Frameworks Concepts and Principles). They sit "above" the
trilateral linking pattern — other corpus pages (eTOM, SID, ODA) link *to* foundation
pages when invoking a defined concept.

**Granularity:** One page per topical area (e.g. `domains.md` covers all 11 horizontal
domains as H3 sub-sections). Anchored wikilinks resolve specific concepts:
`[[wiki/foundations/domains#Customer Domain]]`.

**Required sections (in this order):**

```
# {Page Title}

## Overview
{Brief introduction; cite source section.}

## {variable body H2s}
{Per-concept H3 sub-sections with verbatim definitions/statements/principles.
 The middle of the page is unconstrained — match the structure of the source content.}

## Cross-Framework Application
{Wikilinks to eTOM, SID, ODA pages that reference the concepts on this page.
 Empty initially; populated as cross-framework pages are ingested.}

## Open Questions
{Local open questions specific to this page.}
```

**Trilateral linking:** Foundation pages are exempt from trilateral linking. The
"Cross-Framework Application" section is informational only and not subject to
bidirectional lint enforcement; it accumulates wikilinks over time as other layers
are ingested.

### 5.5 View Page

**File location:** `wiki/views/{kebab-case-view-name}.md`

Views are practitioner cross-cuts. They are **derivative**: they cite and link authoritative
pages but do not themselves constitute authority. They must not introduce new facts. They
are exempt from trilateral linking; instead they require a `Source Pages` section.

**Required sections (in this order):**

```
# {View Title}

> **Derivative page.** This view synthesises content from authoritative wiki pages.
> It does not add new TMF facts. For normative claims, follow the links to source pages.

## Purpose
{What question or use case this view addresses.}

## {View-specific sections}
{Whatever structure serves the view's purpose. All facts must link to authoritative pages.}

## Source Pages
{Explicit list of all wiki pages this view draws on, as wikilinks.}
```

---

## 6. Frontmatter Schema

All wiki pages must have a YAML frontmatter block. Required fields vary by page type.

### Common fields (all types except `view`)

```yaml
---
type: etom-l2          # one of: etom-l2 | sid-abe | oda-component | foundation | view
spec_id: GB921         # primary spec ID
spec_version: "22.5"   # string; the version as printed in the document
retrieval_date: 2026-05-08    # ISO 8601; date the raw file was obtained
source_paths:                  # list of raw files this page is derived from
  - raw/tmf/etom/GB921-eTOM-v22.5.pdf
source_extract_paths:          # list of extracted markdown working copies (parallel to source_paths)
  - raw/extracted/tmf/etom/GB921-eTOM-v22.5.md
authority: primary             # primary | adjacent. Default: primary if omitted.
release_status: production     # OPTIONAL: production | pre-production | draft
                               # Records the source document's stated Release Status verbatim.
                               # Default if omitted: production. Set explicitly to pre-production
                               # or draft when the source PDF reports anything other than
                               # "Release Status: Production". Required to be honest about
                               # provenance; informs how confident downstream readers can be.
---
```

### Additional fields by type

**etom-l2:**
```yaml
l1_parent: "1.4 Resource Domain"   # L1 name and ID, verbatim from GB921
l2_id: "1.4.2"                     # L2 process ID, verbatim
l2_name: "Resource Provisioning"   # L2 process name, verbatim
```

**sid-abe (entity page):**
```yaml
abe_category: service              # one of: product | service | resource | common
entity_name: "CustomerFacingService"   # verbatim entity name from GB922
```

**oda-component:**
```yaml
oda_domain: ""           # ODA functional domain, verbatim from source
component_id: ""         # canonical component identifier from source
component_name: ""       # verbatim component name
psr_layer: ""            # OPTIONAL: product | service | resource | cross-cutting | unspecified
                         # Populate only if the source explicitly classifies the component.
                         # Do not infer.
```

**foundation:**
```yaml
concept_category: ""     # domain | lifecycle | framework | principle | meta
title: ""                # page title verbatim (matches the H1)
```

**view:**
```yaml
derived_from:                       # list of authoritative wiki pages this view draws on
  - wiki/etom/service-domain/service-configuration-activation.md
  - wiki/oda/{domain}/{component}.md
# spec_id, spec_version, retrieval_date, source_paths, source_extract_paths are NOT required
# for view pages; views inherit authority from their source pages.
```

### Adjacent sources

Add `authority: adjacent` and use `spec_id`/`spec_version` appropriate to the adjacent
standard. These pages must not override TMF primary claims.

---

## 7. Trilateral Linking

Every page in the authoritative corpus that is `etom-l2`, `sid-abe`, or `oda-component`
must satisfy all applicable link directions below. Failure to satisfy a direction is a lint
error unless a corresponding open question is filed.

`foundation` and `view` pages are exempt (foundation pages sit above the trilateral;
view pages have their own `Source Pages` requirement).

| Page type     | Must link to |
|---------------|-------------|
| etom-l2       | SID entities manipulated + ODA components that realise |
| sid-abe       | ODA components that own + eTOM processes that manipulate |
| oda-component | SID entities owned + eTOM processes realised |

The "Component Dependencies" section on `oda-component` pages is **not** a trilateral
section. It is within-ODA navigation; the linter does not enforce content there.

### Bidirectional consistency
If `wiki/oda/{domain}/customer-order-management.md` lists
`[[wiki/sid/product/customer-order]]` under "SID Entities Owned", then
`wiki/sid/product/customer-order.md` MUST list
`[[wiki/oda/{domain}/customer-order-management]]` under "ODA Components That Own This
Entity". The linter checks both directions. Adding a link in one direction without the
reciprocal is a lint error.

### When a link cannot be determined from raw source
1. Do NOT guess or infer.
2. File an open question in `wiki/open-questions.md` (§8).
3. In the relevant page section, write either:
   - Plain text: `See open-questions.md — OQ-{NNN}`, or
   - Wikilink (preferred for Obsidian navigation): `See [[wiki/open-questions#OQ-{NNN}]]`
   where NNN is the question number assigned in open-questions.md.
4. The linter accepts either format as satisfying the link requirement for that direction.
   Wikilinks to exempt pages (`wiki/index.md`, `wiki/log.md`, `wiki/open-questions.md`,
   the SID category landings, and any `_index.md`) are skipped by the bidirectional
   check — these pages have no anatomy and cannot host reciprocal sections.

### Version mismatches
Where one document references obsolete IDs from another:
- Resolve to the current ID in the wiki page.
- Note the original reference: "Original spec references {old-id}; resolved to {current-id}."
- If the resolution is uncertain, file an open question instead.

---

## 8. Open-Questions Discipline

`wiki/open-questions.md` is the escalation point for all ambiguities. The agent MUST NOT
resolve ambiguities by inference; it MUST file them here.

### When to file
- A required trilateral link cannot be determined from raw source.
- A cross-reference is ambiguous or inconsistent between sources.
- A version mismatch cannot be resolved with certainty.
- An adjacent source contradicts a primary source.
- A raw source contains a defect (typo, broken extraction, missing section).
- Any normative claim is unclear or absent from the raw source.

### Format (free-form for v1, but each entry must include)

```
## OQ-{NNN} — {Brief title}

- **Raised:** {date}
- **Source page:** {wiki page path that raised the question}
- **Question:** {What is unclear or missing?}
- **Blocking:** {What cannot proceed until this is resolved?}
```

### Closing an open question
Only closed by user direction. When closed, append a `**Resolved:**` line with the
resolution and date. Do not delete the entry; resolved questions remain for audit.

---

## 9. Maintenance Obligations

### `wiki/index.md`
Updated after every ingest. Structure: one section per top-level category (eTOM Service
Domain, eTOM Resource Domain, eTOM Product-related, SID Product, SID Service, SID Resource,
SID Common, ODA, Views), each listing pages with a one-line description. The index is the
entry point for human readers in Obsidian; keep it current and accurate.

### `_index.md` files per directory
Each subdirectory has an `_index.md` summarising the directory's contents and linking the
pages within. Updated when pages are added or removed.

### `wiki/log.md`
Append-only. Never edit existing entries. Each entry records:

```
## {ISO 8601 datetime} — {INGEST | LINT | OPEN-QUESTION | RESOLVED}

- **File(s):** {raw files ingested, or "N/A" for lint runs}
- **Pages created/updated:** {list}
- **Sections skipped (out of scope):** {section refs and reasons, or "none"}
- **Lint result:** {PASS | FAIL — {N} errors}
- **Open questions filed:** {list of OQ-NNN, or "none"}
- **Notes:** {anything notable, including extraction warnings}
```

---

## 10. Forbidden Actions

The following are explicitly forbidden regardless of user request. If asked to do one,
explain why it violates the constitution and propose a compliant alternative.

1. **Training-data recall** — stating any TMF fact not present in raw/ or wiki/.
2. **Fabricating cross-references** — linking pages when the source doesn't establish the
   link.
3. **Paraphrasing normative terms** — canonical names, IDs, attributes must be verbatim.
4. **Touching `project/` — security boundary.** The `project/` folder exists for the user
   to populate manually with current-state company data. The agent must NEVER read, write,
   create, modify, or otherwise interact with files under `project/`. Reading project/
   would introduce company data into the LLM context, which the user has explicitly
   disallowed. This is not a deferral — it is a permanent boundary.
5. **Resolving open questions autonomously** — only the user closes open questions.
6. **Editing `wiki/log.md` existing entries** — it is append-only.
7. **Creating wiki pages without a corresponding raw source file** — no source, no page.
   (Exception: `view` pages, which derive from existing wiki pages.)
8. **Skipping lint after ingest** — lint is mandatory, not optional.
9. **Modifying `raw/`** — primary source files are immutable. The agent's only legitimate
   write target inside `raw/` is `raw/extracted/`.
10. **Ingesting pre-release/draft spec versions without explicit user confirmation.**
11. **Hand-editing files in `raw/extracted/`** — they are regenerated, not edited.

---

## 11. Directory Quick Reference

```
tmf-kb/
├── CLAUDE.md                    ← this file; the constitution
├── raw/
│   ├── tmf/                     ← primary authority; user populates with PDFs
│   │   ├── etom/                ← GB921 + addenda
│   │   ├── sid/                 ← GB922
│   │   └── oda/                 ← ODA Functional Architecture, component documents
│   ├── tmf-adjacent/            ← secondary authority; initially empty
│   └── extracted/               ← markdown extractions, mirroring raw/{tmf,tmf-adjacent}
│       ├── tmf/
│       │   ├── etom/
│       │   ├── sid/
│       │   └── oda/
│       └── tmf-adjacent/
├── wiki/
│   ├── index.md                 ← top-level catalog, updated after every ingest
│   ├── log.md                   ← append-only event log
│   ├── open-questions.md        ← ambiguity escalation log
│   ├── etom/
│   │   ├── _index.md
│   │   ├── service-domain/
│   │   │   ├── _index.md
│   │   │   └── {l2-process}.md
│   │   ├── resource-domain/
│   │   │   ├── _index.md
│   │   │   └── {l2-process}.md
│   │   └── {product-related-domain}/   ← created at ingest from GB921 verbatim naming
│   │       ├── _index.md
│   │       └── {l2-process}.md
│   ├── sid/
│   │   ├── _index.md
│   │   ├── product-abe.md       ← Product ABE category landing
│   │   ├── service-abe.md       ← Service ABE category landing
│   │   ├── resource-abe.md      ← Resource ABE category landing
│   │   ├── common-abe.md        ← Common Business Entities category landing
│   │   ├── product/
│   │   │   ├── _index.md
│   │   │   └── {entity}.md      ← one per Product ABE entity
│   │   ├── service/
│   │   │   ├── _index.md
│   │   │   └── {entity}.md
│   │   ├── resource/
│   │   │   ├── _index.md
│   │   │   └── {entity}.md
│   │   └── common/
│   │       ├── _index.md
│   │       └── {entity}.md
│   ├── oda/
│   │   ├── _index.md
│   │   └── {domain}/            ← domain subdirectories created at ingest
│   │       ├── _index.md
│   │       └── {component}.md   ← one per ODA component
│   ├── foundations/             ← cross-framework concepts and principles (GB991)
│   │   ├── _index.md
│   │   └── {topic}.md           ← e.g. domains, lifecycle, principles
│   └── views/
│       └── _index.md
├── lint/
│   ├── lint.py                  ← deterministic linter
│   └── lint_checks.md           ← lint rules in prose
├── templates/                   ← page templates, one per page type
└── project/                     ← SECURITY BOUNDARY — agent must not touch.
                                    Reserved for user-only manual population.
```

---

## 12. Working Style

When interacting with the user about ingest, open questions, or schema decisions:

- Be direct. State conclusions before reasoning, not after.
- When uncertain, say so explicitly and ask. Do not present false confidence.
- When making a recommendation, give the recommendation and the reasoning — not a menu of
  options without a lean.
- Push back when the user is wrong. Acknowledge when the user is right and a previous
  position is mistaken.
- Prefer getting decisions made over hedging. If a deferred decision is blocking, surface
  it.

This style applies to every agent message — ingest summaries, open-question reports, lint
failure reports, and queries.

---

## 13. Obsidian Conventions

The wiki is read in Obsidian. Adopt Obsidian's conventions so the graph view, backlinks,
and navigation work cleanly:

- **Wikilinks for all inter-wiki references.** Use `[[wiki/path/to/page]]` (without `.md`
  extension). Obsidian resolves these and surfaces backlinks automatically.
- **Frontmatter is YAML.** Obsidian respects YAML frontmatter (§6); do not use alternative
  formats.
- **Avoid `#tags`.** Frontmatter `type:` and `spec_id:` already provide categorisation.
- **External links use standard markdown.** `[label](https://...)`. Wikilinks are wiki-only.
- **File names are kebab-case.** Lowercase, hyphen-separated. Page titles inside the
  document use the canonical TMF name verbatim.
