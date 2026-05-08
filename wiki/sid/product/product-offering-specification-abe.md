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
entity_name: "Product Offering Specification ABE"
---

# Product Offering Specification ABE

## Overview

The Product Offering Specification ABE describes tangible and intangible goods made
available for a certain price to the market in the form of product catalogs. This ABE
is also responsible for targeting market segments based on the appropriate market
strategy. — GB922 Product §4.3, p. 84

ProductOfferingSpecifications are targeted at one or more MarketSegments based on the
appropriate MarketStrategy. Enterprises create ProductOfferingSpecifications from
ProductSpecifications that have additional market led details applied over a particular
period of time. — GB922 Product §4.3, p. 84

## Business Entities

### ProductOfferingSpecification

Represents what is externally presented to the market for the market's use. It includes
commercial constraints and price. The ProductOfferingSpecification Business Entity is
abstract. Using the atomic/composite pattern, it further specializes into two concrete
Business Entities: AtomicProductOfferingSpecification and
CompositeProductOfferingSpecification. — GB922 Product §4.2, p. 24 / §4.3, p. 84

### AtomicProductOfferingSpecification

Concrete subclass. An AtomicProductOfferingSpecification is always associated with
exactly one ProductSpecification, which itself can be atomic or composite.
— GB922 Product §4.2, p. 24

### CompositeProductOfferingSpecification

Concrete subclass. A CompositeProductOfferingSpecification is not directly associated
with any ProductSpecification. Instead, it contains ProductOfferingSpecifications, each
of which may in turn be an AtomicProductOfferingSpecification associated with a
ProductSpecification, or another CompositeProductOfferingSpecification.
— GB922 Product §4.2, p. 24

### Other entities (in nested sub-ABEs)

- ProductOfferingPrice
- ProductOfferingPriceRule
- ProductOfferingPriceTax
- ProductOfferingPriceCharge / Alteration
- PolicyRule, PolicyStatement, PolicyAction (price governance)
- PricingLogicAlgorithm, PLA Spec
- ProductCatalog
- AllowedProductAction, ProductTypeAction

For full entity listings and figures (Pr.05 through Pr.31, Tax.01–Tax.03, PLA.01,
POP.01, POPR.01, POPT.01, PC.01) see source. — GB922 Product §4.3, pp. 84–166

## Sub-ABEs

The Product Offering Specification ABE contains five nested sub-ABEs:

- §4.3.1 **Pricing Logic Algorithm ABE** (p. 156)
  - §4.3.1.1 **PLA Spec ABE** (p. 158)
- §4.3.2 **Product Catalog ABE** (p. 160)
- §4.3.3 **Product Offering Price ABE** (p. 162)
- §4.3.4 **Product Offering Price Rule ABE** (p. 164)
- §4.3.5 **Product Offering Price Tax ABE** (p. 165)

Per CLAUDE.md §5.2 v1 granularity, sub-ABEs are documented at this overview level only.
Detailed BE listings, attributes, and figures are in GB922 Product v25.5.

## Key Attributes

ProductOfferingSpecification (abstract) inherits from EntitySpecification and RootEntity.
Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- ProductOfferingSpecification is the offering layer over a
  ProductSpecification ([[wiki/sid/product/product-specification-abe]]).
- ProductOfferingSpecification is instantiated as ProductOfferingInstance
  ([[wiki/sid/product/product-and-offering-instance-abe]]).
- Each ProductOfferingSpecification is marketed by a PartyRole
  ([[wiki/sid/product/product-party-roles-abe]] — `MarketingOperator`).
- ProductCatalog contains ProductOfferingSpecifications across one or more
  DistributionChannels (Customer Domain, not yet ingested).
- ProductOfferingSpecification targets MarketSegments based on MarketStrategy
  (not yet ingested).
— GB922 Product §4.3, pp. 84–166

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
