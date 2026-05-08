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
entity_name: "Workflow ABE"
release_status: draft
---

# Workflow ABE

> **Source-flagged «Preliminary».** GB922 Common v23.0 §4.29 carries the «Preliminary»
> annotation in its chapter heading. `release_status: draft` set in frontmatter per
> CLAUDE.md §6.

## Overview

Workflow is a business process model, or a generic process model that is made up of
series of business processes or activities that collectively through them a piece
of work passes from initiation to completion.

A workflow ties business processes or activities together in sequence to enable
realize specified objectives. — GB922 Common §4.29, p. 889

## Key Attributes

Source §4.29.1 (Figure WF.01 — Basic Workflow) defines:

- **Workflow** — derived from `RootEntity → Entity`. A Workflow is composed of one
  or more Activities (`AggregatesActivity`).
- **WorkflowSpecification** — derived from `RootEntity → EntitySpecification`.
- **Activity** — atomic unit of work realised by a Workflow (`RealizedBy`).
  ClosedLoopActivity is a specialisation tied to ClosedLoops.

Source §4.29.2 (Figure WF.02 — Detailed Workflow) extends with relationships to
Policy, PartyRole, and Goal.

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.29.1–§4.29.2, pp. 889–891

## Relationships

- **Workflow ↔ WorkflowSpecification** via `SpecifiesWorkflow`
- **Workflow ↔ Goal** via `GoalHas` — see [[wiki/sid/common/goal-abe]]
- **Workflow ↔ Activity** via `AggregatesActivity` (1..* Activities)
- **Activity ↔ ClosedLoop** via `ClosedLoopActivity` — see
  [[wiki/sid/common/closed-loop-abe]]
- **Workflow ↔ Policy** — see [[wiki/sid/common/policy-abe]]
- **Workflow ↔ PartyRole** — PartyRole lives in [[wiki/sid/common/party-abe]]
- Workflow derives from RootEntity / Entity in
  [[wiki/sid/common/root-business-entities-abe]]
— GB922 Common §4.29, pp. 889–891

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Workflow ABE not directly mapped in any ODA
Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Workflow pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Workflow ABE ingested as part of v1 Common gap fill; «Preliminary» in
  source
