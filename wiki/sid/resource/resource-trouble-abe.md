---
type: sid-abe
spec_id: GB922
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Resource_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Resource_v25.5.md
authority: primary
release_status: pre-production
abe_category: resource
entity_name: "Resource Trouble ABE"
---

# Resource Trouble ABE «notFullyDeveloped»

> **Status flag.** GB922 Resource v25.5 §4.11 source-tagged «notFullyDeveloped».
> Pre-production source. See [[wiki/open-questions#OQ-027]] and
> [[wiki/open-questions#OQ-031]].
>
> **Operational relevance.** Resource Trouble Management is in-scope eTOM L2 per
> CLAUDE.md §3 — the production-side fault/alarm/repair flow. SID-side incompleteness
> here parallels the same gap in [[wiki/sid/service/service-problem-abe]]
> («NotFullyDeveloped»).

## Overview

The Resource Trouble ABE collects information about problems found in allocated
resource instances, regardless of whether the problem is physical or logical.
Entities in this ABE capture detection, root cause, and resoluiton of these problems
and maintain a history of the activities involved in diagnosing and solving the
problem. This history includes tracking, reporting, assigning people to fix the
problem, testing and verification, and overall administration of repair activities.
— GB922 Resource §4.11, p. 514

> Verbatim source spelling "resoluiton" (sic — preserved per CLAUDE.md §1).

## Business Entities

§4.11 names a sub-section §4.11.1 **Alarm ABE** but content is sparse — the source
flag «notFullyDeveloped» applies. Conceptually this ABE covers:

- **ResourceProblem** / **ResourceTrouble** — fault representations
- **Alarm** — alarm signalling entities (in nested Alarm ABE)
- **TroubleTicket** — repair/diagnosis tracking entity
- Detection, root-cause, and resolution history entities

For what content exists consult source.

## Key Attributes

Not specified in §4.11 overview; consult source.

## Relationships

- Resource problems correlate to Service problems
  ([[wiki/sid/service/service-problem-abe]] — also «NotFullyDeveloped»).
- TroubleTickets are likely related to BusinessInteraction
  ([[wiki/sid/common/business-interaction-abe]]).
- Operational relevance: eTOM Resource Trouble Management L2 process group (in scope
  per CLAUDE.md §3) directly maps to this ABE.

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status
- OQ-031: Resource Trouble ABE source-tagged «notFullyDeveloped»; combined with the
  parallel Service Problem ABE incompleteness, this is a meaningful gap for
  production-side fault-management mapping work
- OQ-032: Source verbatim "resoluiton" (sic — should likely be "resolution")
