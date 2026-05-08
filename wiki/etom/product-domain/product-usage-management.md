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
l2_id: "1.2.16"
l2_name: "Product Usage Management"
---

# Product Usage Management

> **Vertical context:** Billing ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

The Product Usage management processes encompass the functions required to guide, distribute, mediate, summarize, accumulate, and analyze Product Usage records. These processes may occur in real-time, near real-time (i.e. just at the end of the usage), or may be executed on a periodic basis.

Based on Service Usage, this process aims at identifying Product Usage. For example, for a Video on Demand where you can watch a video as many time as you want during 72 hours, several Service Usages might have been tracked (each time the user watches the video) and only one Product Usage will be identified for all Service Usages in the 72 hours after the first watch.

The guiding processes ensures that the Product Usage records used in the billing processes are appropriately related to the correct customer billing account and products. 

The Product Usage records are edited and if necessary reformatted (mediated) to meet the needs of subsequent processes. The billing event records may also be enriched with additional data during this process.

— GB921 v25.5 Excel master, process ID `1.2.16`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.16.1** Enrich Product Usages — Enrich product usage records with additional data.
- **1.2.16.2** Guide and Assign Product Usages — Ensures that the product usage records used in the billing processes are related to the correct customer billing account and subscribed products.
- **1.2.16.3** Mediate Product Usages — Edits and reformats data for recipient applications.
- **1.2.16.4** Report Product Usage Records — Generate reports on product usage records based on requests from other processes.

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
