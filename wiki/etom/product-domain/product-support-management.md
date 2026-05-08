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
l2_id: "1.2.4"
l2_name: "Product Support Management"
---

# Product Support Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

Product Support Management processes ensure the support capability is in place to allow the  Product Fulfillment, Assurance and Billing processes to operate effectively.  
The responsibilities of these processes include, but are not limited to:
• Provision of product Inventory process infrastructure 
• Policy support and decision support knowledge for product
• Monitoring and reporting on the capabilities and costs of the individual Product FAB processes
• Longer-term trend analysis on product FAB processes in order to establish the extent to which enterprise targets for these processes are being achieved and/or the need for the processes to be modified.

This Process was renamed in 24.0 Old name was: Product Readiness Support

— GB921 v25.5 Excel master, process ID `1.2.4`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.2.4.3 Support Product Configuration Management

**Extended Description.**

The purpose of the Support Product Configuration Management processes is to ensure that there is capability (for example, information, materials, systems and resource) so that the Product Configuration Management processes can operate effectively when a product needs to be configured by specifying how the product operates or functions in terms of a product’s configurable parameters, collectively called characteristics, and related configurations of products, services, and resources that are part of its overall configuration.

Examples are information on how to handle unusual configuration requests based on temporary situations, systems needed to accept and track product configurations, requests for the provisioning of additional parameters or resources where it has been identified that current available parameters or resources will impact on effective product configuration.

These processes are responsible for implementing generic and specific changes to product configuration capabilities. This support could be in updating configuration scripts, batch procedures, etc.

These processes undertake trend analysis on product configurations, e.g. type, frequency, duration, outcome.

### 1.2.4.4 Support Product Offering Purchasing

**Extended Description.**

The purpose of the Support Product Offering Purchasing processes is to ensure that there is capability (for example, information, materials, systems and resources) so that the Product Offering Purchasing processes can operate effectively when there is an inbound/outbound purchase of one or more product offerings, changes an offering being purchased, or reviewing an entire purchase.

Examples are information on how to handle product purchases including shopping purchases in the form of in-store, shopping cart purchases, window shopping (a form of browsing) and purchases in the form of product (offering) orders that result in a product being delivered to a party or from a party.

These processes are responsible for implementing generic and specific changes to product offering purchasing capabilities. This support could be in updating scripts, batch procedures, etc.

These processes undertake trend analysis on product offerings purchasing, e.g. type, frequency, duration, outcome.

### 1.2.4.5 Enable Product Performance Management

**Extended Description.**

The purpose of the Enable Product Performance Management processes is to ensure that there is capability (for example, information, materials, systems and resources) so that the product performance management processes can operate effectively to manage, track, monitor, analyze, improve and report on the performance of specific products.

Examples are information on how to handle product performance management including performance analysis, statistics, trends, etc.

These processes are responsible for implementing generic and specific changes to product performance management capabilities. This support could be in updating scripts, batch procedures, surveys, etc.

These processes undertake trend analysis on product performance management, e.g. product performance categories, performance trends, overall QoS delivered, outcomes, etc.

### 1.2.4.6 Support Product Rating & Rate Assignment

**Extended Description.**

The purpose of the Support Product Rating & Rate Assignment processes is to make sure that there is capability (for example, information, systems and resources) so that the Charging processes can operate effectively. Examples are information needed to calculate the value of the product e.g. tariffs, price plans, accumulated usage, contracts, etc., information needed to apply the discounts to product prices at an individual product level, information needed to accumulate items for rating and information on how to manage the assignment relationships with Billing Account.

These processes undertake trend analysis on charging.

### 1.2.4.7 Support Product Usage Mgt

**Extended Description.**

The purpose of the Support Product Usage Mgt process is to make sure that there is capability (for example, information, systems and resources) so that the Product Usage Mgt process can operate effectively. For example the Product Usage records (aka billing events) to process, the information needed to enrich the Product Usages (e.g. customer, product, or other reference data, price), the schema to reformat the Product Usage records.

These processes undertake trend analysis on billing events management.

### 1.2.4.8 Support Product Balance Management

**Extended Description.**

The purpose of the Support Product Balance Management process is to make sure that there is capability (for example, information, systems and resources) so that the Support Product Balance Management process can operate effectively. For example policy defined to mange balance (e.g. minimum allowable balance limit, balance expiration dates), account information needed to operating the balance.

These processes undertake trend analysis on balance management.

### 1.2.4.9 Manage Product Test

**Extended Description.**

Manage Product Test processes manage the end-to-end execution of a test or test scenario for products not specific to a customer. Tests can be manual or automated.

Product Test Management processes rely on Service Test Management and Resource Test Management processes due to dependencies between product tests, service tests and resource tests.

Product Test Management includes:

- Identification of product tests needed according to fulfilment and assurance issues

- triggering of product tests in manual or automated mode

- Execution of product tests

- Verification of test authorization (role and context) and quota management

- Identification and prioritization of tests

- Setting up the test context and configuration

- Triggering appropriate service resource Tests

- Tests can be on-demand or planned according to specific needs

- Enrichment with service and resource tests results based on applicable product test rules

- Reporting of test results

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.4.3** Support Product Configuration Management — Support Product Configuration Management ensures that all information, materials, systems and resources are available so that the Product Configuration Management processes can operate effectively.
- **1.2.4.4** Support Product Offering Purchasing — Support Product Offering Purchasing ensures that all information, materials, systems and resources are available so that the Product Offering Purchasing processes can operate effectively.
- **1.2.4.5** Enable Product Performance Management — Enable Product Performance Management ensures that all information, materials, systems and resources are available so that the Product Performance Management processes can operate effectively.
- **1.2.4.6** Support Product Rating & Rate Assignment — Ensure that all information and systems are available so that the Product Rating & Rate Assignment processes can be completed without delay.
- **1.2.4.7** Support Product Usage Mgt — Ensure that all information and systems are available so that the Product Usage Mgt process can be completed without delay.
- **1.2.4.8** Support Product Balance Management — Ensure that all information and systems are available so that the Product Balance Management processes can be completed without delay.
- **1.2.4.9** Manage Product Test — Manage Product Test processes manage the end-to-end execution of a test or test scenario for products not specific to a customer.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Product Process Decompositions PDF (GB921_Product_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.
