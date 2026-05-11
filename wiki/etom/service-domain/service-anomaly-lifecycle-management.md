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
l2_id: "1.4.17"
l2_name: "Service Anomaly Lifecycle Management"
---

# Service Anomaly Lifecycle Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Business Value Development ([[wiki/foundations/lifecycle#Business Value Development]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent) at L2 and across every L3 + L4. PSR-symmetric with the Resource-side analog [[wiki/etom/resource-domain/resource-anomaly-lifecycle-management|1.5.20]].

> **BVD-governs / Operations-executes — pairs with [[wiki/etom/service-domain/service-anomaly-management|1.4.18 Service Anomaly Management]] (Operations / Assurance).** The two L2s form a **two-L2 Anomaly pattern** spanning both Lifecycle Areas in v25.5:
>
> - **Lifecycle (this L2)** (S2R-BVD, 1.4.17) — **defines** what "normal" is, **orchestrates** the closed loop, **monitors / reports** on the closed-loop process itself, manages **intelligence** (knowledge continuum) and **optimization** (business-logic fine-tuning).
> - **Management** (Ops-A, 1.4.18) — **executes** per anomaly instance: Predict / Detect / Assess / Mitigate / Manage Learning.
>
> Structurally analogous to the **four-L2 Catalog lifecycle** ([[wiki/etom/service-domain/service-catalog-planning-management|Planning S2R-CM]] + [[wiki/etom/service-domain/service-catalog-lifecycle-management|Lifecycle S2R-BVD]] + [[wiki/etom/service-domain/service-catalog-operational-readiness-management|Operational Readiness Ops-ORS]] + [[wiki/etom/service-domain/service-catalog-content-management|Content Ops-ORS]]) and to the **Test-strategy lineage** (1.4.1.8/9 strategic + 1.4.4.6 operational H5). Third instance in v25.5 of the cross-Lifecycle-Area "BVD governs / Operations executes" pattern.

## Overview

Service Anomaly Lifecycle Management business process establishes and controls all activities that are involved in overseeing, directing, administering, controlling and organizing the definition, detection/prediction, mitigation and learnings related to Service Anomaly Management.

Service Anomaly Lifecycle Management cover the lifecycle activities, including:

- Establishing "what is normal" for Service in order to inform "deviations" or aberrations.
- Orchestrating Service Anomaly Management activities to meet business needs.
- Managing the ability to acquire and apply knowledge and skills from past and present Service anomalies.
- Managing actions that make the best or effective use of Service Management Closed Loops.
- Monitoring feedback to and from Service Management to support Service Anomaly Management activities.
- Reporting on Service Anomaly Management Closed Loops.

— GB921 v25.5 Excel master, process ID `1.4.17`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2). Smart curly quotes around *"what is normal"* and *"deviations"* preserved verbatim per CLAUDE.md §1, §10.3.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.4.17.1 Manage Service Anomaly Definition

**Extended Description.**

Manage Service Anomaly Definition business activity is in charge of defining and describing the information about data which is used in Service Anomaly Management.

Manage Service Anomaly Definition business activity covers activities that describe the criteria, characteristics, and expectations of information required for Service Anomaly Detection. All descriptions and definitions of the information about data use in Service Anomaly Management business activities may include, but not be limited to "normal pattern data", "constraints data", "goals data" etc.

**L4 sub-processes:**

- **1.4.17.1.1** Define Service Anomaly Closed Loop — state and describe the Service Anomaly Closed Loops along with associated information that lead to identifying, detecting or predicting a Service Anomaly. Supports the Anomaly definition process and the Closed Loops associated, including all associated inputs that reasonably affect the management of an Anomaly Lifecycle.
- **1.4.17.1.2** Establish Anomaly Criteria — _(see source-text observation immediately below.)_
- **1.4.17.1.3** Establish Service Anomaly Closed Loop Information Sources — identifies all information sources and the requisite data that must be managed to support Service Anomaly Management Closed Loops. Helps to identify the information (not limited to business and operations rules), business logic, levels of classification, impact and urgency etc. that can help detect Service Anomaly. Supports Service Anomaly Management during day-to-day service delivery.

