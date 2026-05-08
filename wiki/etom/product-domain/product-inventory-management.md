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
l2_id: "1.2.11"
l2_name: "Product Inventory Management"
---

# Product Inventory Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

The purpose of the Manage Product Inventory processes are twofold:

	Establish, manage and administer the enterprise's product inventory, monitor and report on the usage and access to the product inventory, and the quality of the data maintained in it. The product inventory maintains records of all products, their interactions with the enterprise, and any other product related
	Provide available Product Inventory related information required to support Fulfillment, Assurance and Billing & Revenue processes.

The product inventory is also responsible for maintaining the association between customers and purchased product instances, created as a result of the Order Handling processes for a Product Specification in the context of a Product Offering.
Managing product inventory includes product creation, modification to the product inventory.
Responsibilities of these processes include, but are not limited to:

	Identifying the inventory-relevant information requirements to be captured for products;
	Identifying, establishing and maintaining product inventory repository facilities; 
	Establishing and managing the product inventory management and information capture processes;
	Managing the registration and access control processes that enable processes to create, modify and/or look up product information to and from the product inventory;
	Ensuring the product inventory repository accurately captures and records all identified product details, through use of automated or manual audits;
	Tracking and monitoring of the usage of, and access to, the product inventory repository and associated costs, and reporting on the findings;
	Identifying any technical driven shortcomings of the product inventory repository, and providing input to Resource Development & Management processes to rectify these issues.

— GB921 v25.5 Excel master, process ID `1.2.11`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.2.11.1 Identify Relevant Product Inventory Information

**Extended Description.**

Not used for this process element

### 1.2.11.2 Maintain Product Inventory facilities

**Extended Description.**

Not used for this process element

### 1.2.11.3 Control Product Inventory Access

**Extended Description.**

Not used for this process element

### 1.2.11.4 Ensure Product Inventory Quality

**Extended Description.**

Ensuring the product inventory repository accurately captures and records all identified product details, through use of automated or manual audits. Monitoring and reporting on the quality of the information maintained in the inventory. The product inventory maintains records of all products, their interactions with the enterprise, and any other product related- information, required to support CRM and other processes. The product inventory is also responsible for maintaining the association between customers and purchased product instances, created as a result of the Order Handling processes.

### 1.2.11.5 Track Product Inventory Usage

**Extended Description.**

Not used for this process element

### 1.2.11.6 Identify Product Inventory Shortcomings

**Extended Description.**

Not used for this process element

### 1.2.11.7 Product Lifecycle Management Support

**Extended Description.**

Product Lifecycle Management Support supports the management of the lifecycle of a product and pricing associated with a product.

It can create a product, specify the involvement one or more parties have with it, updates information about the product including the status and relationships with Product Specification, Product Offering, Account and all related roles.

The lifecycle of a product also includes prices associated with it which are also managed by this process.

**L4 sub-processes:**

- **1.2.11.7.1** Product Lifecycle Administration Support — Create a product, specify the involvement one or more parties have with it, update information about the product, and remove the product when it is no longer of interest to an enterprise and/or the primary party responsible for the product at request from Operations processes.
- **1.2.11.7.2** Product Pricing — Apply, update, and remove a price associated with a product.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.11.1** Identify Relevant Product Inventory Information — Identifying the inventory-relevant information requirements to be captured for products.
- **1.2.11.2** Maintain Product Inventory facilities — Identifying, establishing and maintaining product inventory repository facilities.
- **1.2.11.3** Control Product Inventory Access — Managing the registration and access control processes that enable processes to create, update and/or look up product information to and from the product inventory.
- **1.2.11.4** Ensure Product Inventory Quality — Not used for this process element.
- **1.2.11.5** Track Product Inventory Usage — Tracking and monitoring of the usage of, and access to, the product inventory repository and associated costs, and reporting on the findings.
- **1.2.11.6** Identify Product Inventory Shortcomings — Identifying any technical driven shortcomings of the product inventory repository, and providing input to Resource Development & Management processes to rectify these issues.
- **1.2.11.7** Product Lifecycle Management Support — Support the management of the lifecycle of a product and pricing associated with a product in the Product Inventory.

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
