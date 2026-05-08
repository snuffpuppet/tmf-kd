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
entity_name: "Service ABE"
---

# Service ABE

> **Production/commercial relevance.** This ABE contains the **CFS/RFS instance
> separation** — Customer Facing Service (commercial layer) vs Resource Facing
> Service (production layer). The source explicitly notes that aggregating across
> these is "a bad idea, as it enables ResourceFacingServices to aggregate
> CustomerFacingServices, which destroys the point of separating them in the first
> place." This separation is central to the corpus's PSR mapping goal.

## Overview

A Service represents an instance of ServiceSpecification. The Service ABE contains
entities that are used to represent both types of Services: CSP Know-Hows instances
(a.k.a. Customer Facing Services or CFS) and Technical solution (a.k.a. Resource
Facing Services or RFS). — GB922 Service §4.4, p. 84

The Service carries the place where the Service is in use if relevant, as well as
configuration characteristics, such as assigned telephone numbers and internet
addresses. The Service also tracks the links to Product realized and/or Resources
used. — GB922 Service §4.4, p. 84

> A ComprisedOf recursive association on Service is tempting to add, because it
> defines the ability to aggregate subordinate Services into a higher-level Service.
> However, this aggregation is a bad idea, as it enables ResourceFacingServices to
> aggregate CustomerFacingServices, which destroys the point of separating them in
> the first place. Hence, it will not be defined in this model.
>
> Specifically, a CustomerFacingService is what is bound to a Product, not a Service.
> ResourceFacingService is not linked directly to Product; rather, it is linked to
> Resource. — GB922 Service §4.4, p. 84

## Business Entities

### Service (abstract)

Base instance of ServiceSpecification. — GB922 Service §4.4, p. 84

### CustomerFacingService (CFS)

Customer-facing service instance, bound to a Product
([[wiki/sid/product/product-and-offering-instance-abe]]). Commercial-layer entity in
the production/commercial separation. — GB922 Service §4.4, p. 84

### ResourceFacingService (RFS)

Technical/network-facing service instance, linked to Resource (Resource Domain — not
yet ingested). Production-layer entity. — GB922 Service §4.4, p. 84

### ServiceRole

Role classification, paralleling ServiceSpecificationRole.
— GB922 Service §4.4 (Figure SO.20)

## Sub-ABEs

§4.4 contains nested sub-ABEs:

- §4.4.1 **Customer Facing Service ABE** (p. 101) — with §4.4.1.1 Example,
  §4.4.1.2 Role, §4.4.1.3 Network Service («Preliminary»), §4.4.1.4 Usage Volume
  Service («Preliminary»)
- §4.4.2 **Resource Facing Service ABE** (p. 105) — with §4.4.2.1 Examples,
  §4.4.2.2 Role

## Key Attributes

Service inherits from Entity ([[wiki/sid/common/root-business-entities-abe]]). The
Service carries place, configuration characteristics (e.g. assigned phone numbers,
internet addresses). Detailed attribute tables not extracted in v1 ingest.

## Relationships

- Service is an instance of ServiceSpecification
  ([[wiki/sid/service/service-specification-abe]]).
- **CFS is bound to Product** ([[wiki/sid/product/product-and-offering-instance-abe]]).
- **RFS is linked to Resource** (Resource Domain — not yet ingested).
- Service relates to PartyRole ([[wiki/sid/common/party-abe]]) — Figure SO.35.
- Service relates to Place / Location ([[wiki/sid/common/location-abe]]) — Figure
  SO.36.
- NetworkServiceSpec and UsageVolumeServiceSpec instantiate as NetworkService and
  UsageVolumeService respectively — Figure SO.37.
— GB922 Service §4.4, pp. 84–108

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-022: Network Service and Usage Volume Service tagged «Preliminary»
