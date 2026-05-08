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
entity_name: "Base Types ABE"
---

# Base Types ABE

## Overview

A small simple object, like money or a date range, whose equality isn't based on
identity. — GB922 Common §4.11, p. 296

This paragraph covers the Base Types ABE from Common Business Domain that have been
found to be useful during the documentation of the SID business models.

Standard types like String, Integer etc are not covered as these are usually provided
by commonly used programming languages. It is not intended to define simplistic
restricted fundamental types like String(7) or Number(3).

These Base Types are not intended to have their own identity (they don't have an id
like a Managed Entity). This means that these entities would not normally be shared,
but would be private attributes of an entity. Fowler defines entities like these as
"value objects". — GB922 Common §4.11, p. 296

## Business Entities

### TimePeriod

When there is a need to show that a Business Entity is only valid for a certain time,
this will be shown by an attribute called `validFor`, of type `TimePeriod`. Used as a
private attribute pattern across SID. — GB922 Common §4.11, p. 296

(Other base types such as Money and date ranges are covered in §4.11; full inventory
not extracted in v1.)

## Key Attributes

`TimePeriod` carries `from` / `to` markers; full attribute set in source.

## Relationships

- `validFor: TimePeriod` is a pattern attribute used across virtually every SID entity
  with lifecycle semantics — including ProductSpecification, Product, PartyRole,
  PaymentMethod, etc.
- Not normally shared — embedded as private attribute composition.
— GB922 Common §4.11, pp. 296–301

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
