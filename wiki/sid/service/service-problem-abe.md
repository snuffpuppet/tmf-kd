---
type: sid-abe
spec_id: GB922
spec_version: "25.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Service_v25.0.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Service_v25.0.md
authority: primary
abe_category: service
entity_name: "Service Problem ABE"
---

# Service Problem ABE «NotFullyDeveloped»

> **Status flag.** GB922 Service v25.0 §4.11 explicitly tags this ABE as
> «NotFullyDeveloped». See [[wiki/open-questions#OQ-024]].

## Overview

The Service Problem ABE manages faults, alarms, and outages from a Service
point-of-view. This is then correlated to trouble tickets, regardless of whether the
cause is physical or logical. — GB922 Service §4.11, p. 150

Other entities in this ABE are used to direct the recovery from each of these types
of problems. They provide the ability to associate Resource faults and alarms to
degradation and outages of Services that run on those Resources.
— GB922 Service §4.11, p. 150

## Business Entities

§4.11 (p. 150) is brief; full BE list is in source Figure SP.01. Conceptually:

- **ServiceProblem** / **ServiceFault** / **ServiceAlarm** / **ServiceOutage**
  entities (as suggested by the chapter overview)
- **TroubleTicket** entity (referenced as the correlation target)
- **ResourceFault**, **ResourceAlarm** entities (cross-domain reference)

For full inventory consult source.

## Key Attributes

Not specified in §4.11 overview; consult source.

## Relationships

- Service Problem entities correlate to Trouble Tickets.
- Resource faults/alarms (Resource Domain — not yet ingested) associate to Service
  degradations/outages — directly relevant to the **production-side** of the
  production/commercial separation.
- Operational relevance: eTOM Service Problem Management L2 (in scope per CLAUDE.md
  §3) directly maps to this ABE.
— GB922 Service §4.11, pp. 150–151

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-024: Service Problem ABE source-tagged «NotFullyDeveloped»; content thin
