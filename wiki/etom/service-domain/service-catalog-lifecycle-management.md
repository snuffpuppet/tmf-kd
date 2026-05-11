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
l2_id: "1.4.13"
l2_name: "Service Catalog Lifecycle Management"
---

# Service Catalog Lifecycle Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Business Value Development ([[wiki/foundations/lifecycle#Business Value Development]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). **Different from the first BVD PSR pair** (1.4.3 + 1.5.3 Specification Lifecycle Management) which had R20.5 lineage — BVD batch is not uniformly R20.5-lineage; Catalog Lifecycle Management is a v25.5 introduction. PSR-symmetric with the Resource-side analog [[wiki/etom/resource-domain/resource-catalog-lifecycle-management|1.5.15]].

> **Completes the four-L2 Catalog lifecycle.** This L2 is the *Business Value Development* stage of v25.5's four-stage Catalog lifecycle (visible across both view pages):
>
> - **Planning** (S2R-CM) — [[wiki/etom/service-domain/service-catalog-planning-management|1.4.16 Service Catalog Planning Management]] (design the catalog specifications)
> - **Lifecycle (this L2)** (S2R-BVD) — 1.4.13 (design / build / policy of catalog over its implementation lifecycle)
> - **Operational Readiness** (Ops-ORS) — [[wiki/etom/service-domain/service-catalog-operational-readiness-management|1.4.14]]
> - **Content** (Ops-ORS) — [[wiki/etom/service-domain/service-catalog-content-management|1.4.15]]

## Overview

> **Source-text observation — PSR-agnostic L2 ED.** The L2 Extended Description is **literally identical to the Resource-side analog 1.5.15** — neither *"Service"* nor *"Resource"* appears in either ED; both reference *"Product/Service/Resource Catalog"* generically. **First PSR pair in Phase 3 with completely PSR-agnostic L2 EDs.** v25.5 appears to treat Catalog Lifecycle Management as a domain-agnostic governance pattern that applies uniformly across PSR — only the L3 names carry PSR qualifiers. Preserved verbatim per CLAUDE.md §1, §10.3.

Catalog Lifecycle Management business process covers a set of business activities that enable manage the lifecycle of an organizations catalog from design to build according to defined requirements.

Catalog Lifecycle Management proves the overarching governance to manage all the stages in the realization and operationalization of the Product/Service/Resource Catalog in support of the organizations business goals.

— GB921 v25.5 Excel master, process ID `1.4.13`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

> **Source-text observation — L3-body-text mis-targeting cluster.** Each L3 on this L2 carries body text (brief + ED) that references the **wrong sub-process name** — shifted by one position from the L3's actual name. Specifically:
>
> - L3 1.4.13.1 (named *"Manage Service Catalog Design"*) — body says *"Manage Catalog **Design**…"* ✓ correct
> - L3 1.4.13.2 (named *"Manage Service Catalog Build"*) — body says *"Manage Catalog **Design**…"* ❌ should say "Build"
> - L3 1.4.13.3 (named *"Manage Service Catalog Policy"*) — body says *"Manage Catalog **Build**…"* ❌ should say "Policy"
>
> **Three source-text bugs on this side; the Resource-side analog [[wiki/etom/resource-domain/resource-catalog-lifecycle-management|1.5.15]] carries the parallel cluster (3 more bugs). Six bugs total across the PSR pair — most prominent source-text inconsistency cluster in Phase 3.** L3 names are correct; L3 body text was clearly shifted forward by one position during authoring. L3 .3's body content (catalog *governance* for operations readiness) is plausibly correct-for-Policy; less clear for L3 .2. **Preserved verbatim** per CLAUDE.md §1, §10.3 — same OQ-045-family handling as previous source-text bugs (Resource Anomaly 1.5.21, Service Capacity Report 1.4.12.9, Model Service Specifications 1.4.19.2). No separate OQ filed.
>
> **Also: PSR-qualifier-omitted-from-body pattern.** All L3 body text omits the "Service" qualifier present in the L3 names (says "Catalog Design" rather than "Service Catalog Design"). Same family as the 1.4.16.1 / 1.5.18.1 extra-qualifier-word quirk from Catalog Planning — Catalog L2s on both sides share an abbreviated-body convention.

