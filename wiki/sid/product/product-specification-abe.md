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
entity_name: "Product Specification ABE"
---

# Product Specification ABE

## Overview

The Product Specification ABE contains all that represents a product specification as
perceived by the business user and specifies what the marketing operator wants to sell
at a functional level (i.e. what are the capacities, which usages are available…).
— GB922 Product §4.2, p. 24

The Product domain is essential to the overall SID model. Customers need to be able to
express their functional needs in plain English in order to determine which
ProductSpecifications can support their requirements and which
ProductOfferingSpecifications can propose these ProductSpecifications.
— GB922 Product §4.2, p. 24

## Business Entities

### ProductSpecification

The ProductSpecification represents a product specification as perceived by the Product
user and specifies what the marketing operator wants to sell at a functional level
(i.e. what are the capacities, which usages are available…). The ProductSpecification
Business Entity is abstract. Using the atomic/composite pattern, it further specializes
into two concrete Business Entities: AtomicProductSpecification and
CompositeProductSpecification. — GB922 Product §4.2, p. 24

ProductSpecification inherits `lifecycleStatus` and `validFor` attributes from
`EntitySpecification`, and `ID`, `name` and `description` from `RootEntity`.
— GB922 Product §4.2, p. 24

### AtomicProductSpecification

Concrete subclass of `ProductSpecification`. — GB922 Product §4.2, p. 24

### CompositeProductSpecification

Concrete subclass of `ProductSpecification` that contains other ProductSpecifications.
— GB922 Product §4.2, p. 24

## Sub-ABEs

The Product Specification ABE contains four nested sub-ABEs (full content in source):

- §4.2.1 **Example Product Specification Entities ABE** (p. 79) — illustrative example entities
- §4.2.2 **Goods and Shipping Product Spec ABE** (p. 81) — for tangible goods and shipping
- §4.2.3 **Network Product Spec ABE** (p. 82) — for network-related product specifications
- §4.2.4 **Usage Volume Product Spec ABE** (p. 83) — for usage-volume product specifications

Per CLAUDE.md §5.2 v1 granularity, sub-ABEs are documented as anchored sections within
this page rather than separate files. Detailed content for each sub-ABE is in GB922
Product v25.5 — see source for full BE listings, attributes, and figures.

## Key Attributes

`ProductSpecification` (abstract) — see source GB922 Product §4.2 figures Pr.01–Pr.44b
for the full characteristic and version model. Detailed attribute tables not extracted
in v1 ingest; consult source PDF.

## Relationships

- A ProductSpecification may be made available as one or more
  AtomicProductOfferingSpecifications, which are defined in
  [[wiki/sid/product/product-offering-specification-abe]].
- A `Product` ([[wiki/sid/product/product-and-offering-instance-abe]]) represents the
  instantiation of a ProductSpecification.
- ProductSpecification has characteristic associations with ServiceSpecification
  (Service Domain, not yet ingested) — Figure Pr.44a.
- ProductSpecification has characteristic associations with Resource
  (Resource Domain, not yet ingested) — Figure Pr.44b.
— GB922 Product §4.2, pp. 24–78

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
