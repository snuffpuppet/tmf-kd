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
entity_name: "Communication Interaction ABE"
---

# Communication Interaction ABE

> **Sub-domain note.** GB922 Common §4.7 explicitly states this ABE is **located in
> "Shared Business Entities Domain"** (not Common). The wiki retains
> `abe_category: common` for v1 schema consistency; the source-stated sub-domain is
> preserved here as text. See [[wiki/open-questions#OQ-014]].

## Overview

The Communication Interaction ABE contains all entities needed for specifying a
CommunicationInteraction describing an exchange of information during a communication
between two or more human(s) and/or machine(s) during a period of time.

CommunicationInteraction might concern Parties playing a role of Customer, Supplier…
or even Resource, therefore the ABE «Communication Interaction ABE» is located in
«Shared Business Entities Domain». — GB922 Common §4.7, p. 173

## Business Entities

### CommunicationInteraction

Describes an exchange of information during a communication between two or more
human(s) and/or machine(s) during a period of time. Examples:

- A person calling another one with a request such as questions about his customer
  order not yet delivered or claiming about his product dysfunction
- A company broadcasting advertising on a media such as TV or radio
- A computer sending information to another one such as an order sent to a supplier
- A customer ordering a ProductOffering using the CSP web portal

— GB922 Common §4.7, p. 173

### CommunicationInteractionItem

Items within a CommunicationInteraction; hierarchical structure (Figure CI.04).
— GB922 Common §4.7, p. 175

### CommunicationInteraction UseCase / Result

Pattern entities for use case and result classification (Figure CI.03).
— GB922 Common §4.7, p. 177

For full attribute tables and figures CI.01–CI.05 plus illustrations I01/I02 in source
§4.7, pp. 173–187.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- CommunicationInteraction relates to PartyRoles
  ([[wiki/sid/common/party-abe]]) — Customer, Supplier, etc.
- May relate to Resources (Resource Domain, not yet ingested).
- Sourced as the trigger for ProductOrder
  ([[wiki/sid/product/product-order-abe]] §4.5).
— GB922 Common §4.7, pp. 173–187

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/party-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-014: Source places this ABE in "Shared" sub-domain; v1 wiki schema does not
  formalise the split
