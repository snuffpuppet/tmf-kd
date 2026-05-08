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
entity_name: "Product Configuration ABE"
---

# Product Configuration ABE

## Overview

The Product Configuration ABE represents the specification of the different possible
Product configurations as well as the Product Configurations instantiated for a
Product. — GB922 Product §4.8, p. 236

> A Configuration (also referred to as a Profile) defines how a Resource, Service, or
> Product operates or functions. A Configuration may contain one or more parts (which
> is realized by using the Atomic/Composite pattern, but it is represented as a single
> entity - ConfigurationRelationship), and each part may contain zero or more fields.
> Each field may have attributes that are statically or dynamically defined. Some of
> these fields have fixed values, while others provide values from which a choice or
> choices can be made (e.g., using the EntitySpec/Entity and/or
> CharacteristicSpec/CharacteristicValue patterns). — GB922 Product §4.8, p. 236

> Refer to Common Domain guide book section Configuration and Profile ABE for more
> details. — GB922 Product §4.8, p. 236

## Business Entities

The Product Configuration ABE applies the generic Configuration pattern (defined in
Common Domain) to the Product entity. The full Configuration model is in the Common
Domain SID guidebook (not yet ingested). Concrete Product-specific entities derived
from the pattern include:

### ProductConfiguration

A Configuration applied to a Product instance, defining how the Product operates or
functions. — GB922 Product §4.8, p. 236 (Figure CP.01)

### ProductConfigurationSpec

The EntitySpecification side of the Entity/EntitySpec pattern for ProductConfiguration —
defines reusable configuration specifications. — GB922 Product §4.8, p. 236

### ConfigurationRelationship

Represents the Atomic/Composite relationship between Configurations.
— GB922 Product §4.8, p. 236

### ConfigSpecRelationship

Equivalent relationship at the specification level.
— GB922 Product §4.8, p. 236

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; the Configuration pattern is
shared with Resource and Service Configurations and is fully defined in the Common
Domain SID document (not yet ingested).

## Relationships

- The Configuration pattern is shared across Product, Service, and Resource — see
  Resource Configuration and Service Configuration ABEs (not yet ingested).
- ProductConfiguration is associated with Product
  ([[wiki/sid/product/product-and-offering-instance-abe]]).
- ProductConfigurationSpec relates to ProductSpecification
  ([[wiki/sid/product/product-specification-abe]]) via the EntitySpec/Entity pattern.
- ConfigurationRelationship and ConfigSpecRelationship enable nested configurations
  (e.g. for circuit-pack-style aggregate entities).
— GB922 Product §4.8, pp. 236–245

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
