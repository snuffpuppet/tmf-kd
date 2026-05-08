---
type: sid-abe
spec_id: GB922
spec_version: "25.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Service_v25.0.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Service_v25.0.md
authority: primary
abe_category: service
entity_name: "Service Specification ABE"
---

# Service Specification ABE

> **Production/commercial relevance.** This ABE introduces the **CFSSpec/RFSSpec**
> distinction — **Customer Facing Service Specification** (commercial layer) vs
> **Resource Facing Service Specification** (production/technical layer). This is
> directly the separation the corpus's PSR mapping goal targets.

## Overview

The Service Specification ABE contains entities that define the shared characteristics
of both types of Service entities. This enables multiple instances to be derived from
a single specification entity. In this derivation, each instance will use the
characteristics defined in its associated specification.

The Service Specification ABE is composed of two main concepts:

1. The CSP Know-Hows specification a.k.a. Customer Facing Services Specification or
   CFSSpec that describe only functional characteristics and capabilities that the CSP
   can provide to a customer however the CSP builds on its own all or part of the
   technical solution. Note that it corresponds only to non-tangible goods.
2. The Technical solution specification a.k.a. Resource Facing Services Specification
   or RFSpec that describes only technical characteristics and capabilities.

— GB922 Service §4.3, p. 22

Entities in this ABE focus on adherence to standards, distinguishing features of a
Service, dependencies (both physical and logical, as well as on other services),
quality, and cost. In general, entities in this ABE enable Services to be bound to
Products and run using Resources. — GB922 Service §4.3, p. 22

## Business Entities

### ServiceSpecification (abstract)

The shared specification base for both CFS and RFS specifications.
— GB922 Service §4.3, p. 22

### CustomerFacingServiceSpec (CFSSpec)

The CSP Know-Hows specification describing functional characteristics and capabilities
provided to a customer (commercial layer of the SID model). Non-tangible goods only.
— GB922 Service §4.3, p. 22

### ResourceFacingServiceSpec (RFSSpec)

The Technical solution specification describing technical characteristics and
capabilities (production layer). — GB922 Service §4.3, p. 22

### ServiceSpecificationType / ServiceSpecificationRole

Type and role classification entities. — GB922 Service §4.3 (Figures SO.14, SO.17)

### ServiceSpecCharacteristic / ServiceSpecCharacteristicValue

The characteristic specification pattern from the Information Framework, applied to
ServiceSpec. — GB922 Service §4.3 (Figures SO.22, SO.23)

### ServicePackageSpec / ServiceBundleSpec

Aggregation specifications. ServicePackage groups CFSSpecs; ServiceBundle aggregates
on the RFS side. — GB922 Service §4.3 (Figures SO.25–SO.30)

### NetworkServiceSpec, UsageVolumeServiceSpec

Specialised RFS subtypes. — GB922 Service §4.3 (Figures SO.31–SO.33)

## Sub-ABEs

§4.3 contains nested sub-ABEs:

- §4.3.1 **Customer Facing Service Spec ABE** (p. 69) — with §4.3.1.1 Examples,
  §4.3.1.2 Role, §4.3.1.3 Network Service Spec («Preliminary»), §4.3.1.4 Service
  Package, §4.3.1.5 Usage Volume Service Spec («Preliminary»)
- §4.3.2 **Resource Facing Service Spec ABE** (p. 78) — with §4.3.2.1 Role,
  §4.3.2.2 Service Bundle (and Examples sub-sub-ABE)
- §4.3.3 **Service Catalog ABE** (p. 83)

Per CLAUDE.md §5.2 v1 granularity, sub-ABEs are documented at this overview level.

## Key Attributes

ServiceSpecification inherits from EntitySpecification
([[wiki/sid/common/root-business-entities-abe]]) — `lifecycleStatus`, `validFor`,
plus RootEntity `ID`, `name`, `description`. Detailed attribute tables not extracted
in v1 ingest.

## Relationships

- ServiceSpecification is at the heart of the Service Domain.
- CFSSpec is bound to ProductSpecification
  ([[wiki/sid/product/product-specification-abe]]) — Service realises Product.
- RFSSpec is bound to ResourceSpecification (Resource Domain — not yet ingested).
- ServiceSpec characteristics relate to ResourceSpec characteristics (Figure SO.22a)
  and to ProductSpec characteristics
  ([[wiki/sid/product/product-specification-abe]] Figure Pr.44a).
- ServicePackage groups CFSSpecs; ServiceBundle aggregates RFSSpecs — note these are
  not interchangeable.
- Service Catalog (sub-ABE §4.3.3) specialises the canonical
  [[wiki/sid/common/catalog-abe]].
— GB922 Service §4.3, pp. 22–83

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-022: Network Service Spec and Usage Volume Service Spec sub-ABEs are tagged
  «Preliminary» by source — content may evolve
