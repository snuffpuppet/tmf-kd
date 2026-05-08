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
entity_name: "Goal ABE"
release_status: draft
---

# Goal ABE

> **Source-flagged «Preliminary».** GB922 Common v23.0 §4.28 carries the «Preliminary»
> annotation in its chapter heading. `release_status: draft` set in frontmatter per
> CLAUDE.md §6.

## Overview

Goal ABE represents a set of information that captures the definition of a goal or
target for a process (task/activity/workflow/etc.) to reach or achieve.

Goals trigger and guide behavior help to guide focus and enable sustain momentum.
Goals are needed to give direction, identify what's important, measure progress
towards success, foster motivation, assure accountability, and assert control.

There is a distinction between Goal and Metric. This ABE is intended to reflect that
distinction, as well as address the need for both. While a GOAL captures information
about a target, a METRIC provides the yardstick or unit of measuring such
achievement. Goal and Metric work hand-in-hand and each can be managed and modeled
independently to bring flexibility to automation. The importance of this ABE is to
capture the essence of dynamic goal setup and updates, which is key to enabler
higher levels of goals management and goals management automation.
— GB922 Common §4.28, p. 884

## Key Attributes

Source §4.28.1 (Figure G.01 — Basic Goal) defines:

- **Goal** — derived from `RootEntity → Entity`. Attributes include `state:
  String`, `validFor: TimePeriod`, `creationDate: DateTime`. A goal is a managed
  entity that has a lifecycle and can be specified. Goals may be synthesized as
  declarative or imperative (procedural) statements.
- **GoalSpecification** — derived from `RootEntity → EntitySpecification`.

Source §4.28.2 (Figure G.02 — Detailed Goal) adds:

- **GoalDirection:** `from: String`, `to: String`, `validFor: TimePeriod`,
  «required» `creationDate: DateTime` — sets a direction for a Goal (e.g. "Increase
  Sales", "Reduce Cost").
- **GoalInstrument:** `validFor: TimePeriod`, «required» `creationDate: DateTime`
- **GoalPartyRole:** `creationDate: DateTime` — establishes a goal/owner via a
  PartyRole
- **GoalMetric** — tracks achievement of goal via MetricDefinition
- **GoalModel:** `validFor: TimePeriod` — sets relationship model of goal

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.28.1–§4.28.2, pp. 884–887

## Relationships

- **Goal ↔ GoalSpecification** via `SpecifiesGoal`
- **Goal ↔ MetricDefinition** via `tracksAchievementOfGoal` (`GoalMetric`
  association class) — see [[wiki/sid/common/metric-abe]]
- **Goal ↔ ClosedLoop** — see [[wiki/sid/common/closed-loop-abe]]
- **Goal ↔ Workflow** via `GoalHas` — see [[wiki/sid/common/workflow-abe]]
- **Goal ↔ PartyRole** via `EstablishesGoal/Owner` (`GoalPartyRole` association
  class) — PartyRole lives in [[wiki/sid/common/party-abe]]
- Both Goal and GoalSpecification derive from RootEntity / Entity /
  EntitySpecification in
  [[wiki/sid/common/root-business-entities-abe]]
— GB922 Common §4.28, pp. 884–887

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Goal ABE not directly mapped in any ODA
Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Goal pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Goal ABE ingested as part of v1 Common gap fill; «Preliminary» in source
