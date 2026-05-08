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
entity_name: "Product and Offering Instance ABE"
---

# Product and Offering Instance ABE

## Overview

Product and ProductOfferingInstance represent, in the product inventory, respectively
an instance of a ProductSpecification and ProductOfferingSpecification subscribed or
not yet subscribed to by a Customer from the CSP or by the CSP from a BusinessPartner.
The Product carries the place where the product is in use, as well as configuration
characteristics, such as assigned telephone numbers and internet addresses. The Product
and Offering Instance ABE also tracks the links to services and/or resources through
which the Product is realized as well as the applied tariff and commitment duration
related to the ProductOfferingInstance. — GB922 Product §4.4, p. 167

## Business Entities

### Product

Each Product corresponds to a unique ProductSpecification provided to a party. A
Product might be either contained in another Product (CompositeProduct) or in a unique
ProductOfferingInstance at one time. — GB922 Product §4.4, p. 167

### ProductOfferingInstance

Each ProductOfferingInstance corresponds to a unique ProductOfferingSpecification
provided to a party. It might be either be composite (CompositeProductOfferingInstance)
and then contain ProductOfferingInstance or be atomic (AtomicProductOfferingInstance)
and contain a unique Product. — GB922 Product §4.4, p. 167

### AtomicProductOfferingInstance

Concrete subclass containing a unique Product. — GB922 Product §4.4, p. 167

### CompositeProductOfferingInstance

Concrete subclass containing other ProductOfferingInstances.
— GB922 Product §4.4, p. 167

### CompositeProduct

A Product that contains other Products. — GB922 Product §4.4, p. 167

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source GB922 Product
§4.4 (figures Pr.07a1, Pr.07a2 onward).

## Relationships

- Each Product corresponds to a unique ProductSpecification
  ([[wiki/sid/product/product-specification-abe]]).
- Each ProductOfferingInstance corresponds to a unique ProductOfferingSpecification
  ([[wiki/sid/product/product-offering-specification-abe]]).
- A ProductOfferingSpecification is marketed exclusively by the CSP playing a PartyRole
  of MarketingOperator or by a PartyRole Supplier played by another company
  ([[wiki/sid/product/product-party-roles-abe]]).
- The Product Instance carries links to services and resources through which it is
  realised — Service ABE (not yet ingested) and Resource ABE (not yet ingested).
— GB922 Product §4.4, p. 167

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
