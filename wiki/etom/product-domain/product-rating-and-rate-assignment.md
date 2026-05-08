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
l2_id: "1.2.17"
l2_name: "Product Rating & Rate Assignment"
---

# Product Rating & Rate Assignment

> **Vertical context:** Billing ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

The purpose of Product Rating & Assignment is to rate a value (monetary or other) to Product Usage or a set of Product Usages and assign the result to a Product and a Billing Account. The charge may be either a credit or a debit and can be handled either online or offline.

Online charging is performed in real-time, requiring an authorization component which may affect how the service is rendered and enables an operator to provide prepaid services to its customers. Whereas offline charging is performed after the service is rendered and is not required to be done in real-time and generally relates to subscription based products.

— GB921 v25.5 Excel master, process ID `1.2.17`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.2.17.1 Perform Rating

**Extended Description.**

Process responsible for calculating the value of a product usage or a set of product usages, before, during or after the rendering of the service, based on parameters of the request (type, quantity, etc.), parameters of the customer/subscriber (tariffs, price plans, accumulated usage, contracts, etc.) and other parameters (time-of-day, taxes, etc.). The same request maybe rated differently for different subscribers based on their purchased offers or agreements.

### 1.2.17.2 Aggregate Items For Rate Assignment

**Extended Description.**

This process is responsible for accumulating contributing items, which can be quantities, values (monetary or other) or both. Aggregation can occur over time or can be initiated to gather a “snapshot” of the items at a point in time.

### 1.2.17.3 Manage Customer Assignment Hierarchy

**Extended Description.**

Customer hierarchies are commonly used for corporate customers, family plans or other type of affinity groups. This process manages the assignment relationships among subscribers, e.g. sharing, inheriting or restricting balances, price plans and discounts. Thereby assuring that a charge is added to or subtracted from the correct account balance.

### 1.2.17.4 Provide Advice of Rate

**Extended Description.**

The activity of Provide Advice of Rate (aka Advice of Charge) is responsible for providing advice on rates, in real-time or offline, an estimate or value of the rate for a specific usage request. The advice is usually based upon performing a full rating process for the request.

### 1.2.17.5 Apply Rate Level Discounts

**Extended Description.**

This process applies discounts to product prices at an individual product level. A discount may be expressed as a monetary amount or percentage, and modifies a price for a product. When a discount is expressed as a percentage, the discounting process determines the discount calculated in relation to the price for the product.

The discount may be displayed as a separate entry on the bill or may be combined with the rate for the product to only show as one entry.

Discounts may be a one-time event or may have some duration (days, months, life of product, etc.). Discounts may apply to a specific customer or be generally available based on selection of products (for example - bundles). Discounting structures may involve tiers, tapers, or thresholds.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.17.1** Perform Rating — Calculating the value of a product usage or a set of product usages, before, during or after the rendering of the service.
- **1.2.17.2** Aggregate Items For Rate Assignment — Manages the accumulation of items that may be used in the selection of a value or in calculation of a rate/discount.
- **1.2.17.3** Manage Customer Assignment Hierarchy — Managing the charging relationships among subscribers.
- **1.2.17.4** Provide Advice of Rate — Provide advice of rate.
- **1.2.17.5** Apply Rate Level Discounts — Applies discounts to product prices.

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
