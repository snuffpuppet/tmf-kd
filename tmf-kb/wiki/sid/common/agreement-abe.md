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
entity_name: "Agreement ABE"
---

# Agreement ABE

## Overview

An Agreement represents a contract or arrangement, either written or verbal and
sometimes enforceable by law, such as a service level agreement or a customer price
agreement. An agreement involves a number of other business entities, such as
products, services, and resources and/or their specifications.
— GB922 Common §4.15, p. 455

One form of business interaction in which Parties (for example, Service Providers or
Customers) engage is an agreement. In the SID model an agreement is a subclass (type)
of BusinessInteraction. A resulting benefit is that an agreement inherits a number of
informational characteristics from business interaction in the model.
— GB922 Common §4.15, p. 455

## Business Entities

### Agreement

Subclass of `BusinessInteraction` ([[wiki/sid/common/business-interaction-abe]])
representing a contract or arrangement.

Specialisations include:

- **ServiceLevelAgreement** (SLA)
- **CustomerPriceAgreement**
- Others as defined in source

§4.15 spans pp. 455–473 (19 pages); full BE inventory and figures A.01 onwards in
source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Agreement is a subclass of BusinessInteraction
  ([[wiki/sid/common/business-interaction-abe]]).
- Engages PartyRoles ([[wiki/sid/common/party-abe]]) such as Service Provider and
  Customer.
- Involves Products, Services, Resources and/or their specifications. ProductOrder
  may refer to an Agreement ([[wiki/sid/product/product-order-abe]]).
- PrivacyAgreement ([[wiki/sid/common/party-privacy-abe]]) is a Privacy-specific
  Agreement specialisation.
— GB922 Common §4.15, pp. 455–473

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/party-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
