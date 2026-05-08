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
entity_name: "Configuration and Profiling ABE"
---

# Configuration and Profiling ABE

## Overview

A Configuration (also referred to as a Profile) defines how a Resource, Service, or
Product operates or functions in terms of Characteristic Specifications and related
Product/Service/Resource Specifications as well as Characteristics and related
Product/Service/Resource entities. — GB922 Common §4.18, p. 507

A Configuration may contain one or more parts (which is realized by using the
Atomic/Composite pattern, but it is represented as a single entity -
ConfigurationRelationship), and each part may contain zero or more fields. Each field
may have attributes that are statically or dynamically defined. Some of these fields
have fixed values, while others provide values from which a choice or choices can be
made (e.g., using the EntitySpec/Entity and/or CharacteristicSpec/CharacteristicValue
patterns). — GB922 Common §4.18, p. 507

The SID framework has defined both a Service Configuration ABE as well as a Resource
Configuration ABE. There are eTOM L2 core processes that deal with configuring services
(Service Configuration & Activation) and provisioning resources (Resource
Provisioning), as well as TAM applications that support these processes and ABEs. The
purpose of this document is to define these two key concepts from these ABEs, and
describe how they can be used to aid in the configuration process. There is also a
Product Configuration ABE that has been added to the SID framework that is included.
— GB922 Common §4.18, pp. 507

## Business Entities

This is the **canonical** Configuration ABE that
[[wiki/sid/product/product-configuration-abe]] specialises for Product. Service
Configuration ABE and Resource Configuration ABE specialise it for those domains.

Core entities:

- **Configuration** — abstract base
- **ConfigurationSpec** — EntitySpec side
- **ConfigurationRelationship** — Atomic/Composite realisation
- **ConfigSpecRelationship** — relationship at the spec level

§4.18 spans pp. 507–519 (13 pages); full inventory and figures CP.01 onwards in
source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialised by Product Configuration
  ([[wiki/sid/product/product-configuration-abe]]).
- Service Configuration and Resource Configuration ABEs sit in their respective domain
  documents (not yet ingested).
- Uses CharacteristicSpec/CharacteristicValue and EntitySpec/Entity patterns from
  [[wiki/sid/common/root-business-entities-abe]].
— GB922 Common §4.18, pp. 507–519

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