> **Source-text observation cluster on L4 1.4.17.1.2 — three threads on the same L4.**
>
> **Thread A — L4 name omits PSR qualifier.** L4 listed as *"Establish Anomaly Criteria"* (no "Service") in the source name column; brief opens *"Establish **Service** Anomaly Criteria business activity…"*. PSR-name vs PSR-body asymmetry within the same row.
>
> **Thread B — Body text references "Products" / "Product's" instead of Services.** Brief: *"…all criteria needed to identify and predict deviation from what is known standard, normal, or expected of **Products** according to business dictates."* ED: *"Establishing a **Product's** anomalous criterion is key to enable differentiate norms or standards from what is not. This will include specific **Service** design constraints (e.g. Service strategy, service offering, service goals) or Service operations."* Mid-paragraph PSR-context flip Product → Service. Pattern matches the cross-PSR-domain copy-paste bug family (1.4.19.2 carrying "Resource Specifications"; 1.4.12.9 carrying "Resource Capacity"; 1.4.13.x cluster) — but here the leakage is **Product → Service**, not Resource → Service. **First instance of Product-domain leakage in Phase 3 source-text bugs.**
>
> **Thread C — Structural correlation: this L4 is missing entirely on the Resource side.** [[wiki/etom/resource-domain/resource-anomaly-lifecycle-management|1.5.20]] has L4s `.1.1` and `.1.3` only — **no `.1.2` analog** for "Establish (Resource) Anomaly Criteria". Whether the GB921 author dropped 1.5.20.1.2 because the Service-side draft was Product-themed-by-mistake, or for another reason, is not stated in the source. Cannot infer authorial intent (CLAUDE.md §1).
>
> All three threads **preserved verbatim** per CLAUDE.md §1, §10.3; OQ-045-family handling; no separate OQ filed.

**1.4.17.1.2 Establish Anomaly Criteria — verbatim source content:**

- **Brief:** Establish Service Anomaly Criteria business activity is in charge of defining and identifying all criteria needed to identify and predict deviation from what is known standard, normal, or expected of Products according to business dictates.
- **ED:** Establish Service Anomaly Criteria business activity is in charge of defining and identifying all criteria needed to identify and predict deviation from what is known standard, normal, or expected of Products according to business dictates. Establishing a Product's anomalous criterion is key to enable differentiate norms or standards from what is not. This will include specific Service design constraints (e.g. Service strategy, service offering, service goals) or Service operations.

### 1.4.17.2 Orchestrate Service Anomaly Management Closed Loop

**Extended Description.**

Orchestrate Service Anomaly Management Closed Loop business activity is in charge of organizing, arranging and coordinating changes that control Service Anomaly Management Closed Loops.

This business activity will cover:

- Managing Service Anomaly Detection activities — initiating, suspending, maintaining, and terminating.
- Organizing Service Anomaly Detection activities — including arranging the sequence for Closed Loop activities.
- Coordinating changes to a Service Anomaly Management Closed Loop.

**L4 sub-processes:**

- **1.4.17.2.1** Manage Service Anomaly Profile — recording and analyzing Service Anomaly Management frameworks in order to enable assess and predict Service Anomaly Management capabilities according to well-specified service management models. Supports Service Anomaly Management operations, as well as capturing the business intents that need to be associated with Service Anomaly Closed Loops and Service Anomaly Management Lifecycle.

> **Minor source-text observation.** The 1.4.17.2.1 brief in source is missing the terminal period (*"…well-specified service management models"* — no period). The Resource-side analog 1.5.20.2.1 brief carries the terminal period. Minor PSR typographic asymmetry; verbatim preserved.

### 1.4.17.3 Monitor Service Anomaly Management Closed Loop

**Extended Description.**

Monitor Service Anomaly Management Closed Loop business activity provides the capability to observe Service Anomaly Management Closed Loops.

This business activity helps to scan; watch; monitor; and gain awareness of Service Anomaly Management activities that provide feedback between Service Anomaly Management Lifecycle(s) stages.

_No L4 sub-processes in source._

### 1.4.17.4 Report Service Anomaly Management Closed Loop

**Extended Description.**

Report Service Anomaly Management Closed Loop business activity documents information organized to deliver an account of any, and all Service Anomaly Closed Loops.

