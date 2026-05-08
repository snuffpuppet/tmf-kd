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
entity_name: "Party Payment ABE"
---

# Party Payment ABE

## Overview

The Party Payment ABE contains all Entities required to describe a payment such as
PaymentMethod and BankAccount. — GB922 Common §4.6, p. 166

A PartyPayment represents the transfer of wealth from one Party to another. So it is
received from a PartyRole and made to a PartyRole.

The PartyPayment might be either inbound or outbound and always uses a PaymentMethod.
A PartyPayment might specify the BankAccount to which the payment is transferred.
— GB922 Common §4.6, p. 166

A PaymentMethod is declared and owned by a PartyRole that has the right to use it. As
all the PaymentMethod might not be yet described as a sub-class of PaymentMethod, a
PaymentMethod might be described by a PaymentMethodSpecification defining the
characteristics. — GB922 Common §4.6, p. 166

## Business Entities

### PartyPayment

Represents the transfer of wealth between PartyRoles. Inbound or outbound.
— GB922 Common §4.6, p. 166

### PaymentMethod

Means by which a payment is made. Owned by a PartyRole. Specialisations include:

- **CheckPM**
- **DigitalWalletPM**
- **LoyaltyBurnPM**
- **ThirdPartyCollectionPM** (e.g. PayPal, Alipay, bank transfer)

— GB922 Common §4.6, p. 166

### PaymentMethodSpecification

The EntitySpec side; describes characteristics of a PaymentMethod that isn't yet
explicitly modelled as a subclass. — GB922 Common §4.6, p. 166

### PaymentPlan

May specify PaymentMethods to use for auto-pay. If several PaymentMethods are
specified, a priority is given to each of them. Over time, PartyPayments are collected
according to the PaymentPlan. — GB922 Common §4.6, p. 166

### Bank ABE (sub-ABE)

§4.6.5, Figure B.01 — covers Bank, BankAccount, and related entities.
— GB922 Common §4.6.5, p. 172

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- PartyPayment is received/made by PartyRoles ([[wiki/sid/common/party-abe]]).
- LoyaltyBurnPM links to LoyaltyBurn defined in [[wiki/sid/product/loyalty-abe]].
- BankAccount sits in the nested Bank ABE.
- BusinessPartner and Customer Payment scenarios distinguish outgoing/incoming.
— GB922 Common §4.6, pp. 166–172

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/party-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
