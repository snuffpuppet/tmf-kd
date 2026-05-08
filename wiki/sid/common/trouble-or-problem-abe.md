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
entity_name: "Trouble or Problem ABE"
---

# Trouble or Problem ABE

> **Diagram-only ABE.** GB922 Common v23.0 lists Trouble or Problem ABE as a
> top-level Common ABE in the §4.1 [ComD-01] Common ABEs Level 1 diagram with a
> brief one-paragraph description, but provides **no dedicated chapter**. Unlike
> Trouble Ticket and Event, the §4.1 brief does not flag this ABE as "not fully
> developed".

## Overview

A description of a problem that can be shared between the service provider and the
customer. Trouble or Problem is an indication that an entity (such as Resource,
Service or Product) is no longer functioning according to the expected SLA.
— GB922 Common §4.1, p. 43

## Key Attributes

No dedicated §4.x chapter exists in GB922 Common v23.0; key attributes not
published at the Common ABE level. Specialised attributes appear in
[[wiki/sid/service/service-problem-abe]] (Service domain, «NotFullyDeveloped»)
and [[wiki/sid/resource/resource-trouble-abe]] (Resource domain,
«notFullyDeveloped»).

## Relationships

- Specialised by [[wiki/sid/service/service-problem-abe]] for Service-side fault
  management
- Specialised by [[wiki/sid/resource/resource-trouble-abe]] for Resource-side fault
  management
- Records of resolution captured by [[wiki/sid/common/trouble-ticket-abe]]
- Indicates entity (Resource / Service / Product) no longer functioning per
  expected SLA — Agreement modelling in [[wiki/sid/common/agreement-abe]]

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Trouble or Problem ABE not directly mapped in
any ODA Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Trouble or Problem pending.
v25.5 candidates by name are 1.4.6 Service Problem Management and 1.5.8 Resource
Trouble Management, but no source mapping table establishes the link to the Common
parent ABE; specialised links would attach to the domain SID Problem/Trouble ABEs
(see Relationships above) when their sweeps run.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-024: Service Problem ABE «NotFullyDeveloped» — paired production-side fault
  modelling gap
- OQ-031: Resource Trouble ABE «notFullyDeveloped» — paired production-side fault
  modelling gap
- OQ-041: Trouble or Problem ABE ingested as part of v1 Common gap fill;
  diagram-only in source (no §4.x chapter content available)
