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
entity_name: "Service Strategy & Plan ABE"
---

# Service Strategy & Plan ABE «notFullyDeveloped»

> **Status flag.** GB922 Service v25.0 §4.12 explicitly tags this ABE as
> «notFullyDeveloped». Additionally, this ABE sits in the Strategy-to-Readiness
> lifecycle area, which is partially out of scope for the operational mapping focus
> of this corpus. See [[wiki/open-questions#OQ-025]].

## Overview

The Service Strategy and Plan ABE contains entities that are used to address the need
for enhanced or new Services, as well as the retirement of existing Services, by the
enterprise. These entities have a strong dependency to both entities in the Resource
and Product domains. Resulting efforts, such as deciding what Resources to use to
host a Service, or what Services are used to support new Product Specifications, are
also supported, as are service demand forecasts. — GB922 Service §4.12, p. 152

## Business Entities

No specific entities are enumerated in the §4.12 overview. The ABE is in development.

## Key Attributes

Not specified in source.

## Relationships

- Implied dependencies on Product domain
  ([[wiki/sid/product/product-specification-abe]]).
- Implied dependencies on Resource domain (not yet ingested).
- Service demand forecasts conceptually link to
  [[wiki/sid/service/service-capacity-abe]].

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-025: Service Strategy & Plan ABE source-tagged «notFullyDeveloped»;
  Strategy-to-Readiness lifecycle area is partially out of scope per CLAUDE.md §3
