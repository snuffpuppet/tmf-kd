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
entity_name: "Capacity ABE"
---

# Capacity ABE

## Overview

A generalized ABE and specializations that provide capacity and capacity demand for
products, services, and resources. — GB922 Common §4.16, p. 474

Capacity is the ability to provide some capability. For example, one measure of
network capacity is the ability of a network to provide a certain amount of bandwidth
during the month of May. — GB922 Common §4.16, p. 474

### Capacity and the Business Process Framework (eTOM)

A number of eTOM Level 3 process elements were used as the basis for some of the
requirements satisfied by this model. They include the L3 processes, Produce Product
Portfolio Business Plans, Produce Service Business Plans, and Produce Resource
Business Plans, with L1 Strategy processes. And, the L3 processes, Enable Service
Configuration & Activation and Enable Resource Provisioning, within the L1 Operations
Support & Readiness processes. — GB922 Common §4.16, p. 474

## Business Entities

This is the **canonical** Capacity ABE that
[[wiki/sid/product/product-capacity-abe]] specialises for Product. Per the source
notation in Product (§4.10), Figure PC.01 is a "copy from CM.02 from Capacity ABE in
Common Domain".

Core entities include:

- **Capacity** — generalised capacity
- **CapacityAmount** — the quantity (datatype `Quantity`)
- **CapacityDemand** — demands placed on a CapacityAmount
- **AppliedCapacityDemand** — applied portion of demand
- **CapacityRelationship** — planned↔actual or aggregated relationships
- **ApplicableTimePeriod** — temporal scope (composite of from/to + rangeInterval +
  daysOfWeek)
- **CapacitySpec** / specification side of EntitySpec/Entity pattern

Service Capacity, Resource Capacity, and Product Capacity ABEs (in their respective
domain documents) specialise this model.

§4.16 spans pp. 474–489 (16 pages); full inventory and figures CM.01 onwards in
source.

## Key Attributes

`CapacityAmount.amount` (Quantity), `units`, `capacityAmountFrom`, `capacityAmountTo`,
`rangeInterval`, `plannedOrActutalCapacity` (sic — see
[[wiki/open-questions#OQ-010]]). `CapacityDemand.priority`. Detailed attribute tables
not extracted in v1; consult source.

## Relationships

- Specialised by Product Capacity ([[wiki/sid/product/product-capacity-abe]]),
  Service Capacity (Service Domain — not yet ingested), Resource Capacity (Resource
  Domain — not yet ingested).
- Relates to GeographicPlace from [[wiki/sid/common/location-abe]] for geographic
  capacity demands.
- Relates to ApplicableTimePeriod (defined in this ABE; uses
  [[wiki/sid/common/base-types-abe]] TimePeriod where appropriate).
— GB922 Common §4.16, pp. 474–489

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-010: Source typo `plannedOrActutalCapacity` (sic) preserved verbatim
