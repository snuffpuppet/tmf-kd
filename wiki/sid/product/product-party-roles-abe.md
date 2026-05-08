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
entity_name: "Product Party Roles ABE"
---

# Product Party Roles ABE

## Overview

Product Party Roles ABE contains all PartyRoles related to the Product Domain such as
ProductManager or ProductUser.

Note: Roles related to Customer such as Payer are located in Customer Domain.
— GB922 Product §4.1, p. 22

## Business Entities

The Product Domain party roles presently identified are: — GB922 Product §4.1, p. 22

### ProductUser

A ProductUser is a type of PartyRole corresponding to the role of using a Product.
— GB922 Product §4.1, p. 22

### ProductManager

A ProductManager is a party role which is responsible for the development of products
for an organization. Product managers own the business strategy behind a product,
specify its functional requirements and generally manage the launch of corresponding
ProductOfferings. They coordinate work done by many other functions (like software
engineers, data scientists and product designers) and are ultimately responsible for
the business success of the product. — GB922 Product §4.1, p. 22

### TaxJurisdiction

TaxJurisdiction is a specific party role played by an organization that has the
authority to levy tax. The geographic area over which tax can be levied is derived
from the base PartyRole class relationship to AdministrativeArea.
— GB922 Product §4.1, p. 22

### LoyaltyProgramMember

A LoyaltyProgramMember is defined on each LoyaltyAccount. A LoyaltyProgramMember is a
type of PartyRole and is granted with the rights on the LoyaltyAccount such as to
execute LoyaltyBurn used to realize a CustomerPayment. — GB922 Product §4.1, p. 22

## Key Attributes

All four roles inherit from `PartyRole` (defined in Common SID), which provides:

- `status: String`
- `validFor: TimePeriod`

`ProductManager` adds `level: String`. — GB922 Product Figure Pr.00, p. 23

For full attribute lists see GB922 Product v25.5 §4.1 and the Common Domain PartyRole
definition (not yet ingested).

## Relationships

- All four entities specialise the `PartyRole` base class from the Common Domain.
- `LoyaltyProgramMember` is associated with `LoyaltyAccount` (defined in
  [[wiki/sid/product/loyalty-abe]]).
- `TaxJurisdiction` relates to `AdministrativeArea` (defined in Common Domain;
  not yet ingested).

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/party-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).
links pending.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested; trilateral
links pending.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute and relationship detail deferred to future ingest
