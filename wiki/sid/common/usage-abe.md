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
entity_name: "Usage ABE"
---

# Usage ABE

## Overview

An occurrence of employing a Product, Service or Resource for its intended purpose,
which is of interest to the business and can have charges applied to it. It is
comprised of characteristics, which represent attributes of usage.
— GB922 Common §4.24, p. 817

Put simply, usage is how much product is used, by whom is it used, where and when is
it used and circumstances under which it is used. Normally, when a usage event
occurs, it is stored in a network element, for instance in a switch, router, gateway
or in an application system. Resources (applications, network and computing
capabilities) usually store usage data in proprietary formats that are not
understood by external systems, such as billing systems. Depending on the polling
strategy, a mediation engine connects to resources, collects usage data and formats
them into a format that is understood by the billing system. Outputs of a mediation
engine are Usage Detail Records (UDRs). Examples of UDRs are Call Detail Records
(CDRs – used to describe usage details of voice call services) and Internet
Protocol Detail Records (IPDRs – used to describe usage details of Internet
Protocol based services). — GB922 Common §4.24.1, p. 817

## Key Attributes

Source §4.24.1 (Figure U.01) shows the abstract Usage class with:

- **Usage:** `usageDate: DateTime`, `usageStatus: Integer`
- Example specialisation **VoiceCallUsage:** `callDuration: Integer`, `callType:
  String`, `destinationAddress: String`, `originationAddress: String`, `timeOfCall:
  DateTime`

Source §4.24.2 (Figure U.02 — Usage Specification) defines:

- **UsageSpecification** — describes a type of usage; comprised of
  UsageSpecCharacteristics that define attributes (Name, Category, Min/Max
  cardinalities)
- **UsageSpecCharacteristic** — characterises an attribute by name, category
  ("Who/When/What/Where/Why"), presence, allowed values
- **UsageSpecCharacteristicValue** — describes allowed values or value ranges
- **UsageCharacteristicValue** — holds actual data on a Usage instance

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.24.1–§4.24.2, pp. 817–820

## Relationships

- **Specialisations:** ProductUsage, ServiceUsage, ResourceUsage — each living in
  its domain ABE:
  [[wiki/sid/product/product-usage-abe]],
  [[wiki/sid/service/service-usage-abe]],
  [[wiki/sid/resource/resource-usage-abe]]
- **UsageSpecCharacteristic** uses the Characteristic pattern from
  [[wiki/sid/common/root-business-entities-abe]] (GB922-1R Root Business Entities
  addendum)
— GB922 Common §4.24, pp. 817–820

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Common Usage ABE not directly mapped in any
ODA Functional Block table; specialised Usage ABEs are mapped via their
specialisation parent's ODA owner.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings pending; v25.5 1.4.8 Service
Guiding & Mediation, 1.5.10 Resource Mediation & Reporting, and 1.2.16 Product
Usage Management are likely candidates but the link should be filed against the
specialisation rather than the Common parent.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Usage ABE ingested as part of v1 Common gap fill
