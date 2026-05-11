---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-10
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.4 Service Domain"
l2_id: "1.4.12"
l2_name: "Service Capacity Management"
---

# Service Capacity Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Capability Management ([[wiki/foundations/lifecycle#Capability Management]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). The entire process tree below — L2 + 9 L3s + 8 L4s + L5s — has no R20.5 lineage. Capacity Management as a dedicated L2 didn't exist as a separate process in pre-v25 GB921; it was introduced in v25.5 as part of the Capability Management vertical's expansion. Same applies to the Resource-side analog L2 [[wiki/etom/resource-domain/resource-capacity-management|1.5.14]].

## Overview

Service Capacity Management business process manage the activities required to ensure a business is able to plan, analyze, optimize, monitor and report on capacity and constraints associated to services in response to business requirements (e.g. SLRs) and objectives (e.g. SLAs, SLOs etc.).

Service capacity is the volume of activity that a service offered can handle while maintaining standards of quality and performance. The underlying business activities supporting Service Capacity Management ensure that there is an effective understanding and management of service delivery business objectives, based on all underlying constraints.

— GB921 v25.5 Excel master, process ID `1.4.12`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

Per-L3 Extended Descriptions and L4 / L5 sub-process listings, verbatim from GB921 v25.5 Excel master.

### 1.4.12.1 Plan Service Capacity

**Extended Description.**

Plan Service Capacity business activity is in charge of determining the service delivery capacity needed to meet changing demand for services over a period of time, as well as implementing the plan that supports the goals of Service Capacity Management.

Service Capacity Plan ensures Service Management aligns capacity planning strategies with business goals, while: ensuring that there are sufficient capability or supporting service capabilities to meet planned and forecasted business goals; identifying gaps in capacity allocation early; determining resource capacity needs according to demand, determining constraints and usage patterns over time; forecasting future capacity needs; and communicating resource capacity requirements in time.

In the context of service capacity planning, consideration is given to measuring performance and comparing it to requirements that are set in Service Level Agreements (SLAs) or Service Level Requirements (SLRs).

_No L4 sub-processes in source._

### 1.4.12.2 Align Service Capacity Planning Goals

**Extended Description.**

Align Service Capacity Planning Goals business activity correlates Service Capacity Plans (established as Service Level Objectives) with business demand, as defined in service level requirements (SLRs).

_No L4 sub-processes in source._

### 1.4.12.3 Establish Service Capacity GAP

**Extended Description.**

Establish Service Capacity GAP business activity identifies any disparity between Service capacity goals (SLAs) and business objectives (SLOs).

_No L4 sub-processes in source._

### 1.4.12.4 Forecast Service Capacity Need

**Extended Description.**

Forecast Service Capacity Need business activity develops projections that predict service capacity growth, by understanding the impact on business.

**L4 sub-processes:**

- **1.4.12.4.1** Define Service Capacity Requirement — Establishes, measures, and adjusts conditions that impact on planning service capacity performance.
- **1.4.12.4.2** Establish Service Capacity Availability Timing Requirement — Identify scheduling needs for service capacity changes to be effective.

### 1.4.12.5 Implement Service Capacity Plan

**Extended Description.**

Implement Service Capacity Plan business activity puts into effect the steps to achieve Service Capacity Plans, with defined service capacity targets, and service capacity management course of action.

**L4 sub-processes:**

- **1.4.12.5.1** Specify Required Service Capacity — Supports implementing service capacity plans by identifying clearly, and definitely, service capacity expectations (SLAs, SLOs etc.).
- **1.4.12.5.2** Specify Service Capacity Course of Action — Identifies clearly, and definitely, the sequence of activities that must be followed to support the 'Service Capacity Plan' expectations.

### 1.4.12.6 Analyze Service Capacity

**Extended Description.**

Analyze Service Capacity business activity establishes, and models insights, patterns and changes to service capacity, by assessing potential capacity needs, and actual capacity that a service currently achieves.

This business activity covers collection of service-related data (usage data, performance data, operational data etc.) to support Service Management manager to identify patterns and insights relating to a Service.

Analyze Service Capacity supports Service Capacity Management by providing relevant and timely insights, including available capability, service "time and material" needs, etc. and how capacity utilization (allocated, in-use, unused) can be optimized to increase business value.

