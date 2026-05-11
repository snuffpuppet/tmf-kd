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
l1_parent: "1.4 Service Domain"
l2_id: "1.4.19"
l2_name: "Service Specification Management"
---

# Service Specification Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Capability Management ([[wiki/foundations/lifecycle#Capability Management]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). PSR-symmetric with the Resource-side analog [[wiki/etom/resource-domain/resource-specification-management|1.5.19]]. Closes the four Capability Management PSR pairs.

> **Cross-L2 back-reference target.** L3 1.4.16.2 Define Service Catalog Specification (in [[wiki/etom/service-domain/service-catalog-planning-management|Service Catalog Planning Management]]) references "Specification Management business activities" — those activities live here. Specification Management is the lower-level activity-set that Catalog Planning leverages to define catalog field / schema / design-requirement specifications.

## Overview

Service Specification Management business process leverages captured service requirements to develop, master, analyze, and update documented standard conditions that must be satisfied by service design and/or delivery.

Service Specifications Management can result in establishing, in a centralized way, technical (know-how) standards.

Such standards provide the organization with a means to control and approve the values and inputs of service specification through structure, review, approval and distribution processes to stakeholders and suppliers.

— GB921 v25.5 Excel master, process ID `1.4.19`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master.

### 1.4.19.1 Describe Service Specifications

**Extended Description.**

Describe Service Specifications business activity identify and elaborate on the conditions for meeting service requirement for consistency, quality, functionality and fit for purpose.

This activity leverages captured service requirements and resource preferences, and builds in tolerances according to stakeholders for service delivery partners to adhere to.

**L4 sub-processes:**

- **1.4.19.1.1** Describe Service Specifications Property — Set out and develop the rules, constraints, models and framing that bound the principles by which Service Specification can be modeled to support service requirements and the business objectives. A Service Specification Property enumerates all the specification attributes and their units of management.
- **1.4.19.1.2** Align Service Specifications — Alignment of service specification to functional and nonfunctional requirement. The alignment of service specifications can be to other services as well as realization of the specific resource according to business concerns (e.g. cost, other accounting and non-accounting requirements etc.).

> **Source-text observation — modelled/modeled spelling inconsistency on L4 1.4.19.1.1.** Brief uses British "modelled"; ED uses American "modeled". Resource-side analog [[wiki/etom/resource-domain/resource-specification-management#1.5.19.1.1 Describe Resource Specifications Property|1.5.19.1.1]] uses "modelled" consistently in both. Trivial v25.5 source quirk; preserved verbatim per CLAUDE.md §1, §10.3.

### 1.4.19.2 Model Service Specifications

> **Source-text observation — significant copy-paste bug.** The L3 **name** is *"Model **Service** Specifications"* but the brief column begins *"Model **Resource** Specifications business activity…"* and the ED prose begins *"Model **Resource** Specifications business activity represents the understanding of collections of **service** specifications…"* — the body text was copy-pasted from the Resource-side mirror page [[wiki/etom/resource-domain/resource-specification-management#1.5.19.2 Master Resource Specifications|1.5.19.2]] (which is named *"Master Resource Specifications"*) and the PSR substitution was applied incompletely. The verb itself differs too — Resource-side L3 name is *"Master"*; Service-side is *"Model"* — but the body prose carries the Resource-mirror verb pattern. Intent is unambiguously Service Specifications given context (this is 1.4.19.x within 1.4.19 **Service** Specification Management). **Preserved verbatim** per CLAUDE.md §1, §10.3 — same OQ-045-family handling as previous source-text bugs (Resource Anomaly 1.5.21, Service Capacity Report 1.4.12.9). No separate OQ filed.

**Extended Description.**

Model Resource Specifications business activity represents the understanding of collections of service specifications and the relationship dependencies in order to manage dependencies, improvement or evolution of standards that affect overall design and delivery of service.

This business activity is used by organizations to establish a collection of standardized, pre-documented specifications, and their dependencies to guide service lifecycle management and service operations.

_No L4 sub-processes in source._

### 1.4.19.3 Analyze Service Specifications

**Extended Description.**

Analyze Service Specifications business activity research, assess and evaluate performance criteria and factors to develop, master, control/update services according to requirements.

This business activity can include multiple analyzes of service specifications, including standard analysis (based on empirical research) or custom analysis (based on other standards). Analysis of Service Specification include testing service specifications and the ability to meet business requirements, as well as conform to operational mandates.

_No L4 sub-processes in source._

> **PSR-asymmetry note — no Service-side analog for L3 `.4`.** The Resource-side analog L2 [[wiki/etom/resource-domain/resource-specification-management|1.5.19]] has a fourth L3 — **1.5.19.4 Update and Version Resource Specifications** — covering explicit version management of resource specifications (track changes, versioning policies, communicate property changes). The Service-side L2 has **no L3-level version-management analog** — version management for service specifications likely lives in the BVD-vertical [[wiki/etom/service-domain/_index|Service Specification Lifecycle Management]] (1.4.3, pending Phase 3 BVD batch). **Heat-map relevance for transformation roadmap** — explicit version management is a real OSS-modernisation axis; Resource side surfaces it at L3, Service side defers to a separate Lifecycle Management L2 (BVD). Worth a back-reference note when 1.4.3 ingests.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.4.19.1** Describe Service Specifications — Identify and elaborate on the conditions for meeting service requirement for consistency, quality, functionality and fit for purpose.
- **1.4.19.2** Model Service Specifications — Model Resource Specifications business activity represents the understanding of collections of service specifications and the relationship dependencies in order to manage dependencies, improvement or evolution of standards that affect overall design and d _(source brief is truncated at character ~256 in Excel; verbatim preserved. ED prose continues the thought.)_
- **1.4.19.3** Analyze Service Specifications — Research, assess and evaluate performance criteria and factors to develop, master, control/update services according to requirements.

## SID Entities Manipulated

- [[wiki/sid/service/service-specification-abe]] — **primary manipulator**. This L2 *is* the end-to-end specifications-management process; the Service Specification ABE (including CFSSpec / RFSSpec and the §4.3.3 Service Catalog sub-ABE) is its data model. The L2's three L3s describe, model, and analyze service specifications across the full lifecycle of the spec artefact. The same ABE carries existing back-links from Service Capability Delivery (1.4.2, upstream-input — service-infrastructure-design specs from the capability-delivery flow) and Service Catalog Planning Management (1.4.16, catalog-planning-specific — Service Catalog sub-ABE artefacts). This L2 (1.4.19) is the primary specifications-management manipulator; 1.4.2 and 1.4.16 are scope-specific manipulators producing their own specification artefacts within the broader ABE.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Service Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0, so no narrative-PDF supplementation pass is anticipated for this L2 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
