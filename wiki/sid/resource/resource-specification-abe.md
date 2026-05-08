---
type: sid-abe
spec_id: GB922
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Resource_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Resource_v25.5.md
authority: primary
release_status: pre-production
abe_category: resource
entity_name: "Resource Specification ABE"
---

# Resource Specification ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Specification ABE contains entities that define the shared
characteristics and behavior of each of the three types of Resource entities. This
enables multiple instances to be derived from a single specification entity. In this
derivation, each instance will use the shared characteristics and behavior defined in
its associated template.

A ResourceSpecification might be Physical such as a handset, Logical such as an IP
address or Compound i.e. composed of Logical and / or Physical Resources such as a Box
with its firmware. — GB922 Resource §4.2, p. 28

ResourceSpecification is an abstract base class that is used to define the invariant
characteristics and behavior (attributes, methods, constraints, and relationships) of
a managed or unmanaged Resource. — GB922 Resource §4.2, p. 28

## Business Entities

### ResourceSpecification (abstract)

Base class for all Resource specifications. Specialised into Physical, Logical, and
Compound. — GB922 Resource §4.2 (Figure Res.01)

### LogicalResourceSpecification

Specialisation for non-physical resources (e.g. IP address, configuration).
— GB922 Resource §4.2 (Figure Res.01)

### PhysicalResourceSpecification

Specialisation for physical/tangible resources (e.g. handset, equipment).
— GB922 Resource §4.2 (Figure Res.01)

### CompoundResourceSpecification

Specialisation composed of Logical and/or Physical Resources (e.g. a Box with
firmware). — GB922 Resource §4.2 (Figure Res.01)

## Sub-ABEs

§4.2 contains substantial nested sub-ABEs (per source TOC):

- §4.2.1 The Firewall Example (illustrative, p. 78)
- §4.2.2 **Compound Resource Specification ABE** (p. 121)
- §4.2.3 **Logical Resource Specification ABE** (p. 122) — including:
  - §4.2.3.1 AI Model Specification ABE (p. 123)
  - §4.2.3.2 Logical Role Specification ABE (p. 131)
  - §4.2.3.3 LogicalResource Spec Examples ABE «doNotImplement» (p. 132)
  - §4.2.3.4 Software Resource and Software Specifications ABE (p. 133)
- §4.2.4 **PhysicalResource Specification ABE** (p. 136) — including:
  - §4.2.4.1 Physical Role Specification ABE (p. 137)
- §4.2.5 **Resource Catalog ABE** (p. 138)

§4.2 spans pp. 28–138 (110 pages). Sub-ABEs documented at this overview level only.

## Key Attributes

ResourceSpecification inherits from EntitySpecification
([[wiki/sid/common/root-business-entities-abe]]). Detailed attribute tables not
extracted in v1 ingest.

## Relationships

- ResourceSpecification is bound to ResourceFacingServiceSpec
  ([[wiki/sid/service/service-specification-abe]]) — RFSSpec consumes Resources to
  realize Services.
- Resource Catalog (§4.2.5) specialises canonical
  [[wiki/sid/common/catalog-abe]].
- AI Model Specification — distinct sub-ABE for AI/ML model specifications.
- Software Resource and Software Specifications — for software-as-resource modelling.
— GB922 Resource §4.2, pp. 28–138

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-027: Pre-production source release status
- OQ-028: §4.2.3.3 LogicalResource Spec Examples ABE source-tagged «doNotImplement»;
  preserved for completeness
