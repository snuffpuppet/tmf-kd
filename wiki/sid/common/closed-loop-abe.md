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

- [[wiki/etom/service-domain/service-anomaly-lifecycle-management]] — **1.4.17 Service Anomaly Lifecycle Management** (BVD vertical). Every L3 in the L2 explicitly references "Closed Loop" / "Anomaly Closed Loop" / "Anomaly Management Closed Loop"; L3 .2 is named *Orchestrate Service Anomaly Management Closed Loop*; L3 .3 is *Monitor*; L3 .4 is *Report* — and L3 .4's ED cites the OODA pattern (Observe / Orient / Decide / Act) verbatim as the conceptual closed-loop model. **First eTOM trilateral link populated on this ABE; replaces the OQ-008 deferral as primary forward link.** Note: the ABE itself is `release_status: draft` («Preliminary»); the eTOM-side process treatment is more developed than the SID-side data treatment in this area as of v25.5.
- [[wiki/etom/resource-domain/resource-anomaly-lifecycle-management]] — **1.5.20 Resource Anomaly Lifecycle Management** (BVD vertical). PSR-symmetric with Service-side back-link above; same closed-loop-orchestration / monitoring / reporting pattern across L3s.

> **Phase-4 candidate manipulators.** Beyond the two BVD-side Anomaly Lifecycle L2s above, ClosedLoop is plausibly manipulated by the Operations-side Anomaly Management L2s (Service Anomaly Management 1.4.18 + Resource Anomaly Management 1.5.21 — both in `wiki/etom/{service,resource}-domain/`). Both reference closed-loop-related activities through their decompositions but neither has its `## SID Entities Manipulated` populated yet (deferred to OQ-008). Closed Loop is also the candidate ABE for Intelligence Management functional-block trilateral when ODA layer ingests further. Tight-scope decision at the 2026-05-12 Anomaly Lifecycle PSR pair ingest deferred those broader trilateral fills. Wikilinks intentionally omitted here per the convention of no wikilinks in trilateral sections beyond the primary forward-link bullet targets.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Closed Loop ABE ingested as part of v1 Common gap fill; «Preliminary»
  in source
