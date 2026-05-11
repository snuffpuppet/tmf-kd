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
l2_id: "1.5.15"
l2_name: "Resource Catalog Lifecycle Management"
---

# Resource Catalog Lifecycle Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Business Value Development ([[wiki/foundations/lifecycle#Business Value Development]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). PSR-symmetric with [[wiki/etom/service-domain/service-catalog-lifecycle-management|Service-side 1.4.13]]. Different from the first BVD PSR pair (1.4.3 / 1.5.3 Specification Lifecycle Management, R20.5 lineage); Catalog Lifecycle is a v25.5 introduction.

> **Completes the four-L2 Catalog lifecycle (Resource side).** This L2 is the *Business Value Development* stage of v25.5's four-stage Resource Catalog lifecycle:
>
> - **Planning** (S2R-CM) — [[wiki/etom/resource-domain/resource-catalog-planning-management|1.5.18 Resource Catalog Planning Management]]
> - **Lifecycle (this L2)** (S2R-BVD) — 1.5.15
> - **Operational Readiness** (Ops-ORS) — [[wiki/etom/resource-domain/resource-catalog-operational-readiness-management|1.5.16]]
> - **Content** (Ops-ORS) — [[wiki/etom/resource-domain/resource-catalog-content-management|1.5.17]]

## Overview

> **Source-text observation — PSR-agnostic L2 ED.** This L2's Extended Description is **literally identical to the Service-side analog 1.4.13** — neither *"Service"* nor *"Resource"* appears in either ED; both reference *"Product/Service/Resource Catalog"* generically. First PSR pair in Phase 3 with completely PSR-agnostic L2 EDs. v25.5 treats Catalog Lifecycle Management as a domain-agnostic governance pattern that applies uniformly across PSR — only the L3 names carry PSR qualifiers. Preserved verbatim.

Catalog Lifecycle Management business process covers a set of business activities that enable manage the lifecycle of an organizations catalog from design to build according to defined requirements.

Catalog Lifecycle Management proves the overarching governance to manage all the stages in the realization and operationalization of the Product/Service/Resource Catalog in support of the organizations business goals.

— GB921 v25.5 Excel master, process ID `1.5.15`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

> **Source-text observation — L3-body-text mis-targeting cluster.** Each L3 carries body text (brief + ED) referencing the **wrong sub-process name** — shifted by one position from the L3's actual name:
>
> - L3 1.5.15.1 (named *"Manage Resource Catalog Design"*) — body says *"Manage Catalog **Design**…"* ✓ correct
> - L3 1.5.15.2 (named *"Manage Resource Catalog Build"*) — body says *"Manage Catalog **Design**…"* ❌ should say "Build"
> - L3 1.5.15.3 (named *"Manage Resource Catalog Policy"*) — body says *"Manage Catalog **Build**…"* ❌ should say "Policy"
>
> **Three source-text bugs on this side; PSR-symmetric with the Service-side analog 1.4.13 which carries the parallel cluster (six bugs total across the PSR pair — most prominent source-text inconsistency cluster in Phase 3).** Preserved verbatim per CLAUDE.md §1, §10.3; OQ-045-family handling; no separate OQ filed.
>
> **PSR-qualifier-omitted-from-body pattern** — all L3 body text omits the "Resource" qualifier (says "Catalog Design" rather than "Resource Catalog Design"). Same family as the Catalog Planning 1.4.16.1 / 1.5.18.1 quirk — Catalog L2s share an abbreviated-body convention across both PSR sides.

### 1.5.15.1 Manage Resource Catalog Design

**Extended Description.**

Manage Catalog Design business activity cover the design of the Catalog in accordance to the Catalog Management Lifecycle.

Manage Catalog Design business activity will leverage Catalog Specification requirement for all information (features, attributes etc.) to be managed by the catalog in order to enable support the Catalog Lifecycle Management

> **Cross-L2 back-reference — Catalog Specification.** References "Catalog Specification requirement" — produced by L3 1.5.18.2 Define Resource Catalog Specification (in [[wiki/etom/resource-domain/resource-catalog-planning-management|Resource Catalog Planning Management]]). Documented hand-off Catalog Planning (S2R-CM) → Catalog Lifecycle (S2R-BVD) on the Resource side.

_No L4 sub-processes in source._

### 1.5.15.2 Manage Resource Catalog Build

**Extended Description.**

Manage Catalog Design business activity covers the design of the Catalog in accordance to the Catalog Management Lifecycle.

This business activity leverages input from the Catalog Design to construct the product/service/resource Catalog in order to meet the business operations goals.

> **Source-text mis-targeting.** ED opens "Manage Catalog **Design** business activity" — but this L3 is named "Manage Resource Catalog **Build**". Same mis-targeting pattern as Service-side 1.4.13.2. **Verbatim preserved**; flagged in section-level callout above.

_No L4 sub-processes in source._

### 1.5.15.3 Manage Resource Catalog Policy

**Extended Description.**

Manage Catalog Build business activity establishes, manages and administers the governing of the catalog for operations readiness and operations.

This business activity leverages support of the Enterprise governance processes for product/service/resource catalog lifecycle management.

> **Source-text mis-targeting.** ED opens "Manage Catalog **Build** business activity" — but this L3 is named "Manage Resource Catalog **Policy**". Same mis-targeting pattern as Service-side 1.4.13.3. **Verbatim preserved.**
>
> **Forward reference — Enterprise governance processes.** Same Enterprise-domain governance reference as Service-side 1.4.13.3 and as the Catalog Planning forward references — out of L1 scope per CLAUDE.md §3.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.15.1** Manage Resource Catalog Design — Cover the design of the Catalog in accordance to the Catalog Management Lifecycle.
- **1.5.15.2** Manage Resource Catalog Build — _(source brief: "Manage Catalog **Design** business activity covers the design of the Catalog in accordance to the Catalog Management Lifecycle." — source-text mis-targeted; verbatim preserved.)_
- **1.5.15.3** Manage Resource Catalog Policy — _(source brief: "Manage Catalog **Build** business activity establishes, manages and administers the governing of the catalog for operations readiness and operations." — source-text mis-targeted; verbatim preserved.)_

## SID Entities Manipulated

- [[wiki/sid/resource/resource-specification-abe]] — catalog-implementation-lifecycle manipulator. The L2 manages the implementation lifecycle of the catalog itself (design → build → policy) — produces the catalog-system implementations that populate the §4.2.5 Resource Catalog sub-ABE. Distinct from Resource Catalog Planning (1.5.18), which produces catalog *specifications*; this L2 produces catalog *implementations* against those specs. After this ingest, the ABE carries **five eTOM back-links** ordered by manipulator role: primary specifications-management (1.5.19) + capability-delivery (1.5.2) + catalog-planning (1.5.18) + specification-lifecycle (1.5.3) + **this L2's catalog-implementation-lifecycle (1.5.15)**. **Densest trilateral pattern in the corpus extended** to five back-links per side, paralleling the Service-side. Target ABE is `release_status: pre-production` per [[wiki/open-questions#OQ-027]].

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables. Same hard gap as Capability Management batch's net-new L2s.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
