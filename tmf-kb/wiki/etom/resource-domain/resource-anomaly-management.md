---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.21"
l2_name: "Resource Anomaly Management"
---

# Resource Anomaly Management

> **Vertical context:** Assurance ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Anomaly Management business processes establish actions that predict and detect aberrations or outlier events/activities, assess them for their impact, mitigate them, and record them before they ever become Resource Problem Management concerns. 
By establishing that an action or event is abnormal (based on known patterns), Resource Anomaly Management helps to assess them through a set of activities that may triage, plan detailed assessment, classify them and provide mitigatory actions for them. Through Resource Anomaly Management, assurance of Products, based on abnormal events or activities can be well categorized, prioritized and actioned on. Resource Anomaly Management is different from Resource Problem Management as the later addresses known issues, faults or problems.

— GB921 v25.5 Excel master, process ID `1.5.21`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.21.1** Predict Resource Anomaly — Predict Resource Anomaly business activity is in charge of declaring or indicating in advance (or foretells on the basis of resource delivery observations, resource use experience or resource management reasons) upcoming exceptions, as well as trends that can lead to outlier activities / events or resource problems.
- **1.5.21.2** Detect Resource Anomaly — Detect Resource Anomaly business activity identify Resource delivery activities that are a deviation (aberrations or abnormal actions/events) from well-define norms or expectations.
- **1.5.21.3** Assess Resource Anomaly — Assess Resource Anomaly business activity check, estimate, appraise and evaluate Resource anomaly observations to determine implications and follow-on treatment.
- **1.5.21.4** Mitigate Resource Anomaly — Mitigate Resource Anomaly business activity is in charge of allaying or alleviate the impact of a product’s anomalous exception.
- **1.5.21.5** Manage Resource Anomaly Learning — Manage Resource Anomaly Learning business activity is in charge of capturing, or acquiring knowledge and skill related to handled anomalous exceptions (from detection, through assessment to mitigation).

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Resource Process Decompositions PDF (GB921_Resource_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.
