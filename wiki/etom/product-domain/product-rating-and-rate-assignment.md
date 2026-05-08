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
