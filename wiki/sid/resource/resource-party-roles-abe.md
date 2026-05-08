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
entity_name: "Resource Party Roles ABE"
---

# Resource Party Roles ABE

> **Pre-production source.** GB922 Resource v25.5 PDF metadata reports
> "Release Status: Pre-production" and "Approval Status: Team Approved" — not the
> standard "Production / TM Forum Approved" of other v25.x SID documents. Ingested
> with explicit user authorisation; treat content with appropriate caution. See
> [[wiki/open-questions#OQ-027]].

## Overview

Resource Party Roles ABE contains all PartyRoles related to the Resource Domain such
as Technician and ResourceManager. — GB922 Resource §4.1, p. 26

## Business Entities

The Resource Domain party roles presently identified are: — GB922 Resource §4.1, p. 26

### Technician

An individual who possesses specific technical training and competence in a specific
area, such as digital services. — GB922 Resource §4.1, p. 26

### ResourceInstaller

An individual who installs PhysicalResources. It specifically doesn't provide all of
the capabilities of a Technician role but also represents a less costly PartyRole.
Specifically, a ResourceInstaller is limited to simple physical installation of
Equipment. A ResourceInstaller does not configure Resources or Services.
— GB922 Resource §4.1, p. 26

### ResourceManager

(Listed in chapter title and overview as a Resource Domain party role; full
description in source §4.1.) — GB922 Resource §4.1, p. 26

## Key Attributes

All roles inherit from `PartyRole` ([[wiki/sid/common/party-abe]]). Detailed attribute
tables not extracted in v1 ingest.

## Relationships

- All entities specialise PartyRole from [[wiki/sid/common/party-abe]].
- Technician/ResourceInstaller relate to Resource entities ([[wiki/sid/resource/resource-abe]]).
- ResourceInstaller is restricted to PhysicalResource installation per the source
  description.

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: GB922 Resource v25.5 source is Pre-production / Team Approved (not Production
  / TM Forum Approved); ingested with user authorisation
