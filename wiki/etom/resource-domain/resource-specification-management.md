---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-11
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.19"
l2_name: "Resource Specification Management"
---

# Resource Specification Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Capability Management ([[wiki/foundations/lifecycle#Capability Management]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). PSR-symmetric with the Service-side analog [[wiki/etom/service-domain/service-specification-management|1.4.19]] in net-new-in-v25.5 status; **asymmetric at L3 level** — this Resource L2 carries an extra L3 (`.4 Update and Version Resource Specifications`) that has no Service-side counterpart.

> **Cross-L2 back-reference target.** L3 1.5.18.2 Define Resource Catalog Specification (in [[wiki/etom/resource-domain/resource-catalog-planning-management|Resource Catalog Planning Management]]) references "Specification Management business activities" — those activities live here. Specification Management is the lower-level activity-set that Catalog Planning leverages.

## Overview

Resource Specification Management business process leverages captured resource requirements to develop, master, analyze, and update documented standard conditions that must be satisfied by a resource design and/or delivery.

Resource Specifications Management can result in establishing in a centralized way, technical (know-how) standards. Such standards provide the organization with a means to control and approve the values and inputs of specification through structure, review, approval and distribution processes to stakeholders and suppliers.

— GB921 v25.5 Excel master, process ID `1.5.19`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master.

### 1.5.19.1 Develop Resource Specifications

**Extended Description.**

Develop Resource Specification business activity define and elaborate on the conditions for meeting resource requirement for consistency, quality, functionality and fit for purpose.

This activity leverages captured resource requirements and resource preferences and builds in tolerances according to stakeholders for suppliers to adhere to.

**L4 sub-processes:**

- **1.5.19.1.1** Describe Resource Specifications Property — Set out and develop the frames, rules, constraints, models and the set of principles on which the resource specifications can be modelled according to resource requirements.
- **1.5.19.1.2** Align Resource Specifications — Alignment of resources specification to functional and nonfunctional requirements. The alignment of resource specifications can be to other resources as well as realization of the specific resource according to business concerns (e.g. cost, other accounting and non-accounting requirements etc.).

> **PSR naming-asymmetry note vs Service-side L3 1.4.19.1.** Resource L3 verb is *"Develop"*; Service L3 verb is *"Describe"*. "Develop" is creation-focused; "Describe" is documentation-focused. Slight scope difference at the L3-name level; both L2s describe their L3 `.1` activity as "define / identify and elaborate on the conditions for meeting requirements." Preserved verbatim per naming-asymmetry convention.

### 1.5.19.2 Master Resource Specifications

**Extended Description.**

Master Resource Specifications business activity learn and understand the collection of resource specifications in order to manage improvement or evolution of standards that will used for design and construction of resource.

This business activity is used by organizations to establish a collection of standardized, pre-written specifications or guide specifications that can be used by resource designers, resource architects, and other resource construction entities.

_No L4 sub-processes in source._

> **PSR naming-asymmetry note vs Service-side L3 1.4.19.2.** Resource L3 verb is *"Master"*; Service L3 verb is *"Model"*. "Master" is curatorial / ownership-focused (the activity name in the ED prose); "Model" is representational-focused (the verb on the Service-side L3-name line). The Service-side ED prose carries a copy-paste bug — it opens with the Resource-mirror verb pattern "Model **Resource** Specifications business activity represents the understanding of collections of **service** specifications…" — see [[wiki/etom/service-domain/service-specification-management#1.4.19.2 Model Service Specifications|1.4.19.2]] for the source-text observation. The Resource-side L3 here is the *intact* version of the activity description.

### 1.5.19.3 Analyze Resource Specifications

**Extended Description.**

Analyze Resource Specifications business activity research, assess and evaluate performance criteria and factors to develop, master, control/update resource specifications for resource requirement adherence.

This business activity can include multiple analyzes of resources specifications, including standard analysis (based on empirical research) or custom analysis (based on other standards). Analysis of Resource Specification include testing Resource specifications and the ability to meet business requirements, as well as conform to operational mandates.

_No L4 sub-processes in source._

### 1.5.19.4 Update and Version Resource Specifications

> **PSR-asymmetric — Resource-only L3 with no Service-side analog.** GB921 v25.5 explicitly carries this L3 only on the Resource side. The Service-side L2 [[wiki/etom/service-domain/service-specification-management|1.4.19]] has 3 L3s (no `.4`); this Resource L2 has 4. Version management for service specifications likely lives in the BVD-vertical Service Specification Lifecycle Management (1.4.3, pending Phase 3 BVD batch). **Heat-map relevance for transformation roadmap** — explicit version-management treatment at L3 level is a real OSS-modernisation axis; Resource side surfaces it here, Service side defers to a separate Lifecycle L2.

**Extended Description.**

Update and Version Resource Specifications business activity update and track changes to existing resource specifications according to versioning policies to support requirement management.

This business activity manages all changes to resource specifications over their lifecycle. Resource specification versioning is an effective means to communicate changes to resource specifications, so that resource planners and consumers know what to expect. It includes communicating when changes are made to resource specification properties.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.19.1** Develop Resource Specifications — Define and elaborate on the conditions for meeting resource requirement for consistency, quality, functionality and fit for purpose.
- **1.5.19.2** Master Resource Specifications — Learn and understand the collection of resource specifications in order to manage improvement or evolution of standards that will used for design and construction of resource.
- **1.5.19.3** Analyze Resource Specifications — Research, assess and evaluate performance criteria and factors to develop, master, control/update resource specifications for resource requirement adherence.
- **1.5.19.4** Update and Version Resource Specifications — Update and track changes to existing resource specifications according to versioning policies to support requirement management. _(PSR-asymmetric — Resource-only L3; no Service-side counterpart in 1.4.19.)_

## SID Entities Manipulated

- [[wiki/sid/resource/resource-specification-abe]] — **primary manipulator**. This L2 is the end-to-end specifications-management process; the Resource Specification ABE (Physical / Logical / Compound ResourceSpec subtypes and the §4.2.5 Resource Catalog sub-ABE) is its data model. The L2's four L3s develop, master, analyze, and version-manage resource specifications across the full lifecycle of the spec artefact. The same ABE carries existing back-links from Resource Capability Delivery (1.5.2, upstream-input — resource-infrastructure-design specs from the capability-delivery flow, including legacy-vs-new integration design) and Resource Catalog Planning Management (1.5.18, catalog-planning-specific — Resource Catalog sub-ABE artefacts). This L2 (1.5.19) is the primary specifications-management manipulator; 1.5.2 and 1.5.18 are scope-specific manipulators. Target ABE is `release_status: pre-production` per [[wiki/open-questions#OQ-027]].

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0, so no narrative-PDF supplementation pass is anticipated for this L2 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
