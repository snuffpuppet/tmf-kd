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
entity_name: "Service Capacity ABE"
---

# Service Capacity ABE

## Overview

The Service Capacity ABE specifies ability of Service to provide capability measured
in quantity and units of quantity over an extended period. It also manages the Service
Capacity Demands. — GB922 Service §4.10, p. 144

Figures SC.01–SC.03 in this ABE are explicitly "Copy from Capacity ABE in Common
Domain" (CM.02, CM.06, CM.09). The canonical Capacity model lives in
[[wiki/sid/common/capacity-abe]]; Service Capacity specialises it for Service.

## Business Entities

This ABE applies the canonical Capacity pattern from
[[wiki/sid/common/capacity-abe]] to Service entities:

- **ServiceCapacity** — service-specific capacity
- **ServiceCapacitySpec** — specification side
- **ServiceCapacityDemand** — service-specific capacity demand

Common entities (Capacity, CapacityAmount, CapacityDemand, AppliedCapacityDemand,
CapacityRelationship, ApplicableTimePeriod) inherited from
[[wiki/sid/common/capacity-abe]].

## Key Attributes

`CapacityAmount.amount` (Quantity), `units`, `capacityAmountFrom`, `capacityAmountTo`,
`rangeInterval`, `plannedOrActutalCapacity` (sic — see open-questions.md OQ-010).
Detailed Service-specific attributes not extracted in v1 ingest.

## Relationships

- Specialises [[wiki/sid/common/capacity-abe]] for Service.
- Parallel to [[wiki/sid/product/product-capacity-abe]] and Resource Capacity ABE
  (Resource Domain — not yet ingested).
- ServiceCapacity relates to Service instances
  ([[wiki/sid/service/service-abe]]).
- Uses GeographicPlace ([[wiki/sid/common/location-abe]]) for geographic capacity.
- Uses ApplicableTimePeriod (defined in
  [[wiki/sid/common/capacity-abe]]).
— GB922 Service §4.10, pp. 144–149

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

- [[wiki/etom/service-domain/service-capacity-management]] — primary ongoing-management
  manipulator. The L2 is dedicated end-to-end to service capacity (plan, align, gap-
  analyse, forecast, implement, analyse, optimize, monitor, report). The Service
  Capacity ABE is the data model. Reciprocal back-link from the L2's `## SID Entities
  Manipulated` section, ingested 2026-05-10 under Phase 3 Capability Management batch
  (Capacity Management PSR pair). **Note:** this L2 is net-new in v25.5 (Original PID
  = None).
- [[wiki/etom/service-domain/service-capability-delivery]] — upstream-input manipulator.
  L3 1.4.2.1 establishes detailed views of anticipated service demand and performance
  requirements; L3 1.4.2.2 (specifically L4 1.4.2.2.1) captures service capacity
  shortfalls. The Service Capacity ABE is the data side of the capacity-requirements
  and capacity-shortfalls artefacts. Reciprocal back-link from the L2's `## SID
  Entities Manipulated` section, ingested 2026-05-10 under Phase 3 Capability
  Management batch (Capability Delivery PSR pair).

See open-questions.md — OQ-008 (further eTOM/ODA links pending broader trilateral
sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-010: Source typo `plannedOrActutalCapacity` (sic) preserved verbatim
