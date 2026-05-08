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

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.2.5.1 Product Configuration Management Plan

**Extended Description.**

Product Configuration Management Plan business activity anticipate future product configuration changes and establish the product configuration management strategy for managing and auditing product configurations.

The Product Configuration Management Plan business activity helps to identify and create configuration items, support controlling and release of configuration items, define and establish reporting, set courses of action for managing configuration status, establish completeness criteria, defined requirements for managing consistency and correctness of configuration items, and the plans to control storage, handling and delivery of product configuration items.

**L4 sub-processes:**

- **1.2.5.1.1** Develop Product Configuration Policy — Develop Product Configuration Policy business activity is in charge of defining the product configuration policy that governs the use of a product configuration.
- **1.2.5.1.2** Establish Product Configuration Management Plan — Establish Product Configuration Management Plan business activity sets up the course of action that will support managing and auditing product configuration items.

### 1.2.5.2 Manage Product Configuration

**Extended Description.**

Manage Product Configuration business activity is in charge of creating, maintaining, controlling, changing and reporting Product Configuration according to Product Configuration Plans.

Manage Product Configuration will establish and maintaining consistency of a product's performance, functional, and physical attributes within the limits defined by product requirements, product design, and operational information throughout the Products Lifecycle.

**L4 sub-processes:**

- **1.2.5.2.1** Create Product Configuration — Create Product Configuration business activity handle configuration of Product configuration (configuration items). This includes creating configuration constraints, configuration relationships and their associations.
- **1.2.5.2.2** Control Product Configuration — Control Product Configuration business activity check, determine and direct product configuration change and use.
- **1.2.5.2.3** Maintain Product Configuration — Maintain Product Configuration business activity handles preserving active product configurations states to support product performance.
- **1.2.5.2.4** Change Product Configuration — Change Product Configuration business activity handles changes to product configuration.
- **1.2.5.2.5** Monitor Product Configuration — Monitor Product Configuration business activity handles monitoring product configurations, changes and/or use.
- **1.2.5.2.6** Report Product Configuration — Report Product Configuration business activity handles reporting and status accounting of product configuration changes and/or use.

### 1.2.5.3 Audit Product Configuration

**Extended Description.**

Audit Product Configuration business activities examine and verify product configurations for compliance to assurance needs.

Audit Product Configuration perform audits that compare the "as built" and "as planned" versions of configuration items, investigate discrepancies, and take action on the results. Audit Product Configuration supports Enterprise Audit Management, Enterprise Risk Management and Enterprise Governance.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

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

- [[wiki/oda/functional-blocks/core-commerce-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Product Process Decompositions PDF (GB921_Product_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.