Anomaly Closed Loops may fall into either or across any of the four stages in any of the overarching Closed Loop pattern — Observe, Orient, Decide and Act — or other variations.

> **OODA framing — verbatim from source.** The L3 ED explicitly cites the **Observe / Orient / Decide / Act** pattern as the conceptual model for Anomaly Closed Loops. Same wording on Resource-side analog 1.5.20.4. v25.5 anchors Anomaly Closed-Loop Management on the OODA loop.

_No L4 sub-processes in source._

### 1.4.17.5 Manage Service Anomaly Intelligence

**Extended Description.**

Manage Service Anomaly Intelligence business activity is in charge of acquiring and applying new learning, knowledge and skills to Service Anomaly Management.

This business activity supports improving, optimizing, or evolving Service Anomaly Management activities. Manage Service Anomaly Intelligence helps to incorporate new knowledge and skills into Service Anomaly Management processes. This is as well to enable improvement and optimization of all Anomaly Management in a continuum.

_No L4 sub-processes in source._

### 1.4.17.6 Manage Service Anomaly Optimization

**Extended Description.**

Manage Service Anomaly Optimization business activity is in charge of actions that make the best and most effective use of Service Anomaly Management activities to improve Service Anomaly Management and ultimately Service Management.

Manage Service Anomaly Optimization business activity can manage the business logic and business rules associated with Service Anomaly Detection, Service Anomaly Assessment, Service Anomaly Forecasting and Prediction, Service Anomaly Mitigation, as well as underlying Service Knowledge Management.

This business activity also includes fine-tuning of business logic, operations logic, business and operations rules that improve efficiency of Anomaly Management as a whole.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.4.17.1** Manage Service Anomaly Definition — defining and describing the information about data which is used in Service Anomaly Management.
- **1.4.17.2** Orchestrate Service Anomaly Management Closed Loop — organizing, arranging and coordinating changes that control Service Anomaly Management Closed Loops.
- **1.4.17.3** Monitor Service Anomaly Management Closed Loop — provides the capability to observe Service Anomaly Management Closed Loops.
- **1.4.17.4** Report Service Anomaly Management Closed Loop — documents information organized to deliver an account of any, and all Service Anomaly Closed Loops.
- **1.4.17.5** Manage Service Anomaly Intelligence — acquiring and applying new learning, knowledge and skills to Service Anomaly Management.
- **1.4.17.6** Manage Service Anomaly Optimization — actions that make the best and most effective use of Service Anomaly Management activities to improve Service Anomaly Management.

## SID Entities Manipulated

- [[wiki/sid/common/anomaly-abe]] — **primary trilateral target.** The Anomaly ABE's `AnomalySpecification` entity *"defines AnomalyClosedLoop scope and lifecycle"* (GB922 Common §4.30.1) — direct match for this L2's L3 1.4.17.1 (Definition) + 1.4.17.2 (Orchestrate Closed Loop) + 1.4.17.4 (Report Closed Loop) framing. The Anomaly ABE Overview language ("any unusual or unexpected event… that an enterprise wishes to detect, analyze, assess and mitigate within an autonomous environment… anomalies may require administrative and operational guidance") matches this L2's "establish what is normal" / "orchestrate / monitor / report on Closed Loops" wording word-for-word. The Service-domain specialisation `ServiceAnomaly / ServiceAnomalySpecification` (Common §4.30.2) is the Service-specific entity manipulated.
- [[wiki/sid/common/closed-loop-abe]] — every L3 in this L2 explicitly references "Closed Loop" / "Anomaly Closed Loop" / "Anomaly Management Closed Loop". The Closed Loop ABE itself documents the Anomaly↔ClosedLoop relationship verbatim (*"Anomaly is managed using a ClosedLoop defined by ClosedLoopSpecification"* — GB922 Common §4.27.2). Note: Closed Loop ABE is **`release_status: draft`** («Preliminary» annotation on GB922 Common v23.0 §4.27 chapter heading) — the SID model in this area is honest-but-evolving; heat-map cell calibration should account for SID-side maturity.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables. Hard ODA gap, same as Capability Management batch's net-new L2s and the Catalog Lifecycle PSR pair.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Service Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status sharpens the gap)_
