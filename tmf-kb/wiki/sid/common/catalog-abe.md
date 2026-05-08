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
entity_name: "Catalog ABE"
---

# Catalog ABE

## Overview

A generalized ABE that represents common Catalog Specification and Catalog entities,
attributes, and associations shared (inherited) by components of the Entity, Federated,
Product, Service, and Resource Catalog ABEs. — GB922 Common §4.17, p. 490

The Catalog Management paragraph describes the usage of "Catalogs" to provide
consistency of catalog model definitions across the Product, Service, and Resource
domains, and to support the federation of catalogs and the ability to create a catalog
containing any entity and/or its specification.

A generalized Catalog ABE contains generic (abstract) CatalogSpecification and Catalog
entities used to define types of catalog specifications and types of catalog entities.
The patterns used to model Catalog business entities are the EntitySpecification/Entity
and the CharacteristicSpecification/CharacteristicValue patterns. It also uses
relationship entities as an alternate to the Composite/Atomic pattern. It embraces the
existing entity of 'Product Catalog ABE' definition present before this guidebook was
developed. — GB922 Common §4.17, p. 490

## Business Entities

- **Catalog** (abstract) — base catalog entity
- **CatalogSpecification** (abstract) — EntitySpec side of catalog
- **EntityCatalog**, **FederatedCatalog** — generic specialisations
- **ProductCatalog** — product-specific (also referenced by
  [[wiki/sid/product/product-offering-specification-abe]] §4.3.2 as a sub-ABE)
- **ServiceCatalog** — service-specific (Service Domain — not yet ingested)
- **ResourceCatalog** — resource-specific (Resource Domain — not yet ingested)

§4.17 spans pp. 490–506 (17 pages); full inventory and figures in source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Generalised by Product Catalog (referenced from
  [[wiki/sid/product/product-offering-specification-abe]]).
- Specialised by Service Catalog and Resource Catalog (other SID domains, not yet
  ingested).
- Uses EntitySpecification/Entity and CharSpec/CharValue patterns from
  [[wiki/sid/common/root-business-entities-abe]].
— GB922 Common §4.17, pp. 490–506

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
