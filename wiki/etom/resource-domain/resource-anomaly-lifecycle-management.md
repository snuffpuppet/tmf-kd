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
l2_id: "1.5.20"
l2_name: "Resource Anomaly Lifecycle Management"
---

# Resource Anomaly Lifecycle Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Business Value Development ([[wiki/foundations/lifecycle#Business Value Development]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent) at L2 and across every L3 + L4. PSR-symmetric with the Service-side analog [[wiki/etom/service-domain/service-anomaly-lifecycle-management|1.4.17]].

> **BVD-governs / Operations-executes — pairs with [[wiki/etom/resource-domain/resource-anomaly-management|1.5.21 Resource Anomaly Management]] (Operations / Assurance).** The two L2s form a **two-L2 Anomaly pattern** spanning both Lifecycle Areas in v25.5:
>
> - **Lifecycle (this L2)** (S2R-BVD, 1.5.20) — **defines** what "normal" is, **orchestrates** the closed loop, **monitors / reports** on the closed-loop process itself, manages **intelligence** (knowledge continuum) and **optimization** (business-logic fine-tuning).
> - **Management** (Ops-A, 1.5.21) — **executes** per anomaly instance: Predict / Detect / Assess / Mitigate / Manage Learning.
>
> Structurally analogous to the **four-L2 Catalog lifecycle** (Planning S2R-CM + Lifecycle S2R-BVD + Operational Readiness Ops-ORS + Content Ops-ORS) and to the **Test-strategy lineage** (1.5.1.8/9 strategic + 1.5.4.9 operational H5). Third instance in v25.5 of the cross-Lifecycle-Area "BVD governs / Operations executes" pattern.

## Overview

Resource Anomaly Lifecycle Management business process establishes and controls all activities that are involved in overseeing, directing, administering, controlling and organizing the definition, detection/prediction, mitigation and learnings related to Resource Anomaly Management.

Resource Anomaly Lifecycle Management cover the lifecycle activities, including:

- Establishing "what is normal" for Resource in order to inform "deviations" or aberrations.
- Orchestrating Resource Anomaly Management activities to meet business needs.
- Managing the ability to acquire and apply knowledge and skills from past and present Resource anomalies.
- Managing actions that make the best or effective use of Resource Management Closed Loops.
- Monitoring feedback to and from Resource Management to support Resource Anomaly Management activities.
- Reporting on Resource Anomaly Management Closed Loops.

— GB921 v25.5 Excel master, process ID `1.5.20`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2). Smart curly quotes around *"what is normal"* and *"deviations"* preserved verbatim per CLAUDE.md §1, §10.3.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.20.1 Manage Resource Anomaly Definition

**Extended Description.**

Manage Resource Anomaly Definition business activity is in charge of defining and describing the information about data which is used in Resource Anomaly Management.

Manage Resource Anomaly Definition business activity covers activities that describe the criteria, characteristics, and expectations of information required for Resource Anomaly Detection. All descriptions and definitions of the information about data use in Resource Anomaly Management business activities may include, but not be limited to "normal pattern data", "constraints data", "goals data" etc.

**L4 sub-processes:**

- **1.5.20.1.1** Define Resource Anomaly Closed Loop — state and describe the Resource Anomaly Closed Loops along with associated information that lead to identifying, detecting or predicting a Resource Anomaly. Supports the Anomaly definition process and the Closed Loops associated, including all associated inputs that reasonably affect the management of an Anomaly Lifecycle.
- **1.5.20.1.3** Establish Resource Anomaly Closed Loop Information Sources — identifies all information sources and the requisite data that must be managed to support Resource Anomaly Management Closed Loops. Helps to identify the information (not limited to business and operations rules), business logic, levels of classification, impact and urgency etc. that can help detect Resource Anomaly. Supports Resource Anomaly Management during day-to-day resource delivery.

> **PSR-asymmetry — L4 `.1.2` missing entirely on this side.** The Service-side analog [[wiki/etom/service-domain/service-anomaly-lifecycle-management|1.4.17]] has L4 `1.4.17.1.2 Establish Anomaly Criteria` (5 L4s total under L3 `.1`); Resource-side here has only `.1.1` and `.1.3` (2 L4s under L3 `.1`, 4 L4s for the L2 overall). **Inverse-shape to the Capacity Management `.6.1` numbering gap** (where Service was missing what Resource had); here Service has what Resource is missing. The missing Resource-side L4 corresponds **structurally** to the Service-side L4 that carries the Product → Service body-text leakage bug — see source-text observation on the Service-side page. Whether the GB921 author dropped 1.5.20.1.2 deliberately or accidentally is not stated in the source; cannot infer authorial intent (CLAUDE.md §1). Verbatim preserved.

### 1.5.20.2 Orchestrate Resource Anomaly Management Closed Loop

**Extended Description.**

Orchestrate Resource Anomaly Management Closed Loop business activity is in charge of organizing, arranging and coordinating changes that control Resource Anomaly Management Closed Loops.

This business activity will cover:

- Managing Resource Anomaly Detection activities — initiating, suspending, maintaining, and terminating.
- Organizing Resource Anomaly Detection activities — including arranging the sequence for Closed Loop activities.
- Coordinating changes to a Resource Anomaly Management Closed Loop.

**L4 sub-processes:**