### 1.4.13.1 Manage Service Catalog Design

**Extended Description.**

Manage Catalog Design business activity cover the design of the Catalog in accordance to the Catalog Management Lifecycle.

Manage Catalog Design business activity will leverage Catalog Specification requirement for all information (features, attributes etc.) to be managed by the catalog in order to enable support the Catalog Lifecycle Management.

> **Cross-L2 back-reference — Catalog Specification.** The second paragraph references "Catalog Specification requirement" — produced by L3 1.4.16.2 Define Service Catalog Specification (in [[wiki/etom/service-domain/service-catalog-planning-management|Service Catalog Planning Management]]). This is the documented hand-off from Catalog Planning (S2R-CM) → Catalog Lifecycle (S2R-BVD) within the four-L2 Catalog lifecycle.

_No L4 sub-processes in source._

### 1.4.13.2 Manage Service Catalog Build

**Extended Description.**

Manage Catalog Design business activity covers the design of the Catalog in accordance to the Catalog Management Lifecycle.

This business activity leverages input from the Catalog Design to construct the product/service/resource Catalog in order to meet the business operations goals.

> **Source-text mis-targeting.** ED opens "Manage Catalog **Design** business activity covers the design of the Catalog" — but this L3 is named "Manage Service Catalog **Build**". The first sentence carries the L3 .1 activity name; the second sentence's content (constructing the catalog using Catalog Design input) is plausibly Build-correct. **Verbatim preserved**; flagged in the section-level callout above.

_No L4 sub-processes in source._

### 1.4.13.3 Manage Service Catalog Policy

**Extended Description.**

Manage Catalog Build business activity establishes, manages and administers the governing of the catalog for operations readiness and operations.

This business activity leverages support of the Enterprise governance processes for product/service/resource catalog lifecycle management.

> **Source-text mis-targeting.** ED opens "Manage Catalog **Build** business activity establishes, manages and administers the governing of the catalog" — but this L3 is named "Manage Service Catalog **Policy**". The first sentence carries the L3 .2 activity name; the content (governance for operations readiness) is plausibly Policy-correct. **Verbatim preserved**; flagged in the section-level callout above.
>
> **Forward reference — Enterprise governance processes.** The second paragraph references "Enterprise governance processes for product/service/resource catalog lifecycle management" — Enterprise-domain content, out of L1 scope per CLAUDE.md §3. Pattern matches the "Enterprise Business Process for Catalog Management" reference from L3 1.4.16.2 / 1.5.18.2 in Catalog Planning.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.4.13.1** Manage Service Catalog Design — Cover the design of the Catalog in accordance to the Catalog Management Lifecycle.
- **1.4.13.2** Manage Service Catalog Build — _(source brief: "Manage Catalog **Design** business activity covers the design of the Catalog in accordance to the Catalog Management Lifecycle." — source-text mis-targeted; verbatim preserved.)_
- **1.4.13.3** Manage Service Catalog Policy — _(source brief: "Manage Catalog **Build** business activity establishes, manages and administers the governing of the catalog for operations readiness and operations." — source-text mis-targeted; verbatim preserved.)_

## SID Entities Manipulated

- [[wiki/sid/service/service-specification-abe]] — catalog-implementation-lifecycle manipulator. The L2 manages the implementation lifecycle of the catalog itself (design → build → policy) — produces the catalog-system implementations that populate the §4.3.3 Service Catalog sub-ABE. Distinct from Catalog Planning (1.4.16), which produces catalog *specifications*; this L2 produces catalog *implementations* against those specs. After this ingest, the ABE carries **five eTOM back-links** ordered by manipulator role: primary specifications-management (1.4.19, ongoing-maintenance) + capability-delivery upstream-input (1.4.2, project-driven-design) + catalog-planning (1.4.16, catalog-system-design) + specification-lifecycle (1.4.3, class-introduction-to-retirement) + **this L2's catalog-implementation-lifecycle (1.4.13)**. **Densest trilateral pattern in the corpus extended** — five discrete manipulator-role-cells on the same SID artefact, all source-grounded.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables. Same hard gap as Capability Management batch's net-new L2s (in contrast to the first BVD PSR pair 1.4.3 / 1.5.3 which had R20.5 lineage and a softer ODA gap).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Service Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
