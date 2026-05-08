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
entity_name: "Account ABE"
---

# Account ABE

## Overview

The Account ABE contains all entities needed for specifying basic attributes and
relationships that describe an account. — GB922 Common §4.13, p. 433

An Account specifies basic attributes and relationships that describe an account.

An Account aims to register all Credits and Debits according to criteria. It carries
one or many Balances (results of Credits and Debits) and might use one or many
Currencies.

Each Account is possessed by one or many PartyRoles such as the Holder or the Payer of
a CustomerBillingAccount. — GB922 Common §4.13, p. 433

## Business Entities

### Account (abstract)

Base account entity. Carries one or many Balances; may use one or many Currencies.

### BusinessPartnerAccount

Carries additional information (such as `creditLimit`) and has specific relationships.
— GB922 Common §4.13, p. 433

### CustomerBillingAccount

As above. — GB922 Common §4.13, p. 433

### FinancialAccount

Part of the sub-ledger accounting that aggregates the amounts of one or more business
partner and/or Customer accounts owned by a given party. It's an internal view of the
CSP to manage incomes and outcomes. — GB922 Common §4.13, p. 433

### BusinessPartnerAccountAssignment / CustomerBillingAccountAssignment

Each accounting event from a BusinessPartnerAccount or CustomerBillingAccount is
logged to a FinancialAccount according to the assignment rules specified by these
entities. — GB922 Common §4.13, p. 433

## Key Attributes

`Account` carries `Balance(s)` and `Currency(ies)`. `BusinessPartnerAccount` /
`CustomerBillingAccount` add `creditLimit`. Detailed attribute tables not extracted in
v1 ingest; consult source.

## Relationships

- Each Account is possessed by one or many PartyRoles
  ([[wiki/sid/common/party-abe]]) such as the Holder or Payer.
- Each Account might be related to other Accounts (parent/child relationship).
- Currency relates via the Currency sub-ABE inside [[wiki/sid/common/party-abe]]
  (§4.4.45).
- Assignments relate Account entries to FinancialAccount.
— GB922 Common §4.13, pp. 433–434

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/party-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
