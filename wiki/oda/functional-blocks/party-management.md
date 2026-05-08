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

GB1022 §4.3.3 (Standard Business Information Entities) provides a verbatim mapping
table from Frameworx SID ABEs to the Party Management block (source GB922 R20.5).
Domains covered: Market/Sales, Customer, Business Partner, Common (Party).

The full mapping table is in source pp. 24–27. Sample entries (R20.5 source naming):
- Customer Party Roles, Customer Interaction, Customer Bill (Customer Domain)
- Market & Sales Strategy and Plan, Market Segment, Competitor, Sales Channel
  (Market/Sales Domain)
- Party (Common Domain) — corresponds to [[wiki/sid/common/party-abe]] in v23.0
  corpus
- Privacy management ABEs — correspond to [[wiki/sid/common/party-privacy-abe]]
- Party Payment, Bank — correspond to [[wiki/sid/common/party-payment-abe]]
- Communication Interaction — corresponds to
  [[wiki/sid/common/communication-interaction-abe]]
- Account — corresponds to [[wiki/sid/common/account-abe]]
- Agreement — corresponds to [[wiki/sid/common/agreement-abe]]

See [[wiki/open-questions#OQ-008]] (trilateral sweep deferred) and
[[wiki/open-questions#OQ-037]] (R20.5 → v25.x version mismatch). Many R20.5 ABEs
referenced (Market Sales Domain ABEs, Customer Domain ABEs) are NOT in our v1
corpus scope (Customer/Sales/Market domains excluded per CLAUDE.md §3); those
references are preserved verbatim in source but not wikilinked.

## eTOM Processes Realised

GB1022 §4.3.2 (Business Processes in the Party Management Block) provides a
verbatim mapping table from eTOM L2 processes to the Party Management block (source
GB921 R20.5). The full mapping covers many L1.1 (Market) and L1.2 (Sales) processes
that are out of corpus scope per CLAUDE.md §3, plus selected Customer/Common
processes.

The full mapping table is in source pp. 18–24.

See [[wiki/open-questions#OQ-008]] (trilateral sweep deferred) and
[[wiki/open-questions#OQ-037]] (R20.5 → v25.x version mismatch). Most processes
mapped from Party Management are out of scope (Market/Sales/Customer domains); those
that fall in Product/Service/Resource Domain × OFAB will be linked during the
trilateral sweep.

## Component Dependencies

- [[wiki/oda/functional-blocks/core-commerce-management]] — Party data feeds CCM
  ordering and billing
- [[wiki/oda/functional-blocks/production]] — Service Provisioning consumes Party
  identity data
- [[wiki/oda/functional-blocks/engagement-management]] — surfaces Party data through
  user journeys
- [[wiki/oda/functional-blocks/intelligence-management]] — analyses Party behaviour

## Open Questions

- OQ-008: ODA↔eTOM↔SID trilateral linking sweep deferred
- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x;
  many references resolve to scope-excluded domains (Market/Sales/Customer)
