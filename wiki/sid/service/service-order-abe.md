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
entity_name: "Service Order ABE"
---

# Service Order ABE

## Overview

The Service Order ABE contains all entities that represent a type of Request of one
or several services for any type of Service Specification. A Service Order decomposes
a Product Order's products into the services associated with a ServiceOrder through
which the products are realized. — GB922 Service §4.6, p. 113

## Business Entities

### ServiceOrder

A request to procure, update, or remove one or more Services. Decomposes a ProductOrder
into the Services that realise the Products. Sub-class of `BusinessInteraction`
([[wiki/sid/common/business-interaction-abe]]).
— GB922 Service §4.6, p. 113 (Figure SOr.01)

### ServiceOrderItem

Order item at the service level — paralleling
[[wiki/sid/product/product-order-abe]] ProductOrderItem.
— GB922 Service §4.6 (Figure SOr.03)

For full inventory and figures SOr.01–SOr.03 see source.

## Key Attributes

ServiceOrder inherits from BusinessInteraction; detailed attribute tables not
extracted in v1 ingest.

## Relationships

- ServiceOrder decomposes [[wiki/sid/product/product-order-abe]] ProductOrder into
  Services.
- ServiceOrder is a sub-class of BusinessInteraction
  ([[wiki/sid/common/business-interaction-abe]]).
- Inherits relationships from BusinessInteraction (Figures SOr.02, SOr.03).
- References [[wiki/sid/service/service-abe]] entities being ordered.
— GB922 Service §4.6, pp. 113–116

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
