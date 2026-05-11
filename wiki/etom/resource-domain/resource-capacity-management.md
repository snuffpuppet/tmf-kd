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
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.14"
l2_name: "Resource Capacity Management"
---

# Resource Capacity Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Capability Management ([[wiki/foundations/lifecycle#Capability Management]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

> **Net-new in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). The entire process tree below — L2 + 9 L3s + 10 L4s + L5s — has no R20.5 lineage. PSR-symmetric with the Service-side analog [[wiki/etom/service-domain/service-capacity-management|1.4.12]] in this respect; both L2s entered GB921 in v25.5 as part of the Capability Management vertical's expansion.

## Overview

Resource Capacity Management business process manage the activities required to ensure a business is able to plan, analyze, optimize, monitor and report on capacity and constraints associated to resources in response to business objectives in a timely fashion.

The underlying business activities supporting Resource Capacity Management ensure that there is an effective understanding and management of business objectives, based on underlying Resource constraints.

— GB921 v25.5 Excel master, process ID `1.5.14`, sheet `eTOM25,5`. Original PID = `None` (v25.5-net-new L2).

## L3 Process Details

Per-L3 Extended Descriptions and L4 / L5 sub-process listings, verbatim from GB921 v25.5 Excel master.

### 1.5.14.1 Plan Resource Capacity

**Extended Description.**

Plan Resource Capacity business activity is in charge of determining the production capacity needed to meet changing demand for resources over a period of time, and implements the plan.

Plan Resource Capacity  ensures Resource Management aligns capacity planning strategies with business goals; while ensuring that there are sufficient resources or supporting resource capabilities to support planned and forecasted business objectives; identifying gaps in capacity allocation early; determining resource capacity needs according to demand, determining constraints and usage patterns over time; forecasting future capacity needs; and communicating resource capacity requirements in time.

In the context of capacity planning, consideration is given to all input requirements, conversion processes and outputs.

_No L4 sub-processes in source._

### 1.5.14.2 Align Resource Capacity Planning Goals

**Extended Description.**

Align Resource Capacity Planning Goals business activity correlates Resource Capacity Plans with business demand.

_No L4 sub-processes in source._

### 1.5.14.3 Establish Resource Capacity GAP

**Extended Description.**

Establish Resource Capacity GAP business activity identifies any disparity between resource capacity goals and business objectives.

_No L4 sub-processes in source._

### 1.5.14.4 Forecast Resource Capacity Need

**Extended Description.**

Forecast Resource Capacity Need business activity develops projections that predict resource capacity growth, by understanding the impact on business.

**L4 sub-processes:**

- **1.5.14.4.1** Define Resource Capacity Requirement — Establishes, measures, and adjusts conditions that impact on planning resource capacity.
- **1.5.14.4.2** Establish Resource Capacity Availability Timing Requirement — Identify scheduling needs for resource capacity changes.

### 1.5.14.5 Implement Resource Capacity Plan

**Extended Description.**

Implement Resource Capacity Plan business activity puts into effect the steps to achieve Resource Capacity Plans, with defined resource capacity target and resource capacity management course of action.

**L4 sub-processes:**

- **1.5.14.5.1** Specify Required Resource Capacity — Supports implementing resource capacity plans by identifying clearly, and definitely, resource capacity expectations.
- **1.5.14.5.2** Specify Resource Capacity Course of Action — Identifies clearly, and definitely, the sequence of activities that must be followed to support the 'Resource Capacity Plan' expectations.

### 1.5.14.6 Analyze Resource Capacity

**Extended Description.**

Analyze Resource Capacity business activity establishes, and models insights, patterns and changes to resource capacity by assessing potential capacity need and actual capacity that a resource currently achieves.

This business activity covers collection of resource-related data (usage data, performance data, operational data etc.) to support Resource Managers to identify patterns and insights relating to a resource.

Analyze Resource Capacity supports Resource Capacity Management by providing relevant and timely insights, including available inventory holding capacity, resource "time and material" needs, etc. and how capacity utilization (allocated, in-use, unused) can be optimized to increase business value.

