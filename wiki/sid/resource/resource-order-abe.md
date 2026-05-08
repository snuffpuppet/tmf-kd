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
entity_name: "Resource Order ABE"
---

# Resource Order ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Order ABE contains entities related to a request to provide / update /
remove Resources. — GB922 Resource §4.5, p. 332

## Business Entities

### ResourceOrder

A request to provide, update, or remove Resources. Sub-class of `BusinessInteraction`
([[wiki/sid/common/business-interaction-abe]]) following the same pattern as
ProductOrder ([[wiki/sid/product/product-order-abe]]) and ServiceOrder
([[wiki/sid/service/service-order-abe]]).
— GB922 Resource §4.5 (Figure RO.01)

### ResourceOrderItem

Order item at the resource level — paralleling Service/Product Order items.
— GB922 Resource §4.5

For full inventory and the EntitySpecification/Entity pattern usage, consult source.

## Key Attributes

ResourceOrder inherits from BusinessInteraction; detailed attribute tables not
extracted in v1 ingest.

## Relationships

- ResourceOrder follows the order decomposition chain:
  ProductOrder → [[wiki/sid/service/service-order-abe]] → ResourceOrder.
- Sub-class of BusinessInteraction ([[wiki/sid/common/business-interaction-abe]]).
- References [[wiki/sid/resource/resource-abe]] entities being ordered.

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status
