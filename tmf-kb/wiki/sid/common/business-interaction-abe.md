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
entity_name: "Business Interaction ABE"
---

# Business Interaction ABE

## Overview

The Business Interaction ABE represents an arrangement, contract, or communication
between an enterprise and one or more other entities such as individuals and
organizations (or parts of organizations). Interactions take on the form of requests,
responses, and notifications. — GB922 Common §4.14, p. 435

In the course of doing business a service provider interacts with other entities such
as individuals and organizations (or parts of organizations). Individuals and
organizations are known as parties. Parties can play a number of different roles from
a service provider's perspective. A party could play the role of customer, employee,
supplier, partner, and so forth. Business interactions can also involve such things as
applications, intelligent devices, and other types of resources. Interactions can also
involve customer accounts. — GB922 Common §4.14, p. 435

Business interactions take the form of requests, responses, notifications, and
agreements. — GB922 Common §4.14, p. 435

## Business Entities

Per source overview, the BusinessInteraction model is realised through:

- **BusinessInteraction** — abstract base
- **Request** type — e.g. ProductOrder
- **Response** type
- **Notification** type
- **Agreement** type — formalised contract; specialised in
  [[wiki/sid/common/agreement-abe]] (§4.15)

§4.14 spans pp. 435–454 (20 pages); full BE listings, attributes, and figures BI.01
onwards in source. ProductOrder ([[wiki/sid/product/product-order-abe]]) is a Request
specialisation of BusinessInteraction.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- BusinessInteraction is the parent class for ProductOrder
  ([[wiki/sid/product/product-order-abe]]).
- Agreement ([[wiki/sid/common/agreement-abe]]) is a subclass of BusinessInteraction.
- Interactions involve Parties / PartyRoles ([[wiki/sid/common/party-abe]]).
- May involve Resources, Accounts ([[wiki/sid/common/account-abe]]).
— GB922 Common §4.14, pp. 435–454

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
