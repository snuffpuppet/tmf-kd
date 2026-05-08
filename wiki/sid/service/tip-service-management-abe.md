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
entity_name: "TIP Service Management ABE"
---

# TIP Service Management ABE «likelyToBeDepreciated»

> **Deprecation flag.** GB922 Service v25.0 §4.13 explicitly states: "This ABE is
> likely to be removed in Release 25.5". Source-tagged «likelyToBeDepreciated» (sic
> — verbatim from source; "deprecated" is the standard spelling). See
> [[wiki/open-questions#OQ-026]].

## Overview

The TMF Interface Program introduced in the Multi-Technology Operations System
Interface (MTOSI) 2.0, Service Management interfaces based upon extensions to the SID
service model in this ABE. The resulting solution set introduced two new service
management activation interfaces, and a service inventory interface.
— GB922 Service §4.13, p. 152

> Note: TMF Interface Program (aka TIP) is legacy stuff to define interfaces and
> interfaces are now defined by the Open API Program. — GB922 Service §4.13, p. 152

## Business Entities

§4.13 spans pp. 152–166. Entities relate to MTOSI 2.0 Service Management interfaces:

- Service Definition entities (Figure SO.31)
- Service Characteristics entities (Figure SO.32)
- Service Activation entities (Figure SO.33)
- CommonServiceInfo (Figure SO.33a)

For full BE inventory consult source. Given the deprecation flag, deeper ingest is
not warranted.

## Key Attributes

Not extracted in v1 ingest given pending deprecation.

## Relationships

- Legacy ABE; entities here are subsumed or replaced by current Service ABE
  ([[wiki/sid/service/service-abe]]) and Service Specification ABE
  ([[wiki/sid/service/service-specification-abe]]) constructs.
- Source notes interface definitions are now handled by the TMF Open API Program
  (out of scope for v1 corpus per CLAUDE.md §3).

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-026: TIP Service Management ABE source-tagged «likelyToBeDepreciated» — flagged
  for removal in Release 25.5. Re-evaluate inclusion when v25.5 Service is published;
  may be removed entirely from corpus then.
