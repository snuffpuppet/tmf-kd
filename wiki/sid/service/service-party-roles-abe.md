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
entity_name: "Service Party Roles ABE"
---

# Service Party Roles ABE

## Overview

The Service Party Roles ABE contains all PartyRoles related to the Service Domain such
as ServiceManager. — GB922 Service §4.2, p. 21

## Business Entities

The Service Domain party roles presently identified are: — GB922 Service §4.2, p. 21

### ServiceDesigner

A ServiceDesigner is a party role which is responsible for the design of the Service
Provider' know-how (CustomerFacingServiceSpecs). To be valid a know-how needs to align
with one or more technical solutions (ResourceFacingServiceSpec or Supplier's
ProductSpec). — GB922 Service §4.2, p. 21

### TechnicalSolutionDesigner

A TechnicalSolutionDesigner is a party role which is responsible for the design of
technical solutions (ResourceFacingServiceSpec). To be valid a technical solution needs
to align with one or more Resources (ResourceSpec or Supplier's ProductSpec).
— GB922 Service §4.2, p. 21

## Key Attributes

Both roles inherit from `PartyRole` defined in
[[wiki/sid/common/party-abe]]. Detailed attribute tables not extracted in v1
ingest; consult source.

## Relationships

- Both roles specialise PartyRole from [[wiki/sid/common/party-abe]].
- ServiceDesigner relates to CustomerFacingServiceSpec
  ([[wiki/sid/service/service-specification-abe]]).
- TechnicalSolutionDesigner relates to ResourceFacingServiceSpec
  ([[wiki/sid/service/service-specification-abe]]) and ResourceSpec (Resource Domain,
  not yet ingested).
— GB922 Service §4.2, p. 21

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
