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
l2_id: "1.5.18"
l2_name: "Resource Catalog Planning Management"
---

# Resource Catalog Planning Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Capability Management ([[wiki/foundations/lifecycle#Capability Management]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). The entire process tree below — L2 + 2 L3s — has no R20.5 lineage. PSR-symmetric with the Service-side analog [[wiki/etom/service-domain/service-catalog-planning-management|1.4.16]].

## Overview

Resource Catalog Planning Management business process covers a set of business activities that understand and enable establish the plan to define, design and operationalize a catalog in order to meet the needs and objectives of Resource cataloging.

The Resource Catalog Planning Management business process ensure that the organization is able to identify the most appropriate scheme and goal for it catalog. It includes designing the Catalog plan and developing the specification according to Resource management requirement.

— GB921 v25.5 Excel master, process ID `1.5.18`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

Per-L3 Extended Descriptions verbatim from GB921 v25.5 Excel master. No L4 / L5 decomposition in source for this L2.

### 1.5.18.1 Design Resource Catalog Plan

**Extended Description.**

Resource Design Catalog Plan business activity understands requirements and capabilities demanded from the business to establish the Catalog plan based on the Resource strategy for Resource Catalog Planning Management.

> **Source-text observation — PSR-symmetric extra-qualifier-word quirk.** The L3 name is *"Design Resource Catalog Plan"* but the ED opens with *"**Resource Design** Catalog Plan business activity…"* — the PSR qualifier word "Resource" is shifted from the middle of the name to the front of the ED prose. Service-side analog [[wiki/etom/service-domain/service-catalog-planning-management#1.4.16.1 Design Service Catalog Plan|1.4.16.1]] carries the parallel quirk. PSR-symmetric source-text artefact preserved verbatim per CLAUDE.md §1, §10.3. No separate OQ filed.

_No L4 sub-processes in source._

### 1.5.18.2 Define Resource Catalog Specification

**Extended Description.**

Define Catalog Specification business activity establishes the Catalog specifications based on the product/service/resource strategy to support Catalog Planning Management.

Define Catalog Specification leverages Specification Management business activities to establish the mandatory and optional design requirements, as well as catalog entry fields according to product/service/resource management needs. This process will be governed by the Enterprise Business Process for Catalog Management.

> **Forward reference — Specification Management.** The ED references "Specification Management business activities" — points to L2 1.5.19 Resource Specification Management, scheduled for ingest under the fourth Capability Management PSR pair. When 1.5.19 lands, this L3 becomes a back-reference target.

> **Forward reference — Enterprise Business Process for Catalog Management.** The closing sentence references an "Enterprise Business Process for Catalog Management" as the governance authority. No L2 by that name exists in the v25.5 in-scope corpus; likely Enterprise-domain content (out of L1 scope per CLAUDE.md §3) or a generic governance framework. Preserved verbatim. Pattern matches the Service-side analog 1.4.16.2 and other S2R out-of-scope forward references. No separate OQ filed.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.18.1** Design Resource Catalog Plan — Understands requirements and capabilities demanded from the business to establish the Catalog plan based on the Resource strategy for Resource Catalog Planning Management.
- **1.5.18.2** Define Resource Catalog Specification — Establishes the Catalog specifications based on the product/service/resource strategy to support Catalog Planning Management.

## SID Entities Manipulated

- [[wiki/sid/resource/resource-specification-abe]] — direct match. The Resource Catalog is §4.2.5 Resource Catalog ABE within the Resource Specification ABE per the v1 SID granularity decision (sub-ABEs documented at parent-ABE level). The L2's L3 1.5.18.2 explicitly produces "Catalog specifications", "mandatory and optional design requirements", and "catalog entry fields" — these are the Resource Catalog sub-ABE's structural content. The same ABE carries an existing back-link from Resource Capability Delivery (1.5.2, design-specifications dependency for resource infrastructure components, including legacy-vs-new integration design) — this L2 (1.5.18) is the *catalog-planning-specific* manipulator producing catalog-side artefacts, vs 1.5.2's *resource-infrastructure-design* manipulator. Target ABE is `release_status: pre-production` per [[wiki/open-questions#OQ-027]]. Plain-prose reference to the canonical Catalog pattern (Common Domain) — wikilink lives on the SID page itself.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables, since GB1022 was scoped operationally and the mapping tables predate the v25.5 introduction of Catalog Planning Management as a discrete L2.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0, so no narrative-PDF supplementation pass is anticipated for this L2 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
