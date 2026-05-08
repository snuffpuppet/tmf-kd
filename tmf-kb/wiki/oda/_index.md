# ODA

Open Digital Architecture component pages, sourced from the canonical
**GB1022 ODA Functional Architecture Guidebook v1.1.0** (Production / TM Forum
Approved). Six Functional Blocks plus the architectural Systems of Separation
grouping.

## Functional Blocks

[[wiki/oda/functional-blocks/_index|Browse functional blocks]] — 6 components
(Decoupling & Integration, Engagement Management, Party Management, Core Commerce
Management, Production, Intelligence Management).

## ODA Domains (alternate / future structure)

ODA component decomposition beyond the 6 high-level Functional Blocks (e.g.
finer-grained components within each block, the ODA Component Catalog) lives in
other TMF documents (e.g. IG1171 ODA Component Definition — referenced in GB1022
§5.3 — not currently in the corpus). For v1, the 6 Functional Blocks are the
canonical ODA decomposition the corpus represents.

## IG1167 Proposed Extensions

**Source:** `raw/tmf/oda/IG1167_ODA_Functional_Architecture_Exploratory_Report_v6.0.0.pdf`
(Production / TM Forum Approved, v6.0.0, 2021).

IG1167 is a TMF **Exploratory Report** that proposes extensions and changes on top
of the canonical GB1022 ODA Functional Architecture. Per §3 of IG1167: "Reference
GB1022 ODA Functional Architecture Guidebook" — IG1167 is explicitly built on the
GB1022 baseline (now in this corpus, see above).

### IG1167 §7 — NEW BUSINESS INFORMATION OBJECTS

> Per IG1167 §7 intro: "The section captures the proposals to extend or advance the
> Functions. Each section captures the new proposals." Each subsection further notes:
> "For the currently adopted standards … please refer to GB1022 ODA Functional
> Architecture Guidebook v2.0.0."

The IG1167 §7 sub-sections per ODA Functional Block:

| § | Block | Status of proposed extensions |
|---|-------|-------------------------------|
| 7.1 | [[wiki/oda/functional-blocks/decoupling-and-integration]] | New functionalities (Table 1) — most marked TBD |
| 7.2 | [[wiki/oda/functional-blocks/engagement-management]] | New EM block functionalities (Table 2) |
| 7.3 | [[wiki/oda/functional-blocks/party-management]] | New PM functionalities (Table 3); New Mappings/CRs to eTOM (Table 4); New Mappings/CRs to SID (Table 5); New Mapping to Functional Framework — *Ongoing Study*; New Reference Interfaces — *Ongoing Study* |
| 7.4 | [[wiki/oda/functional-blocks/core-commerce-management]] | New CCM functionalities (Table 6); New Mappings/CRs to eTOM (Table 7); New Mappings/CRs to SID (Table 8); New Reference Interfaces (Table 9) |
| 7.5 | [[wiki/oda/functional-blocks/production]] | New Mappings/CRs to eTOM (Table 10); New Mappings/CRs to SID (Table 11); New Reference Interfaces (Table 12) |
| 7.6 | [[wiki/oda/functional-blocks/intelligence-management]] | New IM functionalities (Table 14); New Mappings/CRs to eTOM (Table 12); New Mappings/CRs to SID (Table 13); New Reference Interfaces (Table 16) |

### IG1167 §8–§11 (other content)

- **§8 Deployment Scenarios** — five real-world examples (Orange Production Factory,
  Telefonica E2E Service Model, Telstra NaaS / Operational Domain Management,
  Microsoft Azure model, Reference to TR262 Platform-based Model, ETSI ZSM Model)
- **§10 Detailed Intelligence Management Implementation** (Appendix A) — deployment
  flavors, ODA Knowledge Plane, ETSI GANA Framework instantiation
- **§11 Business Scenarios / Use Case** — ODA and legacy BSS/OSS, Federation of ODA

### How to read IG1167 vs GB1022 in this corpus

- **GB1022 (canonical):** the established ODA Functional Architecture. Used as the
  source for the 6 ODA Functional Block pages in `wiki/oda/functional-blocks/`.
- **IG1167 (exploratory, this section):** proposes additions/changes. Many entries
  in IG1167's tables are explicitly marked "TBD" or "Ongoing Study" — the document is
  a working report, not a settled standard. Where IG1167 makes concrete proposals
  (e.g. §7.5 Production §7.5.2 SID Mapping table), those are mapping proposals from
  the IG1167 working group, not yet incorporated into the canonical GB1022 model.
- **Recommendation for mapping work:** start from the canonical block pages
  ([[wiki/oda/functional-blocks/_index]]). Consult IG1167 directly (extracted at
  `raw/extracted/tmf/oda/IG1167_..._v6.0.0.md`) for proposed extensions when relevant.
  Treat IG1167's §7 mapping tables as proposals to inspect — not as established
  ODA-to-eTOM/SID mappings.

See [[wiki/open-questions#OQ-039]] for the IG1167 ingest summary.
