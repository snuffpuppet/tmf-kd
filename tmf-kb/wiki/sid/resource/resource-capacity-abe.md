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
entity_name: "Resource Capacity ABE"
---

# Resource Capacity ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Capacity ABE specifies the ability of Resource to provide capability
measured in quantity and units of quantity over an extended period. It also manages
the Resource Capacity Demands. — GB922 Resource §4.10, p. 503

Figure RC.01 in this ABE is explicitly "Copy from Capacity ABE in Common Domain"
(CM.02). The canonical Capacity model lives in [[wiki/sid/common/capacity-abe]];
Resource Capacity specialises it for Resources.

## Business Entities

This ABE applies the canonical Capacity pattern from
[[wiki/sid/common/capacity-abe]] to Resource entities:

- **ResourceCapacity** — resource-specific capacity
- **ResourceCapacitySpec** — specification side
- **ResourceCapacityDemand** — resource-specific demand

Common entities (`Capacity`, `CapacityAmount`, `CapacityDemand`, `AppliedCapacityDemand`,
`CapacityRelationship`, `ApplicableTimePeriod`) inherited from
[[wiki/sid/common/capacity-abe]].

## Key Attributes

`CapacityAmount.amount` (Quantity), `units`, `capacityAmountFrom`, `capacityAmountTo`,
`rangeInterval`, `plannedOrActutalCapacity` (sic — see open-questions.md OQ-010).

## Relationships

- Specialises [[wiki/sid/common/capacity-abe]] for Resource.
- Parallel to [[wiki/sid/product/product-capacity-abe]] and
  [[wiki/sid/service/service-capacity-abe]].
- ResourceCapacity relates to Resource instances ([[wiki/sid/resource/resource-abe]]).
- Uses GeographicPlace ([[wiki/sid/common/location-abe]]) for geographic capacity.
— GB922 Resource §4.10

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-010: Source typo `plannedOrActutalCapacity` (sic) preserved verbatim
- OQ-027: Pre-production source release status
