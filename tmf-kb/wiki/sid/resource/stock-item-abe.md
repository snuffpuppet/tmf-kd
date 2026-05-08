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
entity_name: "Stock Item ABE"
---

# Stock Item ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Stock Item ABE covers all information needed by the supply chain.
— GB922 Resource §4.9, p. 354

It includes:

- The Stock Item catalogue
- The Stock Items stored in a warehouse
- The Stock Item Shipments specifying Stock Items movements (receiving or shipping)

— GB922 Resource §4.9, p. 354

## Business Entities

§4.9 spans pp. 354–502 (148 pages — second-largest single ABE in this document after
§4.3 Resource at 100 pages and §4.2 Resource Specification at 110 pages). Conceptually:

- **StockItem** — items in inventory
- **StockItemSpecification** / **StockItemCatalogue** — types of stock and their
  catalog
- **StockItemShipment** — receiving/shipping movements
- **Warehouse** entities

For full BE inventory consult source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Stock Items relate to PhysicalResources
  ([[wiki/sid/resource/resource-abe]]) — particularly equipment and tangible goods.
- Stock Item catalogue relates to canonical [[wiki/sid/common/catalog-abe]].
- Shipment movements relate to Location ([[wiki/sid/common/location-abe]]) for
  warehouse and delivery destinations.
- Stock Item Spec relates to Goods and Shipping Product Spec
  ([[wiki/sid/product/product-specification-abe]] §4.2.2 sub-ABE) — supply chain
  link to Product side.

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status
- OQ-030: Stock Item ABE is large (148 pages); v1 ingest covers conceptual content
  only. Supply chain modelling is somewhat outside the typical OSS-monolith mapping
  scope — confirm relevance for the user's PSR mapping work.
