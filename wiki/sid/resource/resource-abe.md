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
entity_name: "Resource ABE"
---

# Resource ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].
>
> **Production-side relevance.** Resource entities are the production/network-facing
> data layer that ResourceFacingService (RFS in
> [[wiki/sid/service/service-abe]]) consumes. This is the "production" side of the
> production/commercial separation the corpus's PSR goal targets.

## Overview

A Resource represents an instance of ResourceSpecification. The Resource ABE contains
entities that are used to represent the three types of Resources: Logical, Physical
and Compound Resources.

The Resource carries the place where the Resource is installed, as well as
configuration characteristics, such as assigned telephone numbers and internet
addresses. The Resource also tracks the links to Product and/or Service realized.
— GB922 Resource §4.3, p. 139

> Resources are physical or non-physical components (or some combination of these)
> within an enterprise's infrastructure or inventory. They are typically consumed or
> used by Services (for example a physical port assigned to a service) or contribute
> to the realization of a Product (for example, a SIM card). They can be drawn from
> the Application, Computing and Network domains, and include, for example, network
> elements, software, IT systems, content and information, and technology components.
> — GB922 Resource §4.3, p. 139

## Business Entities

### Resource (abstract)

Base instance of ResourceSpecification.

### LogicalResource

Non-physical resource instance (e.g. IP address, account, software state).

### PhysicalResource

Physical resource instance (e.g. equipment, SIM card, port).

### CompoundResource

Composite resource (e.g. networked device with firmware — combines Logical and
Physical). — GB922 Resource §4.3 (Figure LR.04)

## Sub-ABEs

§4.3 spans pp. 139–238 (100 pages) and contains extensive sub-ABEs:

- §4.3.1 **Compound Resource ABE** (p. 239)
- §4.3.2 **Computing and Software Addendum** (p. 240) — including scenarios
- §4.3.3 **Logical Resource ABE** (p. 274) — major nested structure:
  - §4.3.3.1 Address ABE (p. 276)
  - §4.3.3.2 AI Model ABE (p. 278)
  - §4.3.3.3 Computing and Software ABE (p. 282) — and Software Resource sub-sub-ABE
  - §4.3.3.4 LogicalResource Examples ABE «doNotImplement» (p. 284)
  - §4.3.3.5 Management Information ABE (p. 286) — with sub-sub-ABEs:
    - Accounting ABE (p. 287)
    - Management Method ABE (p. 288)
    - Performance Info ABE (p. 290)
    - Resource State ABE (p. 291)
    - Resource Statistical ABE (p. 292)

Per CLAUDE.md §5.2 v1 granularity, sub-ABEs are documented at this overview level.

## Key Attributes

Resource carries:
- `place` — where the Resource is installed
- Configuration characteristics — e.g. assigned phone numbers, internet addresses

Detailed attribute tables and the full hierarchy are in source.

## Relationships

- Resource is an instance of ResourceSpecification
  ([[wiki/sid/resource/resource-specification-abe]]).
- **ResourceFacingService binds to Resources** ([[wiki/sid/service/service-abe]]) —
  the production-side coupling.
- Resources can also relate directly to Products
  ([[wiki/sid/product/product-and-offering-instance-abe]]) — e.g. a SIM card as part
  of a Product.
- Resource location relates to Place / GeographicAddress
  ([[wiki/sid/common/location-abe]]).
- Resource configuration relates to
  [[wiki/sid/resource/resource-configuration-abe]].
- Compound Resource may contain Logical and Physical Resources.
- AI Model entities are a distinct LogicalResource subtype.
— GB922 Resource §4.3, pp. 139–333

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-027: Pre-production source release status
- OQ-028: §4.3.3.4 LogicalResource Examples ABE source-tagged «doNotImplement»
- OQ-029: §4.3 contains a substantial Computing and Software Addendum (pp. 240–273)
  with detailed scenarios. v1 ingest covers structural placement only; deepening
  recommended if computing/software resource mapping becomes important.
