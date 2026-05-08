---
type: sid-abe
spec_id: GB922
spec_version: "23.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Common_v23.0.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Common_v23.0.md
authority: primary
abe_category: common
entity_name: "Closed Loop ABE"
release_status: draft
---

# Closed Loop ABE

> **Source-flagged «Preliminary».** GB922 Common v23.0 §4.27 carries the «Preliminary»
> annotation in its chapter heading. `release_status: draft` set in frontmatter per
> CLAUDE.md §6. Treat content as honest-but-evolving.

## Overview

Closedloop is a "management framework" in which current outcomes are used to
improve future outcomes in order to achieve specified goals. The management
framework includes the feedforward workflow and a feedback workflow, where the
feedforward is a control loop meant to continually optimize and improve.

There can be different management frameworks, referred to in this model as
"closedloop models". Optimized versions of closedloop management frameworks may be
derived for specific scenarios. Closedloop can be typified as fast or slow and can
work hierarchically or as peers or both, based on implementation choices.

For more information please refer to IG1219.
— GB922 Common §4.27, p. 871

## Key Attributes

Source §4.27.1 (Figure CL.01 — Basic Closed Loop) defines:

- **ClosedLoop** — derived from `RootEntity → Entity → ManagedEntity`. A
  ClosedLoop can have a goal or multiple goals.
- **ClosedLoopSpecification** — derived from `RootEntity → EntitySpecification`;
  elaborates the scope of application of a ClosedLoop. The scope can be on any
  other entity, such as Product, Service, Resource, Customer, Partner based
  operations.

Source §4.27.2 (Figure CL.02 — Closed Loop SID Pattern) shows ClosedLoops
associated to workflows: typically more than one workflow makes up a ClosedLoop,
in that a ClosedLoop will require a control workflow (controlflow — responsible
for learning, analysis, decision-making) and a feedback workflow.

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.27.1–§4.27.2, pp. 871–872

## Relationships

- **ClosedLoop ↔ ClosedLoopSpecification** via `SpecifiesClosedLoop`
- **ClosedLoop ↔ Goal** (one or many Goals per ClosedLoop) — see
  [[wiki/sid/common/goal-abe]]
- **ClosedLoop ↔ Workflow** (control workflow + feedback workflow) — see
  [[wiki/sid/common/workflow-abe]]
- **ClosedLoop ↔ AnomalySpecification** — Anomaly is managed using a ClosedLoop
  defined by ClosedLoopSpecification; see [[wiki/sid/common/anomaly-abe]]
- ClosedLoop derives from `RootEntity` and `ManagedEntity` from
  [[wiki/sid/common/root-business-entities-abe]]
— GB922 Common §4.27, pp. 871–872

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Closed Loop ABE not directly mapped in any
ODA Functional Block table to date. Likely candidate for Intelligence Management
when that block's trilateral sweep runs.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Closed Loop pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Closed Loop ABE ingested as part of v1 Common gap fill; «Preliminary»
  in source
