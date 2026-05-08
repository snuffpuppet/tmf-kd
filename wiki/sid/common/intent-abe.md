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
entity_name: "Intent ABE"
---

# Intent ABE

## Overview

The Intent ABE contains the entities needed for specifying basic attributes and
relationships that describe an Intent. — GB922 Common §4.26, p. 864

An Intent contains a set of expectations expressed (expression) in statements using
a particular expressionLanguage.

An Intent Report reports on the status of a given Intent instance. Objects of class
IntentReport are individual intent reports that are created for an intent and as
part of the communication between intent management functions. In accordance with
the Intent class, IntentReport does not have sub-classes for distinguishing
different types of intent reports. The reasons and details of why a report was sent
and for what purpose are stated in the "expression" attribute of IntentReport.
— GB922 Common §4.26.1, p. 864

## Key Attributes

Source §4.26.1 (Figure I.01 — Intent ABE) defines:

- **Intent:** `expression: String`, `expressionLanguage: String`,
  `handlingState: String`, `validFor: TimePeriod`
- **IntentReport:** `expression: String`, `expressionLanguage: String`,
  `reportSequenceNumber: int`, `reportTimestamp: DateTime`

Both Intent and IntentReport extend from `Entity`.

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.26.1–§4.26.2, pp. 864–865

## Relationships

- **Intent ↔ IntentReport** via `IntentReportsAboutIntent` (1 Intent → 0..*
  IntentReports)
- Both **Intent** and **IntentReport** extend `Entity` from
  [[wiki/sid/common/root-business-entities-abe]]
— GB922 Common §4.26.1, pp. 864–865

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Intent ABE not directly mapped in any ODA
Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Intent pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Intent ABE ingested as part of v1 Common gap fill
