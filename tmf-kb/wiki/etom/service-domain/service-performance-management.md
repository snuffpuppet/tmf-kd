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
l1_parent: "1.4 Service Domain"
l2_id: "1.4.7"
l2_name: "Service Performance Management"
---

# Service Performance Management

> **Vertical context:** Assurance ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Performance Management business process directs and controls activities that define Service Performance Objectives (e.g. Service Availability, Service Quality, Process efficiency, Service Reliability, etc.), sets performance goals & targets, track performance trends, monitor performance, analyze performance, control performance (optimize, troubleshoot), report or communicate performance, and manage consequences of service performance. Service Performance Management business process support the Enterprise Performance Management goals. These goals include quality, efficiency, reliability, availability, monetary (cost, profitability, etc.) mandates along with any productivity requirement of service delivery and service engagement by the organization. It includes identifying, establishing the applying the methodologies that define and manage service performance criteria to meet business objectives.
This process was renamed in 23.5 it was named Service Quality Management

— GB921 v25.5 Excel master, process ID `1.4.7`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.7.6** Manage Service Performance Requirement — Manage Service Performance Requirement business activity controls activities and underlying tasks that define the performance requirements for a service. It sets the standards and expectations for service performance.
- **1.4.7.7** Manage Service Performance Plan — Manage Service Performance Plan business activity controls the creating, implementing, improving, and terminating of plan(s) for service performance.
- **1.4.7.8** Manage Service Performance Measure — Manage Service Performance Measure business activity controls the definition, change, and removal of measures for service performance.
- **1.4.7.9** Manage Service Performance Analysis — Manage Service Performance Analysis business activity controls activities and tasks supporting assessment, investigating, auditing, and reporting on service performance.
- **1.4.7.10** Manage Service Performance Control — Manage Service Performance Control business activity is responsible for monitoring, evaluating, and improving service performance.
- **1.4.7.11** Manage Service Performance Reporting — Manage Service Performance Reporting business activity is responsible for creating, changing, and publishing reports on service performance.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.