> **Source-text observation — L4 numbering gap.** The L4 sub-processes for this L3 are numbered `.6.2`, `.6.3`, `.6.4` — there is no `.6.1` in the source. The Resource-side analog L3 [[wiki/etom/resource-domain/resource-capacity-management#1.5.14.6 Analyze Resource Capacity|1.5.14.6]] has a `.6.1 Identify Resource Capacity Optimization Need` L4 with no Service-side counterpart. Source-text quirk preserved verbatim per CLAUDE.md §1, §10.3 (no separate OQ filed; pattern matches OQ-045 family).

**L4 sub-processes:**

- **1.4.12.6.2** Assess Available Service Capacity — Evaluates unused service capacity in relation to service capacity plans, and service utilization trends.
- **1.4.12.6.3** Model Service Capacity — Establishes a representation of service capacity based on demand and defined business properties. Provides a structured way to utilize information to improve the way services are delivered.
    - **1.4.12.6.3.1** (L5) Establish Service Capacity Utilization Behavior — Develops Service Capacity usage models.
- **1.4.12.6.4** Perform Service Capacity and Capacity Demand Trend Analysis — Analyses trends between available service capacity and service capacity demand according to business and ongoing service usage.

### 1.4.12.7 Optimize Service Capacity

**Extended Description.**

Optimize Service Capacity business activity is in charge of improving service capacity usage, by managing underlying and related dependencies, and constraints.

For Service Capacity Management, Optimize Service Capacity can enable reclaim unused or available Resource capacities, and also allocate additional capacity just in time to meet demand. It can also help to repurpose resources based on their capacity utilization patterns, and support configuration management of all constraints and dependencies.

> **Source-text observation — asymmetric L4 structure vs Resource side.** Service-side has 1 L4 (`.7.1 Manage Service Capacity Thresholds`) with 2 L5s beneath (`.7.1.1 Adjust`, `.7.1.2 Allocate`). The Resource-side analog [[wiki/etom/resource-domain/resource-capacity-management#1.5.14.7 Optimize Resource Capacity|1.5.14.7]] has 2 L4s — `.7.1 Manage Resource Capacity **Utilization**` (with the same Adjust + Allocate L5s) and `.7.2 Manage Resource Capacity Thresholds` as a parallel sibling. Same L5 names parented under different L4 names across the PSR pair. Asymmetric — preserved verbatim.

**L4 sub-processes:**

- **1.4.12.7.1** Manage Service Capacity Thresholds — Administering service capacity thresholds based on business and operational conditions, and concerns.
    - **1.4.12.7.1.1** (L5) Adjust Service Capacity — Fulfilling changes to Service Capacity.
    - **1.4.12.7.1.2** (L5) Allocate Service Capacity — Assigns the amount in capacity that a service must support.

### 1.4.12.8 Monitor Service Capacity

**Extended Description.**

Monitor Service Capacity business activity identifies relevant service capacity attributes/properties, and monitors and tracks all service attributes, their use, and changes.

Monitor Service Capacity supports all activities in Service Capacity Management by providing timely visibility for all concerns around service capacity.

_No L4 sub-processes in source._

### 1.4.12.9 Report Service Capacity

**Extended Description.**

Report Service Capacity business activity prepares and presents detailed accounts of all relevant service capacity information, in a timely manner, and in ways that are relevant and reliable for use by business.

Different business functions with interest for Resource Capacity may require specific reports with specific information. This business activity ensures reports for Resource Capacity are collated, organized and presented in ways that are useful, and reliable to the needs of business functions in a timely manner.

> **Source-text observation — copy-paste bug.** The body of this L3's ED references "Resource Capacity" twice (in the Service-side L2's Service-side L3). Intent is unambiguously *Service Capacity* given context (this is 1.4.12.9 Report **Service** Capacity within 1.4.12 **Service** Capacity Management). The text appears copy-pasted from the Resource-side mirror page [[wiki/etom/resource-domain/resource-capacity-management#1.5.14.9 Report Resource Capacity|1.5.14.9]] without the Service substitution. Verbatim preserved per CLAUDE.md §1, §10.3. Pattern matches OQ-045-family handling — source-text bug, intent recognisable, no separate OQ filed.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.4.12.1** Plan Service Capacity — Determining the service delivery capacity needed to meet changing demand for services over a period of time, as well as implementing the plan that supports the goals of Service Capacity Management.
- **1.4.12.2** Align Service Capacity Planning Goals — Correlates Service Capacity Plans (established as Service Level Objectives) with business demand, as defined in service level requirements (SLRs).
- **1.4.12.3** Establish Service Capacity GAP — Identifies any disparity between Service capacity goals (SLAs) and business objectives (SLOs).
- **1.4.12.4** Forecast Service Capacity Need — Develops projections that predict service capacity growth, by understanding the impact on business.
- **1.4.12.5** Implement Service Capacity Plan — Puts into effect the steps to achieve Service Capacity Plans, with defined service capacity targets, and service capacity management course of action.
- **1.4.12.6** Analyze Service Capacity — Establishes, and models insights, patterns and changes to service capacity, by assessing potential capacity needs, and actual capacity that a service currently achieves.
- **1.4.12.7** Optimize Service Capacity — Improving service capacity usage, by managing underlying and related dependencies, and constraints.
- **1.4.12.8** Monitor Service Capacity — Identifies relevant service capacity attributes/properties, and monitors and tracks all service attributes, their use, and changes.
- **1.4.12.9** Report Service Capacity — Prepares and presents detailed accounts of all relevant service capacity information, in a timely manner, and in ways that are relevant and reliable for use by business.

## SID Entities Manipulated

- [[wiki/sid/service/service-capacity-abe]] — direct match. The Service Capacity ABE (which specialises the canonical Capacity pattern from the Common Domain) is the primary data model this L2 manages: the L2's nine L3s plan, align, gap-analyse, forecast, implement, analyse, optimize, monitor, and report on service capacity. The same ABE carries an existing back-link from Service Capability Delivery (1.4.2, capacity-shortfalls dependency) — this L2 (1.4.12) is the *primary ongoing-management* manipulator vs 1.4.2's *upstream-input* manipulator. The cross-L2 navigation lives on the SID page itself; cross-L2 wikilinks here would trigger bidirectional consistency checks.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables, since GB1022 was scoped operationally and the mapping tables predate the v25.5 introduction of Capacity Management as a discrete L2.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Service Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0, so no narrative-PDF supplementation pass is anticipated for this L2 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — filed 2026-05-10 with the 1.4.1 ingest; applies forward to all 16 S2R L2s; net-new-in-v25.5 status of this L2 sharpens the gap)_