- **1.5.20.2.1** Manage Resource Anomaly Profile — recording and analyzing Resource Anomaly Management frameworks in order to enable assess and predict Resource Anomaly Management capabilities according to well-specified resource management models. Supports Resource Anomaly Management operations, as well as capturing the business intents that need to be associated with Resource Anomaly Closed Loops and Resource Anomaly Management Lifecycle.

> **Minor source-text observation — PSR-asymmetric typography.** The 1.5.20.2.1 brief carries a terminal period (*"…well-specified resource management models."*); the Service-side analog 1.4.17.2.1 brief is missing the terminal period. Verbatim preserved.

### 1.5.20.3 Monitor Resource Anomaly Management Closed Loop

**Extended Description.**

Monitor Resource Anomaly Management Closed Loop business activity provides the capability to observe Resource Anomaly Management Closed Loops.

This business activity helps to scan; watch; monitor; and gain awareness of Resource Anomaly Management activities that provide feedback between Resource Anomaly Management Lifecycle(s) stages.

_No L4 sub-processes in source._

### 1.5.20.4 Report Resource Anomaly Management Closed Loop

**Extended Description.**

Report Resource Anomaly Management Closed Loop business activity documents information organized to deliver an account of any, and all Resource Anomaly Closed Loops.

Anomaly Closed Loops may fall into either or across any of the four stages in any of the overarching Closed Loop pattern — Observe, Orient, Decide and Act — or other variations.

> **OODA framing — verbatim from source.** The L3 ED explicitly cites the **Observe / Orient / Decide / Act** pattern as the conceptual model for Anomaly Closed Loops. Same wording on Service-side analog 1.4.17.4. v25.5 anchors Anomaly Closed-Loop Management on the OODA loop.

_No L4 sub-processes in source._

### 1.5.20.5 Manage Resource Anomaly Intelligence

**Extended Description.**

Manage Resource Anomaly Intelligence business activity is in charge of acquiring and applying new learning, knowledge and skills to Resource Anomaly Management.

This business activity supports improving, optimizing, or evolving Resource Anomaly Management activities. Manage Resource Anomaly Intelligence helps to incorporate new knowledge and skills into Resource Anomaly Management processes. This is as well to enable improvement and optimization of all Anomaly Management in a continuum.

_No L4 sub-processes in source._

### 1.5.20.6 Manage Resource Anomaly Optimization

**Extended Description.**

Manage Resource Anomaly Optimization business activity is in charge of actions that make the best and most effective use of Resource Anomaly Management activities to improve Resource Anomaly Management and ultimately Resource Management.

Manage Resource Anomaly Optimization business activity can manage the business logic and business rules associated with Resource Anomaly Detection, Resource Anomaly Assessment, Resource Anomaly Forecasting and Prediction, Resource Anomaly Mitigation, as well as underlying Resource Knowledge Management.

This business activity also includes fine-tuning of business logic, operations logic, business and operations rules that improve efficiency of Anomaly Management as a whole.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.20.1** Manage Resource Anomaly Definition — defining and describing the information about data which is used in Resource Anomaly Management.
- **1.5.20.2** Orchestrate Resource Anomaly Management Closed Loop — organizing, arranging and coordinating changes that control Resource Anomaly Management Closed Loops.
- **1.5.20.3** Monitor Resource Anomaly Management Closed Loop — provides the capability to observe Resource Anomaly Management Closed Loops.
- **1.5.20.4** Report Resource Anomaly Management Closed Loop — documents information organized to deliver an account of any, and all Resource Anomaly Closed Loops.
- **1.5.20.5** Manage Resource Anomaly Intelligence — acquiring and applying new learning, knowledge and skills to Resource Anomaly Management.
- **1.5.20.6** Manage Resource Anomaly Optimization — actions that make the best and most effective use of Resource Anomaly Management activities to improve Resource Anomaly Management.

## SID Entities Manipulated

- [[wiki/sid/common/anomaly-abe]] — **primary trilateral target.** The Anomaly ABE's `AnomalySpecification` entity *"defines AnomalyClosedLoop scope and lifecycle"* (GB922 Common §4.30.1) — direct match for this L2's L3 1.5.20.1 (Definition) + 1.5.20.2 (Orchestrate Closed Loop) + 1.5.20.4 (Report Closed Loop) framing. The Anomaly ABE Overview language matches this L2's "establish what is normal" / "orchestrate / monitor / report on Closed Loops" wording word-for-word. The Resource-domain specialisation referenced in GB922 Common §4.30.2 ("Resource and other domain-specific anomaly specialisations follow the same pattern") is the Resource-specific entity manipulated.
- [[wiki/sid/common/closed-loop-abe]] — every L3 in this L2 explicitly references "Closed Loop" / "Anomaly Closed Loop" / "Anomaly Management Closed Loop". The Closed Loop ABE itself documents the Anomaly↔ClosedLoop relationship verbatim (GB922 Common §4.27.2). Note: Closed Loop ABE is **`release_status: draft`** («Preliminary» annotation on GB922 Common v23.0 §4.27 chapter heading) — the SID model in this area is honest-but-evolving; heat-map cell calibration should account for SID-side maturity.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables. Hard ODA gap, same as Capability Management batch's net-new L2s and the Catalog Lifecycle PSR pair.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
