---
type: sid-abe
spec_id: GB922
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Product_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Product_v25.5.md
authority: primary
abe_category: product
entity_name: "Product Capacity ABE"
---

# Product Capacity ABE

## Overview

Product Capacity ABE represents specific ability of Products measured in quantity and
units of quantity over an extended period. — GB922 Product §4.10, p. 248

> The ability to deliver 10000 units of Product described in the previous example is
> expressed via the CapacityAmount, whose datatype is Quantity. Quantity is a composite
> of an amount attribute and a units (unit of measure) attribute. For this instance of
> Capacity, the capacityAmount attribute contains the amount "10000", and the unit of
> measure "units". Other examples of units of measure could be transaction volumes,
> storage requirements, traffic volumes, port availabilities, and so forth.
> — GB922 Product §4.10, p. 248

The capacity model is generalised in the Common Domain Capacity ABE; Product Capacity
specialises it for Products. (Common Domain SID not yet ingested.)
— GB922 Product §4.10, p. 248 (Figure PC.01 reference: "copy from CM.02 from Capacity
ABE in Common Domain")

## Business Entities

### Capacity

Generalised capacity entity. — GB922 Product §4.10, p. 248

### CapacityAmount

Datatype `Quantity` (composite of `amount` and `units`). Has `capacityAmountFrom`,
`capacityAmountTo`, and `rangeInterval` to express ranges. The
`plannedOrActutalCapacity` attribute (sic — verbatim) indicates planned vs actual.
— GB922 Product §4.10, p. 248

### CapacityDemand

Represents a demand placed on a CapacityAmount over a defined timeframe (via
ApplicableTimePeriod). Has a `priority` attribute defining relative importance.
— GB922 Product §4.10, p. 248

### AppliedCapacityDemand

The amount of CapacityDemand that has been applied against a CapacityAmount.
— GB922 Product §4.10, p. 248

### CapacityRelationship

Enables planned Capacity to be associated with actual Capacity, or for Capacities to be
aggregated. — GB922 Product §4.10, p. 248

### ApplicableTimePeriod

Composite of `from` and `to` dates/times plus `rangeInterval` for handling
combinations of >, <, >=, <=. Refinements include `daysOfWeek`.
— GB922 Product §4.10, p. 248

## Key Attributes

See Business Entities above. Detailed attribute tables not extracted in v1 ingest;
consult source. The Capacity model is generalised in Common Domain — refer to that
guide for the full pattern.

## Relationships

- Geographic constraints expressed via relationship to GeographicPlace (Common Domain,
  not yet ingested).
- Capacity model is shared across Product, Service, Resource — Service and Resource
  Capacity ABEs (not yet ingested).
- CapacityDemand may have its own ApplicableTimePeriod, distinct from the Capacity's,
  enabling multiple demands against a single CapacityAmount.
— GB922 Product §4.10, pp. 248–252

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-010: Verbatim source attribute name `plannedOrActutalCapacity` (sic — appears to
  be a misspelling of `plannedOrActualCapacity`)
