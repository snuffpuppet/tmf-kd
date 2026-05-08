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
entity_name: "Root Business Entities ABE"
---

# Root Business Entities ABE

> **Foundational ABE.** This is the top of the SID class hierarchy. RootEntity sits at
> the root of the inheritance tree; many SID entities across all domains inherit
> attributes from it. See [[wiki/foundations/information-framework]] for the
> conceptual definition.

## Overview

A set of common business entities that collectively serve as the foundation of the
business view. This set of entities enables the entities in different domains of the
SID Framework to be associated with each other, providing greater overall coherence to
the information framework. — GB922 Common §4.12, p. 302

This is the top of the SID class hierarchy. The purpose of the RootEntity is to define
a set of attributes that are common to select SID entities in the Product, Service and
Resource domains, such as Service, Service Specification, Resource, and Resource
Specification, as well as Policy entities in the Common Business Entities domain.
These properties enable us to name and describe all objects (manageable and
unmanageable) in the environment. — GB922 Common §4.12, p. 302

## Business Entities

### RootEntity (abstract)

The top of the SID class hierarchy. Provides:

- `ID` — unique identity
- `name` — generic naming
- `description` — optional descriptive text

A RootEntity might be categorized by a `RootEntityType` and described by one or many
`Attachments`. — GB922 Common §4.12, p. 302

### RootEntityType

Categorization classifier — represents a SID Entity such as Product or
ProductSpecification. Used by Privacy ([[wiki/sid/common/party-privacy-abe]]) and
elsewhere as a meta-level reference. — GB922 Common §4.12, p. 302

### EntitySpecification (abstract)

The "Spec" side of the EntitySpec/Entity pattern used pervasively throughout SID.
Carries `lifecycleStatus` and `validFor` attributes. — GB922 Common §4.12

### Entity (abstract)

The instance side of the EntitySpec/Entity pattern. — GB922 Common §4.12

### ManagedEntity / EntityIdentification

Entities with explicit identity for management purposes. — GB922 Common §4.12

### Collection

Represents collections of ManagedEntity objects, used by Policy ABE
(PolicyRepository, PolicyEventBase) and Logical Resource ABE (ReplacementSet).
— GB922 Common §4.12, p. 302

### Attachment

Used by RootEntity to associate brochures, manuals, or other supporting documents.
— GB922 Common §4.12, p. 302

### Characteristic / CharacteristicSpec / CharacteristicValue

The CharSpec / CharValue pattern for describing properties of entities.
— GB922 Common §4.12

§4.12 spans pp. 302–432 (131 pages, the largest single ABE chapter in this document).
Many additional pattern entities and figures (R.01 onwards) are in the source.

## Key Attributes

`RootEntity` attributes (verbatim):

- `ID`
- `name: String` — generic naming
- `description: String` — optional

`EntitySpecification` adds:

- `lifecycleStatus`
- `validFor: TimePeriod` (from [[wiki/sid/common/base-types-abe]])

Detailed attribute tables for the rest not extracted in v1; consult source.

## Relationships

- Almost every other SID entity ultimately inherits from RootEntity directly or
  through EntitySpecification / Entity / ManagedEntity.
- RootEntityType is the meta-level reference used by Privacy and other ABEs that
  declare cross-cutting interest in arbitrary SID entity types.
— GB922 Common §4.12, pp. 302–432

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-018: §4.12 is the largest single ABE chapter (131 pages); v1 ingest covers
  conceptual top-of-hierarchy only — many pattern entities require deeper ingest
