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

GB1022 §4.4.3 Table 4-7 enumerates the SID ABEs owned by the Core Commerce
Management block, sourced from GB922 R20.5. The table covers Customer (#01–#04),
Product (#01–#08), Business Partner (#01–#06), and Common (#01–#02) domains.
Cross-walk to our v25.0 / v25.5 / v23.0 corpus and the resulting links are recorded
in [[wiki/open-questions#OQ-042]].

**Product Domain ABEs** (Table 4-7 #01–#08) — resolved to GB922 Product v25.5:

- [[wiki/sid/product/product-and-offering-instance-abe]] (#01 Product ABE — R20.5
  "Product ABE" represented Product instance; v25.5 hosts both Product instance
  and Offering instance content here)
- [[wiki/sid/product/product-specification-abe]] (#02 Product Specification ABE)
- [[wiki/sid/product/strategic-product-portfolio-plan-abe]] (#03 Strategic Product
  Portfolio Plan ABE)
- [[wiki/sid/product/product-offering-specification-abe]] (#04 Product Offering
  ABE — R20.5 entry described offering definitions; v25.5 spec side lives here.
  Offering instance side is also covered by
  [[wiki/sid/product/product-and-offering-instance-abe]] linked above)
- [[wiki/sid/product/product-usage-abe]] (#05 Product Usage ABE)
- [[wiki/sid/product/product-configuration-abe]] (#06 Product Configuration ABE)
- [[wiki/sid/product/loyalty-abe]] (#07 Loyalty ABE)
- [[wiki/sid/product/product-test-abe]] (#08 Product Test ABE)

**Common Domain ABEs** (Table 4-7 #01–#02) — resolved to GB922 Common v23.0:

- [[wiki/sid/common/agreement-abe]] (#01 Agreement ABE)
- [[wiki/sid/common/capacity-abe]] (#02 Capacity ABE)

**Additional Common Domain ABEs from v1 partial sweep (not in Table 4-7):**

The following three Common ABE pages carry CCM back-links added during the v1
partial sweep (see AGENTS.md "Initial trilateral sweep done"). They are not in
GB1022 §4.4.3 Table 4-7 but the inferences are plausible (Catalog is the canonical
parent of Product Catalog; Business Interaction is the canonical parent of
ProductOrder; Account is the canonical parent of CustomerBillingAccount). Linked
here to maintain bidirectional consistency with the existing back-links; flagged
in [[wiki/open-questions#OQ-042]] for source-supported review.

- [[wiki/sid/common/account-abe]] (legacy v1 sweep; not in Table 4-7)
- [[wiki/sid/common/business-interaction-abe]] (legacy v1 sweep; not in Table 4-7)
- [[wiki/sid/common/catalog-abe]] (legacy v1 sweep; not in Table 4-7)

**Customer Domain ABEs** (Table 4-7 entries 01–04: Customer Product Order, Customer
Problem, Customer SLA, Applied Customer Billing Rate) — out of corpus scope per
CLAUDE.md §3 (Customer Domain not in v1).

**Business Partner Domain ABEs** (Table 4-7 entries 01–06: Party Problem, Business
Partner Product Order, Party Product Specification & Offering, Party Revenue
Settlement, Party Service Level Agreement, Applied Party Billing Rate
«Preliminary - Ongoing study») — out of corpus scope per CLAUDE.md §3 (Business
Partner Domain not in v1).

— GB1022 §4.4.3, Table 4-7, pp. 33–36.

## eTOM Processes Realised

GB1022 §4.4.2 Table 4-6 enumerates the eTOM L2 processes realised by the Core
Commerce Management block, sourced from GB921 R20.5. Cross-walk to our GB921
v25.5 corpus and the resulting links are recorded in
[[wiki/open-questions#OQ-042]].

**Product Domain L2s** — resolved to v25.5:

- [[wiki/etom/product-domain/product-configuration-management]] (Table 4-6 R20.5
  1.2.5; same ID, same name)
- [[wiki/etom/product-domain/product-inventory-management]] (R20.5 1.2.11; same
  ID, same name)
- [[wiki/etom/product-domain/product-usage-management]] (R20.5 1.2.16; same ID,
  same name)
- [[wiki/etom/product-domain/product-rating-and-rate-assignment]] (R20.5 1.2.17;
  same ID, same name)
- [[wiki/etom/product-domain/product-balance-management]] (R20.5 1.2.18; same ID,
  same name)
- [[wiki/etom/product-domain/product-support-management]] (v25.5 1.2.4 absorbs
  R20.5 1.2.9 "Product Offering Purchasing" as L3 1.2.4.4 "Support Product
  Offering Purchasing", and R20.5 1.2.15 "Product Test Management" as L3 1.2.4.9
  "Manage Product Test" — same restructuring pattern as Service/Resource Test
  ABEs into Service/Resource Support Management; see OQ-042)

**R20.5 entries deferred or out of scope:**

- R20.5 1.1.5, 1.1.9, 1.1.19 (Sales / Selling / Loyalty Program Management) —
  Market & Sales Domain, out of corpus scope per CLAUDE.md §3
- R20.5 1.2.1, 1.2.2 (Product & Offer Portfolio Planning / Capability Delivery)
  — Strategy/Capability lifecycle, out per §3
- R20.5 1.2.7 — v25.5 retains 1.2.7 in "Business Value Development" vertical, out
  of OFAB scope per §3
- R20.5 1.2.8 (Product Capacity Management) — not in v25.5 OFAB in-scope set
- R20.5 1.3.x (Customer Order Handling / Problem Handling / QoS-SLA Management)
  — Customer Domain, out per §3. Note 1.3.3 likely re-emerges in v25.5 1.2.27
  Product Order Management; left unlinked pending source confirmation (OQ-042)
- R20.5 1.6.x (Party Offering Development & Retirement / Agreement / Order /
  Problem / Special Event / Revenue Sharing) — Business Partner Domain, out
  per §3

— GB1022 §4.4.2, Table 4-6, pp. 29–33.

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

- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x
- OQ-042: Core Commerce Management trilateral sweep — R20.5→v25.x cross-walk
  decisions (resolved Product/Common ABE mappings, eTOM L2 absorption pattern,
  domains out of corpus scope)
