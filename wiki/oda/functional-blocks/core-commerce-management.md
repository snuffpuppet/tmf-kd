---
type: oda-component
spec_id: GB1022
spec_version: "1.1.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf
source_extract_paths:
  - raw/extracted/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.md
authority: primary
oda_domain: "Functional Blocks"
component_id: "GB1022 §4.4"
component_name: "Core Commerce Management"
psr_layer: "product"
---

# Core Commerce Management

> **Architectural role.** Per GB1022 §3 Systems of Separation: Core Commerce
> Management is one of three blocks in the **Systems of Records** group — the
> commercial layer.
>
> **Production/commercial relevance.** This is the **commercial-side** block. It
> handles Product Offerings, Catalogues, Order Capture, Charging — the "WHAT" of
> the business in commercial terms. It pairs with [[wiki/sid/product-abe]] (Product
> ABE) on the data layer and with the operational Product Domain L2s on the process
> layer ([[wiki/etom/product-domain/_index]]).

## Overview

The Core Commerce Management (CCM) Block represents the part of the enterprise that
is concerned with enabling profitable exchange of goods and services. It includes
all those activities which directly or indirectly facilitate that exchange such as
marketing & sales, sourcing and procurement, strategic (buying & selling) portfolio
plans (commercial rules), life-cycle product management, offer management, new
business development - for all types of business engagements - B2B, B2C, C2C, B2B2X
etc. It is responsible for formalizing business models, revenue generation and
business assurance processes. — GB1022 §4.4.1, p. 28

Core Commerce Management can be characterized as follows:

- Core Commerce Management deals with **"WHAT"**
- It handles the catalogue of Product Offerings and Products marketed by the telco
  operator for all types of business (B2C, B2B, B2B2X, …)
- Core Commerce Management is in charge of Product Offerings and Products Catalogue
  oriented processes, functions and repositories such as:
    - Product Offerings and Products Catalogue Management
    - Order Handling, from Order Capture & Configuration to the global orchestration
      of the Customer Order Delivery
    - Rating of any types of charges and Bill items Calculation
    - Business Partners Revenue Sharing & Settlement
    - Product Assurance
    - Product Strategy activities
- Core Commerce Management is independent from technical concerns - managed by
  Production – to be able to decouple commercial and technical evolution

— GB1022 §4.4.1, p. 28

## Responsibilities

Per source bullet list above plus Table 4-5 (eTOM Process Descriptions) in §4.4.2
and Table 4-6 (SID ABE mappings) in §4.4.3.

## SID Entities Owned

GB1022 §4.4.3 (Standard Business Information Objects) provides a verbatim mapping
table from Frameworx SID ABEs to the Core Commerce Management block (source GB922
R20.5). Primary domains covered: Product, Customer, Common.

The full mapping table is in source pp. 33–36. Key entries (R20.5 source naming) and
their v25.x equivalents in this corpus:

- Product Specification, Product Offering, Product, Product Order, Product Usage,
  Product Configuration, Loyalty, Product Catalog →
  [[wiki/sid/product-abe]] category (12 ABEs in v25.5)
- Catalog (canonical) → [[wiki/sid/common/catalog-abe]]
- Agreement → [[wiki/sid/common/agreement-abe]]
- Account → [[wiki/sid/common/account-abe]]
- Customer Bill, Customer Bill Inquiry, Customer Bill Cycle (Customer Domain — out
  of corpus scope; preserved as source reference)
- Business Interaction → [[wiki/sid/common/business-interaction-abe]]

See [[wiki/open-questions#OQ-008]] and [[wiki/open-questions#OQ-037]].

## eTOM Processes Realised

GB1022 §4.4.2 (Business Processes in the Core Commerce Management Block) provides a
verbatim mapping table from eTOM L2 processes to the CCM block (source GB921 R20.5).
The full mapping is in source pp. 29–33.

In v25.5 corpus terms, CCM is the ODA realisation of much of:
- Product Domain operational L2s ([[wiki/etom/product-domain/_index]]) — particularly
  Product Order Management (1.2.27), Product Configuration Management (1.2.5),
  Product Inventory Management (1.2.11), Product Catalog Operational Readiness /
  Content Management (1.2.21, 1.2.22), Product Usage / Rating / Balance Management
  (1.2.16, 1.2.17, 1.2.18), Product Anomaly / Problem Management (1.2.25, 1.2.26),
  Product Performance Management (1.2.6), Product Support Management (1.2.4)

See [[wiki/open-questions#OQ-008]] and [[wiki/open-questions#OQ-037]].

## Component Dependencies

- [[wiki/oda/functional-blocks/party-management]] — Party data is used for Customer
  Order Capture, Billing
- [[wiki/oda/functional-blocks/production]] — Production exposes Service capabilities
  that CCM offers as Products; Production supplies Usage records for CCM rating
- [[wiki/oda/functional-blocks/engagement-management]] — surfaces CCM via user
  journeys
- [[wiki/oda/functional-blocks/intelligence-management]] — analyses commerce data
- [[wiki/oda/functional-blocks/decoupling-and-integration]]

## Open Questions

- OQ-008: ODA↔eTOM↔SID trilateral linking sweep deferred
- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x
