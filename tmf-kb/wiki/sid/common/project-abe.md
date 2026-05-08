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
entity_name: "Project ABE"
---

# Project ABE

## Overview

Represents the tools used by project managers to ensure that enterprise objectives of
quality, cost and time are achieved by planning and scheduling work. It uses common
industry definition of Project, Work Breakdown Structure and Activity to provide
support to project managers. — GB922 Common §4.22, p. 761

The intention of this document is not to try and define a radically different model of
a project, but to provide a generic model, based on current industry best practice that
can be used to link parts of the SID model together.

Unfortunately, there is no industry standard project model that we can adopt, so the
approach of this document is to provide a generic project management model and to
extend that model by SID blades (sub-classing), reflecting specific project management
techniques. — GB922 Common §4.22, p. 761

## Business Entities

§4.22 spans pp. 761–931 (~170 pages — the largest single ABE chapter in this document).
Industry-standard core concepts referenced include:

- **Project** — base entity
- **WorkBreakdownStructure** (WBS) — hierarchical decomposition of project work
- **Activity** — atomic units of work within a WBS
- **ProjectSpec** — EntitySpec side
- Many supporting entities for scheduling, resource assignment, deliverables, milestones

For full BE inventory and figures see source.

> The source notes "Unfortunately, there is no industry standard project model that we
> can adopt" — this ABE is a generic project model that organisations are expected to
> extend ("by SID blades") for their own methodologies (waterfall, agile, etc.).
> — GB922 Common §4.22, p. 761

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Generic enough to relate to almost any other domain entity — projects can deliver
  Products, Services, Resources.
- Schedule relates to Calendar ([[wiki/sid/common/calendar-abe]]) and
  ApplicableTimePeriod / TimePeriod ([[wiki/sid/common/base-types-abe]]).
- Resource assignment relates to Party / PartyRole
  ([[wiki/sid/common/party-abe]]) and Resource entities (Resource Domain — not yet
  ingested).
- Performance tracking via [[wiki/sid/common/performance-abe]] and
  [[wiki/sid/common/metric-abe]].
— GB922 Common §4.22, pp. 761–931

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-020: Project ABE is the largest single chapter (170 pages); v1 ingest is highly
  conceptual — deeper ingest needed for the WBS, Activity, scheduling detail
- OQ-021: Project ABE relevance to current-state operational mapping is uncertain;
  source frames it as a generic model intended for organisational extension. Confirm
  whether it should remain in the corpus or be flagged as out of mapping scope
