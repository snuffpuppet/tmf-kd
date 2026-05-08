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
component_id: "GB1022 §4.3"
component_name: "Party Management"
psr_layer: "cross-cutting"
---

# Party Management

> **Architectural role.** Per GB1022 §3 Systems of Separation: Party Management is
> one of three blocks in the **Systems of Records** group (with Core Commerce
> Management and Production) — responsible for operational processes with stable,
> long-lived data.

## Overview

The Party Management (PM) Block handles all interactions and data associated with
entities or actors that are involved or likely to get involved with the enterprise.
Party roles and behaviors are not dependent on industry specifics. This block
includes support for identification processes which are required to validate parties
and management of Party relationships. — GB1022 §4.3.1, p. 18

Party Management can be characterized as follows:

- Party Management deals with **"WHO" & "WHY"**
- It handles Persons and Organizations (called Party) involved in business
  processes. These Parties can be Customers, Business Partners or Employees.
- In charge of Party oriented processes, functions and repositories such as:
    - Party, Party Information and Privacy Management, Party Roles and Rights
      Management
    - Party Interaction Management
    - Billing Account Management and Bill Production
    - Party Financial Management activities: payment, bill inquiry, dunning, …
    - Market and Party Strategy activities
- Party Management is not Telco specific, as any type of digital industry has now
  this kind of needs.

— GB1022 §4.3.1, p. 18

## Responsibilities

Per the source's bullet list above plus Table 4-3 (eTOM Process Descriptions) and
Table 4-4 (SID ABE mappings) in §4.3.

## SID Entities Owned

GB1022 §4.3.3 Table 4-4 enumerates the SID ABEs owned by the Party Management
block, sourced from GB922 R20.5. The table covers Market/Sales (#01–#07), Customer
(#01–#05), Business Partner (#01–#08), Common (#01–#02), Enterprise (#01),
Product (#01), Service (#01), and Resource (#01) domains. Cross-walk to our
v23.0 / v25.0 / v25.5 corpus and the resulting links are recorded in
[[wiki/open-questions#OQ-043]].

Note: GB1022 Table 4-4 places Party (#02) and Party Privacy (#08) under Business
Partner Domain. Our v23.0 GB922 Common places them under Common Domain — a R20.5
→ v23.0 reorganization (Party concepts moved to Common because they are truly
cross-cutting). The same concepts are linked below to their v23.0 Common ABE
homes; the domain reorg is documented in OQ-043.

**Common Domain ABEs** — resolved to GB922 Common v23.0:

- [[wiki/sid/common/communication-interaction-abe]] (Table 4-4 Common #01
  Communication Interaction)
- [[wiki/sid/common/party-abe]] (Table 4-4 Business Partner #02 Party — domain
  reorg R20.5→v23.0; same canonical Party concept)
- [[wiki/sid/common/account-abe]] (Table 4-4 Business Partner #03 Business
  Partner Account — v23.0 Common Account ABE explicitly includes
  BusinessPartnerAccount)
- [[wiki/sid/common/party-privacy-abe]] (Table 4-4 Business Partner #08 Party
  Privacy — domain reorg R20.5→v23.0)

**Domain Party Roles ABEs** — resolved to GB922 v25.x:

- [[wiki/sid/product/product-party-roles-abe]] (Table 4-4 Product #01)
- [[wiki/sid/service/service-party-roles-abe]] (Table 4-4 Service #01)
- [[wiki/sid/resource/resource-party-roles-abe]] (Table 4-4 Resource #01)

**Additional Common ABEs from v1 partial sweep (not in Table 4-4):**

The following two Common ABE pages carry pre-existing PM back-links from the v1
partial sweep, not directly supported by Table 4-4. Inferences are plausible
(Agreement: Party Agreement Management is in §4.3.1; Party Payment: R20.5 BP #05
Party Bill Collection mentions PartyPayment but is narrower than the v23.0 Party
Payment ABE). Linked here to maintain bidirectional consistency; flagged in
[[wiki/open-questions#OQ-043]] for source-supported review.

- [[wiki/sid/common/agreement-abe]] (legacy v1 sweep; not in Table 4-4)
- [[wiki/sid/common/party-payment-abe]] (legacy v1 sweep; partial support via
  R20.5 BP #05)

**Out of corpus scope:**

- Market/Sales Domain entries 01–07 — Market/Sales Domain not in v1 corpus per
  CLAUDE.md §3
- Customer Domain entries 01–05 — Customer Domain not in v1 corpus per §3
- Business Partner Domain entries 01 Party Strategy & Plan, 04 Party Bill
  «preliminary», 05 Party Bill Collection, 06 Business Partner Party Roles,
  07 Party Interaction (overlaps Communication Interaction already linked) —
  Business Partner Domain not in v1 corpus per §3
- Common #02 Users and Roles — no clean v23.0 successor (closest match would
  be PartyRole within Party ABE which is already linked)
- Enterprise #01 Enterprise Party Roles — Enterprise Domain not in v1 corpus
  per §3

— GB1022 §4.3.3, Table 4-4, pp. 24–27.

## eTOM Processes Realised

GB1022 §4.3.2 Table 4-3 enumerates the eTOM L2 processes realised by the Party
Management block, sourced from GB921 R20.5. **All 32 entries fall in domains
outside corpus scope** (Market 1.1.x, Customer 1.3.x, Business Partner 1.6.x —
none in Service / Resource / Product per CLAUDE.md §3). Party Management
therefore produces zero eTOM L2 wikilinks under v1 corpus scope. This is
source-supported absence, not a corpus gap — see [[wiki/open-questions#OQ-043]]
for the full enumeration.

The 1.X.Y "Party Identification & Authentication" placeholder in Table 4-3 is
also out of scope and source-flagged "to be discussed for next versions".

— GB1022 §4.3.2, Table 4-3, pp. 18–23.

## Component Dependencies

- [[wiki/oda/functional-blocks/core-commerce-management]] — Party data feeds CCM
  ordering and billing
- [[wiki/oda/functional-blocks/production]] — Service Provisioning consumes Party
  identity data
- [[wiki/oda/functional-blocks/engagement-management]] — surfaces Party data through
  user journeys
- [[wiki/oda/functional-blocks/intelligence-management]] — analyses Party behaviour

## Open Questions

- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x;
  many references resolve to scope-excluded domains (Market/Sales/Customer)
- OQ-043: Party Management trilateral sweep — R20.5→v23.0/v25.x cross-walk
  decisions (domain reorganization for Party / Party Privacy; out-of-scope
  enumeration for Market/Sales/Customer/Business Partner; pre-existing
  Agreement and Party Payment back-links flagged for source-supported review)
