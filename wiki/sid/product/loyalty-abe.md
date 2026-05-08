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
entity_name: "Loyalty ABE"
---

# Loyalty ABE

## Overview

A loyalty program is one of the tools used by the loyalty process to retain customers.

The Loyalty ABE contains all entities useful to specify and instantiate loyalty
programs.

A LoyaltyProgramProdSpec defines the LoyaltyRules that have to be checked in order to
identify the actions to apply.

Depending on the type of LoyaltyRules a LoyaltyAccount might be needed to collect gains
or not.

A LoyaltyProgramProduct is a type of ProductComponent and described by a
LoyaltyProgramProdSpec. — GB922 Product §4.7, p. 217

> A loyalty program is one of the tools used by the loyalty process to retain
> customers. For example, another tool is the ProductOfferingSpecification Commitment.
> The aim of marketing is to find levers in the form of rewards to enhance customer
> loyalty to its operator. — GB922 Product §4.7, p. 217

## Business Entities

### LoyaltyProgramProdSpec

A type of ProductSpecification that defines the LoyaltyRules to be checked.
— GB922 Product §4.7, p. 217

### LoyaltyProgramProduct

A type of `ProductComponent` described by a LoyaltyProgramProdSpec.
— GB922 Product §4.7, p. 217

### LoyaltyAccount

Account entity that collects loyalty gains. Depending on the type of LoyaltyRules a
LoyaltyAccount might be needed or not. — GB922 Product §4.7, p. 217

### LoyaltyRule

Rule definitions checked to identify actions to apply.
— GB922 Product §4.7, p. 217

### LoyaltyBurn

Action that consumes loyalty value from a LoyaltyAccount, used to realize a
CustomerPayment. — GB922 Product §4.7, p. 217 (referenced in §4.1)

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- LoyaltyProgramMember ([[wiki/sid/product/product-party-roles-abe]]) is defined on
  each LoyaltyAccount and is granted rights including LoyaltyBurn execution.
- LoyaltyProgramProdSpec is a subtype of ProductSpecification
  ([[wiki/sid/product/product-specification-abe]]).
- LoyaltyProgramProduct is a type of ProductComponent — relates to Product entities
  in [[wiki/sid/product/product-and-offering-instance-abe]].
- LoyaltyBurn relates to CustomerPayment (Customer Domain, not yet ingested).
— GB922 Product §4.7, pp. 217–235

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