> **PSR asymmetry note.** This L3 carries 4 L4s. The Service-side analog [[wiki/etom/service-domain/service-capacity-management#1.4.12.6 Analyze Service Capacity|1.4.12.6]] has only 3 L4s (numbered `.6.2`, `.6.3`, `.6.4` — no `.6.1` in source). The `.6.1 Identify Resource Capacity Optimization Need` L4 below has no Service-side counterpart. Asymmetric — preserved verbatim.

**L4 sub-processes:**

- **1.5.14.6.1** Identify Resource Capacity Optimization Need — Establish the best, or most effective, use of resource capacity. _(Resource-only L4; no Service-side counterpart in 1.4.12.6.)_
- **1.5.14.6.2** Assess Available Resource Capacity — Evaluates unused resource capacity in relation to resource capacity plans and resource utilization trends.
- **1.5.14.6.3** Model Resource Capacity — Establishes a representation of Resource Capacity based on demand and defined business properties.
    - **1.5.14.6.3.1** (L5) Establish Resource Capacity Utilization Behavior — Develops Resource Capacity usage models.
- **1.5.14.6.4** Perform Resource Capacity and Capacity Demand Trend Analysis — Analyses trends between available resource capacity and resource capacity demand according to business and ongoing resource usage.

### 1.5.14.7 Optimize Resource Capacity

**Extended Description.**

Optimize Resource Capacity business activity is in charge of improving resource capacity usage by managing underlying and related dependencies and constraints.

For Resource Capacity Management, Optimize Resource Capacity can enable reclaim unused or available Resource capacities, and also allocate additional capacity just in time to meet demand. It can also help to repurpose resources based on their capacity utilization patterns, and support configuration management of all constraints and dependencies.

> **PSR asymmetry note.** This L3 carries 2 L4s — `.7.1 Manage Resource Capacity **Utilization**` (with 2 L5s `Adjust` + `Allocate` beneath it) and `.7.2 Manage Resource Capacity Thresholds` as a parallel sibling. The Service-side analog [[wiki/etom/service-domain/service-capacity-management#1.4.12.7 Optimize Service Capacity|1.4.12.7]] has only 1 L4 (`.7.1 Manage Service Capacity **Thresholds**`) with the same Adjust + Allocate L5s parented under it. **Same L5 names parented under different L4 names across the PSR pair**, and the Service-side has no Utilization-management L4 analog. Asymmetric — preserved verbatim.

**L4 sub-processes:**

- **1.5.14.7.1** Manage Resource Capacity Utilization — Fulfilling and assuring the effective use of resource capacity.
    - **1.5.14.7.1.1** (L5) Adjust Resource Capacity — Fulfilling changes to Resource Capacity.
    - **1.5.14.7.1.2** (L5) Allocate Resource Capacity — Assigns the amount in capacity that a resource must support.
- **1.5.14.7.2** Manage Resource Capacity Thresholds — Administering resource capacity thresholds based on operational conditions and concerns.

### 1.5.14.8 Monitor Resource Capacity

**Extended Description.**

Monitor Resource Capacity business activity identifies relevant resource capacity attributes/properties, and monitors and tracks all attributes, their use, and changes.

 Monitor Resource Capacity supports all activities of Resource Capacity Management by providing timely visibility for all concerns around Resource Capacity

_No L4 sub-processes in source._

### 1.5.14.9 Report Resource Capacity

**Extended Description.**

Report Resource Capacity business activity prepares and presents detailed accounts of all relevant resource capacity information, in a timely manner that is relevant and reliable for use by business.

Different business functions with interest for Resource Capacity may require specific reports with specific information. This business activity ensures reports for Resource Capacity are collated, organized and presented in ways that are useful, and reliable to the needs of business functions in a timely manner.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.14.1** Plan Resource Capacity — Determining the production capacity needed to meet changing demand for resources over a period of time, and implements the plan.
- **1.5.14.2** Align Resource Capacity Planning Goals — Correlates Resource Capacity Plans with business demand.
- **1.5.14.3** Establish Resource Capacity GAP — Identifies any disparity between resource capacity goals and business objectives.
- **1.5.14.4** Forecast Resource Capacity Need — Develops projections that predict resource capacity growth, by understanding the impact on business.
- **1.5.14.5** Implement Resource Capacity Plan — Puts into effect the steps to achieve Resource Capacity Plans, with defined resource capacity target and resource capacity management course of action.
- **1.5.14.6** Analyze Resource Capacity — Establishes, and models insights, patterns and changes to resource capacity by assessing potential capacity need and actual capacity that a resource currently achieves.
- **1.5.14.7** Optimize Resource Capacity — Improving resource capacity usage by managing underlying and related dependencies and constraints.
- **1.5.14.8** Monitor Resource Capacity — Identifies relevant resource capacity attributes/properties, and monitors and tracks all attributes, their use, and changes.
- **1.5.14.9** Report Resource Capacity — Prepares and presents detailed accounts of all relevant resource capacity information, in a timely manner that is relevant and reliable for use by business.

## SID Entities Manipulated

- [[wiki/sid/resource/resource-capacity-abe]] — direct match. The Resource Capacity ABE (which specialises the canonical Capacity pattern from the Common Domain) is the primary data model this L2 manages: the L2's nine L3s plan, align, gap-analyse, forecast, implement, analyse, optimize, monitor, and report on resource capacity. The same ABE carries an existing back-link from Resource Capability Delivery (1.5.2, with concrete capacity metrics — transaction volumes, storage requirements, traffic volumes, port availabilities — feeding into the capability-delivery flow); this L2 (1.5.14) is the *primary ongoing-management* manipulator vs 1.5.2's *upstream-input* manipulator. Target ABE is `release_status: pre-production` per [[wiki/open-questions#OQ-027]]. The cross-L2 navigation lives on the SID page itself; cross-L2 wikilinks here would trigger bidirectional consistency checks.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). Note: this L2 is **net-new in v25.5** (no R20.5 lineage; Original PID = None) — definitionally cannot appear in GB1022's R20.5-keyed §4.x mapping tables, since GB1022 was scoped operationally and the mapping tables predate the v25.5 introduction of Capacity Management as a discrete L2.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0, so no narrative-PDF supplementation pass is anticipated for this L2 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — net-new-in-v25.5 status of this L2 sharpens the gap)_
