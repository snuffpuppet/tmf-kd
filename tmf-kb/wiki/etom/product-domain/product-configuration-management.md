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
l1_parent: "1.2 Product Domain"
l2_id: "1.2.5"
l2_name: "Product Configuration Management"
---

# Product Configuration Management

> **Vertical context:** Fulfillment ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

Configuration Management configures or creates a new version of a configuration for an entity, such as a product, service, or resource, as defined by  a configuration specification. This process also modifies a configuration and values for configuration parameters, and removes a configuration.
The configuration of one entity may be required the configuration of other entities as defined by a selected configuration specification to use.  For example, the configuration of a product may require the configuration of a service and a physical resource, such as a device.

— GB921 v25.5 Excel master, process ID `1.2.5`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.5.1** Product Configuration Management Plan — Product Configuration Management Plan business activity anticipate future product configuration changes and establish the product configuration management strategy for managing and auditing product configurations.
- **1.2.5.2** Manage Product Configuration — Manage Product Configuration business activity is in charge of creating, maintaining, controlling, changing and reporting Product Configuration according to Product Configuration Plans.
- **1.2.5.3** Audit Product Configuration — Audit Product Configuration business activities examine and verify product configurations for compliance to assurance needs.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Product Process Decompositions PDF (GB921_Product_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.
