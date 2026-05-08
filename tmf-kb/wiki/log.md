# TMF Knowledge Base — Event Log

Append-only. Every ingest, lint run, open-question filing, and resolution is recorded here.
Never edit existing entries. Format defined in [[CLAUDE]] §9.

---

## 2026-05-08T12:40Z — ASSESSMENT (ingest paused before page creation)

- **File(s):** `raw/tmf/oda/IG1167_ODA_Functional_Architecture_Exploratory_Report_v6.0.0.pdf`
- **Pages created/updated:** none — ingest paused at workflow step 4 (page creation)
- **Sections skipped (out of scope):** N/A — full document was not ingested
- **Lint result:** PASS (baseline state preserved; no new wiki pages produced)
- **Open questions filed:** none
- **Notes:**
    - Source extracted to `raw/extracted/tmf/oda/IG1167_ODA_Functional_Architecture_Exploratory_Report_v6.0.0.md`
      using `pdftotext -layout` (poppler 26.04.0). Extraction clean: 78 pages → 2693 lines.
    - Document GA status confirmed via PDF metadata: "Release Status: Production",
      "Approval Status: TM Forum Approved". Version 6.0.0 (May 2021).
    - **Material finding:** §3 (line 416) reads "Reference GB1022 ODA Functional
      Architecture Guidebook." IG1167 is an exploratory/extension document built on top
      of GB1022, which is the canonical ODA Functional Architecture reference. IG1167's
      §7 ("NEW BUSINESS INFORMATION OBJECTS") proposes Change Requests (CRs) against
      eTOM and SID for five Function Blocks: Engagement Management, Party Management,
      Core Commerce Management, Production, Intelligence Management.
    - **Decision:** pause IG1167 ingest until canonical sources are available.
      Ingesting an extension document before its canonical baseline would corrupt the
      corpus's normative integrity (proposed CRs would read as established mappings).
    - **Planned ingest order:**
        1. GB991 — TMF Core Frameworks Concepts and Principles (foundations)
        2. GB922 — SID (data layer foundation; provides Product/Service/Resource/Common ABE entities)
        3. GB921 — eTOM (process layer; can link SID entities)
        4. GB1022 — canonical ODA Functional Architecture Guidebook (component layer; can link both)
        5. IG1167 (this document) — properly attributed as exploratory extensions on top of GB1022
    - **Extraction tool settled:** `pdftotext -layout` from poppler (recorded in CLAUDE.md §2).

---

## 2026-05-08T13:30Z — INGEST (GB991 foundations)

- **File(s):** `raw/tmf/foundations/GB991_TMForum_Core_Frameworks_Concepts_and_Principles_v25.5.pdf`
- **Pages created/updated:**
    - `wiki/foundations/_index.md` (new)
    - `wiki/foundations/domains.md` (new)
    - `wiki/foundations/lifecycle.md` (new)
    - `wiki/foundations/business-process-framework.md` (new)
    - `wiki/foundations/information-framework.md` (new)
    - `wiki/foundations/functional-framework.md` (new)
    - `wiki/foundations/principles.md` (new)
    - `wiki/index.md` (updated — added Foundations section)
    - `wiki/open-questions.md` (updated — OQ-001 through OQ-007 filed)
- **Sections skipped (out of scope):**
    - GB991 §1.2 (Business Capability Map) — marked FUTURE WORK in source
    - GB991 §1.6 (Metrics) — marked FUTURE WORK in source
    - GB991 §2.2.1 (Business Capability principles) — marked FUTURE WORK in source
    - GB991 §2.2.5 (Metrics principles) — marked FUTURE WORK in source
    - GB991 §3 (The Frameworks) — overlaps §1.3–§1.5, deferred to later ingest if needed
    - GB991 §4 (Methodology) — procedural content, deferred
    - GB991 §5 (Meta Models) — abstract, deferred
    - GB991 §6 (Administrative Appendix) — admin metadata, out of corpus scope
- **Lint result:** see next entry
- **Open questions filed:** OQ-001 (Sles typo), OQ-002 (business vs non-business
  domains), OQ-003 (INF principle numbering gap), OQ-004 (FUF principles transitional),
  OQ-005 (§1.2 FUTURE WORK), OQ-006 (§1.6 + §2.2.5 FUTURE WORK), OQ-007 (§2.2.1 FUTURE WORK)
- **Notes:**
    - Schema additions: introduced `foundation` page type. CLAUDE.md §5.4 (anatomy),
      §6 (frontmatter), §7 (trilateral exemption), §11 (directory tree) all updated.
      Linter (`lint/lint.py`) updated with `foundation` entries in REQUIRED_FRONTMATTER,
      REQUIRED_HEADINGS, TRILATERAL_SECTIONS. Template `templates/foundation.md` added.
    - Source extracted to `raw/extracted/tmf/foundations/GB991_TMForum_Core_Frameworks_Concepts_and_Principles_v25.5.md`.
      49 pages → 1892 lines. Extraction clean.
    - GB991 v25.5 GA status confirmed: "Release Status: Production", "Approval Status:
      TM Forum Approved".
    - PSR (Product, Service, Resource) is now visible in the corpus as three of the 11
      horizontal domains defined in §1.1.1. Foundation pages serve as the cross-framework
      vocabulary other layers will link to.
    - Cross-framework Application sections on each foundation page are intentionally
      empty — they will be populated as eTOM, SID, and ODA pages are ingested and
      reference foundation concepts.

---

## 2026-05-08T14:15Z — INGEST (GB922 Product SID)

- **File(s):** `raw/tmf/sid/GB922_Product_v25.5.pdf`
- **Pages created/updated:**
    - `wiki/sid/product/product-party-roles-abe.md` (new)
    - `wiki/sid/product/product-specification-abe.md` (new)
    - `wiki/sid/product/product-offering-specification-abe.md` (new)
    - `wiki/sid/product/product-and-offering-instance-abe.md` (new)
    - `wiki/sid/product/product-order-abe.md` (new)
    - `wiki/sid/product/product-usage-abe.md` (new)
    - `wiki/sid/product/loyalty-abe.md` (new)
    - `wiki/sid/product/product-configuration-abe.md` (new)
    - `wiki/sid/product/product-test-abe.md` (new)
    - `wiki/sid/product/product-capacity-abe.md` (new)
    - `wiki/sid/product/product-performance-abe.md` (new, notFullyDeveloped)
    - `wiki/sid/product/strategic-product-portfolio-plan-abe.md` (new, notFullyDeveloped)
    - `wiki/sid/product-abe.md` (updated — populated category landing)
    - `wiki/sid/product/_index.md` (updated — populated entities listing)
    - `wiki/index.md` (updated — SID Product section populated)
    - `wiki/open-questions.md` (updated — OQ-008 through OQ-013 filed)
- **Sections skipped (out of scope):**
    - GB922 Product §1 General Information, §2 Typographic Conventions, §3 Glossary,
      §5 Administrative Appendix — administrative metadata, not corpus content
    - All chapter §4 detail beyond ABE overview level (per ABE-level granularity
      decision, see CLAUDE.md §5.2; full attribute tables and figure-level detail
      remain in source for future deepening)
- **Lint result:** see next entry
- **Open questions filed:**
    - OQ-008 (shared trilateral gap: eTOM/ODA layers not yet ingested)
    - OQ-009 (BE-level detail deferred per v1 granularity)
    - OQ-010 (`plannedOrActutalCapacity` source typo)
    - OQ-011 (Product Performance ABE notFullyDeveloped)
    - OQ-012 (Strategic Product Portfolio Plan ABE notFullyDeveloped)
    - OQ-013 (Strategy-to-Readiness ABE relevance to operational mapping)
- **Notes:**
    - Schema clarification: CLAUDE.md §5.2 updated to formalise ABE-level granularity
      for v1 (one wiki page per top-level ABE; sub-ABEs and BEs become anchored
      sub-sections).
    - Source extracted to `raw/extracted/tmf/sid/GB922_Product_v25.5.md` using
      `pdftotext -layout`. 268 pages → 8364 lines. Extraction clean.
    - GB922 Product v25.5 GA confirmed via PDF metadata: "Maturity Level: General
      availability (GA)", "Release Status: Production", "Approval Status: TM
      Forum-Approved", "Suitable for Conformance".
    - 12 ABEs covered (§4.1–§4.12 of source). Two are tagged «notFullyDeveloped» by
      the source itself.
    - All 12 ABE pages cite OQ-008 in their trilateral sections; this single shared
      open question replaces the ~24 individual gap-OQs that would otherwise be filed.
    - Cross-framework Application (foundation pages) NOT updated this ingest — SID
      Product entities reference foundation concepts (Domains, Information Framework,
      ABE) but the foundation pages' "Cross-Framework Application" sections will be
      populated in a sweep after eTOM and ODA are also ingested. Avoiding partial
      population now reduces churn.
    - Three SID PDFs remain (Service v25.0, Common v23.0, Resource v25.5 pre-prod).
      Per agreed sequence, these are the next ingest events.

---

## 2026-05-08T15:00Z — INGEST (GB922 Common SID)

- **File(s):** `raw/tmf/sid/GB922_Common_v23.0.pdf`
- **Pages created/updated:**
    - 19 new ABE pages in `wiki/sid/common/` (Party, Party Privacy, Party Payment,
      Communication Interaction, Digital Identity, Calendar, Location, Base Types,
      Root Business Entities, Account, Business Interaction, Agreement, Capacity,
      Catalog, Configuration and Profiling, Metric, Performance, Policy, Project)
    - `wiki/sid/common-abe.md` (updated — populated category landing)
    - `wiki/sid/common/_index.md` (updated — populated entities listing)
    - `wiki/index.md` (updated — SID Common section populated)
    - `wiki/open-questions.md` (updated — OQ-014 through OQ-021 filed)
- **Sections skipped (out of scope):**
    - GB922 Common §1 General Information, §2 Typographic Conventions, §3 Glossary,
      §5 Administrative Appendix — administrative metadata, not corpus content
    - §4.1, §4.2, §4.3 figure-only organisational sections (Common/Pattern/Shared
      Level 1 diagrams) — referenced in OQ-014 for sub-domain context but not
      ingested as standalone pages
    - All chapter §4.4–§4.22 detail beyond ABE overview level (per ABE-level
      granularity decision; full attribute tables, BE-level definitions, and figure
      detail remain in source for future deepening). Several ABEs (Root Business
      Entities at 131 pages, Metric at 110 pages, Project at 170 pages, Location at
      79 pages) flagged with their own OQs for follow-up depth.
- **Lint result:** see next entry
- **Open questions filed:** OQ-014 (sub-domain split deferred), OQ-015
  ("authentification" verbatim), OQ-016/017/018/019/020 (BE-level depth deferrals
  per ABE), OQ-021 (Project ABE mapping relevance)
- **Notes:**
    - Source extracted to `raw/extracted/tmf/sid/GB922_Common_v23.0.md`. 931 pages
      → 34,043 lines. Largest extraction in the corpus to date. Extraction clean.
    - GB922 Common v23.0 GA confirmed: "Maturity Level: General availability (GA)",
      "Release Status: Production", "Approval Status: TM Forum Approved", "Suitable
      for Conformance".
    - 19 ABEs covered (§4.4–§4.22 of source). All trilateral sections reference
      OQ-008 (the shared eTOM/ODA gap from Product ingest).
    - Important findings: §4.12 (Root Business Entities) provides the foundational
      class hierarchy that almost every other SID entity inherits from. §4.16
      (Capacity), §4.17 (Catalog), and §4.18 (Configuration and Profiling) are the
      canonical models specialised by Product (and to-be-ingested Service/Resource).
      Several Product ABE pages (e.g. Product Capacity, Product Configuration) now
      have proper cross-references to their Common-domain parents.
    - **Granularity caveat:** the ABE-level v1 granularity is honest about scope —
      this ingest captures structural understanding for mapping work, not exhaustive
      reference. For specific BE/attribute lookups during mapping, the user consults
      the source PDF (with raw/extracted/ markdown as a navigable companion).
    - Two SID PDFs remain (Service v25.0, Resource v25.5 pre-prod). Service is
      next; Resource needs `release_status` schema field added before ingest.

---

## 2026-05-08T15:30Z — INGEST (GB922 Service SID)

- **File(s):** `raw/tmf/sid/GB922_Service_v25.0.pdf`
- **Pages created/updated:**
    - 12 new ABE pages in `wiki/sid/service/` (Service Party Roles, Service
      Specification, Service, Service Configuration, Service Order, Service Usage,
      Service Test, Service Performance, Service Capacity, Service Problem, Service
      Strategy & Plan, TIP Service Management)
    - `wiki/sid/service-abe.md` (updated — populated category landing)
    - `wiki/sid/service/_index.md` (updated — populated entities listing)
    - `wiki/index.md` (updated — SID Service section populated)
    - `wiki/open-questions.md` (updated — OQ-022 through OQ-026 filed)
- **Sections skipped (out of scope):**
    - GB922 Service §1 General Information, §2 Typographic Conventions, §3 Glossary,
      §5 Administrative Appendix — administrative metadata
    - §4.1 Service Domain Overviews (organisational figures only)
    - All chapter §4.2–§4.13 detail beyond ABE overview level (per ABE-level
      granularity decision)
- **Lint result:** see next entry
- **Open questions filed:**
    - OQ-022 (Network Service Spec / Usage Volume Service Spec «Preliminary»)
    - OQ-023 (Service Performance work-in-progress)
    - OQ-024 (Service Problem «NotFullyDeveloped» — partial blocker for production-side
      fault mapping)
    - OQ-025 (Service Strategy & Plan «notFullyDeveloped» + scope question)
    - OQ-026 (TIP Service Management «likelyToBeDepreciated» — flagged for v25.5
      removal)
- **Notes:**
    - Source extracted to `raw/extracted/tmf/sid/GB922_Service_v25.0.md`. 177 pages
      → 6188 lines. Extraction clean.
    - GB922 Service v25.0 GA confirmed: "Maturity Level: General Availability (GA)",
      "Release Status: Production", "Approval Status: TM Forum Approved", "Suitable
      for Conformance".
    - **Direct PSR mapping relevance.** §4.3 (Service Specification) and §4.4
      (Service) introduce the **CFS/RFS distinction** — CustomerFacingService
      (commercial layer) vs ResourceFacingService (production/technical layer). The
      source explicitly notes that allowing RFS to aggregate CFS "destroys the point
      of separating them in the first place" — this is the architectural separation
      the corpus's PSR mapping goal targets. Both pages prominently flag this.
    - Service ABEs specialise canonical Common ABEs: Configuration (§4.5 → Common
      §4.18), Test (§4.8 → Common §4.9-area), Capacity (§4.10 → Common §4.16). All
      three Service pages link back to their canonical parents.
    - 1 SID PDF remains: Resource v25.5 pre-prod (429 pages). Needs `release_status`
      schema field added to CLAUDE.md §6 and lint.py before ingest.

---

## 2026-05-08T16:00Z — INGEST (GB922 Resource SID, pre-production)

- **File(s):** `raw/tmf/sid/GB922_Resource_v25.5.pdf`
- **Pages created/updated:**
    - 13 new ABE pages in `wiki/sid/resource/` (Resource Party Roles, Resource
      Specification, Resource, Resource Configuration, Resource Order, Resource Usage,
      Resource Test, Resource Performance, Stock Item, Resource Capacity, Resource
      Trouble, Resource Topology, Resource Strategy & Plan)
    - `wiki/sid/resource-abe.md` (updated — populated category landing)
    - `wiki/sid/resource/_index.md` (updated — populated entities listing)
    - `wiki/index.md` (updated — SID Resource section populated)
    - `wiki/open-questions.md` (updated — OQ-027 through OQ-034 filed)
    - `CLAUDE.md` (updated — added optional `release_status` frontmatter field §6)
- **Sections skipped (out of scope):**
    - GB922 Resource §1, §2, §3 (admin metadata), §5 (Administrative Appendix)
    - All chapter §4 content beyond ABE-overview level (per ABE-level granularity).
      Several large ABEs (Resource Specification at 110pp, Resource at 100pp, Stock
      Item at 148pp, Computing/Software addendum) flagged for follow-up depth.
- **Lint result:** see next entry
- **Open questions filed:**
    - OQ-027 (Pre-production source — Release Status / Team Approved status flag)
    - OQ-028 («doNotImplement» example sub-ABEs preserved)
    - OQ-029 (Computing and Software Addendum depth deferred — likely high relevance
      for OSS-monolith mapping)
    - OQ-030 (Stock Item ABE relevance to OSS mapping uncertain)
    - OQ-031 (Resource Trouble «notFullyDeveloped» — pairs with OQ-024 Service Problem
      gap, both production-side fault management)
    - OQ-032 (Source typo "resoluiton" preserved verbatim)
    - OQ-033 (Resource Topology «notFullyDeveloped»)
    - OQ-034 (Resource Strategy & Plan «notFullyDeveloped» + scope question)
- **Notes:**
    - **Schema addition:** CLAUDE.md §6 now includes optional `release_status`
      frontmatter field (`production` | `pre-production` | `draft`). Default
      `production` if omitted. All Resource ABE pages set `release_status:
      pre-production`. Linter does not enforce values for v1 (optional field).
    - Source extracted to `raw/extracted/tmf/sid/GB922_Resource_v25.5.md`. 429 pages
      → 12,913 lines. Extraction clean.
    - Pre-production / Team Approved status confirmed in PDF metadata. Ingested
      with explicit user authorisation (recorded in pre-flight 2026-05-08).
    - **Production-side data layer now in corpus.** Resource entities (Logical,
      Physical, Compound) are the production-side counterparts to RFS in
      [[wiki/sid/service/service-abe]]. The CFS/RFS distinction in Service domain
      pairs RFS with these Resource entities — completing the production/commercial
      separation pattern at the SID layer.
    - Three Resource ABEs marked «notFullyDeveloped»: Trouble, Topology, Strategy
      & Plan. The Trouble gap, paired with Service Problem ABE («NotFullyDeveloped»),
      is a meaningful incompleteness for production-side fault mapping work — flagged
      jointly via OQ-024 + OQ-031.
    - **SID layer ingest complete.** All four GB922 ABE categories now populated:
      Product (12 ABEs), Service (12 ABEs), Common (19 ABEs), Resource (13 ABEs).
      Total 56 SID ABE pages plus 4 category landings.
    - Next ingest: GB921 (eTOM) — Excel master + 3 decomposition PDFs. Excel needs
      a different extraction approach than `pdftotext` — `pandas` + `openpyxl` to
      be settled when Excel ingestion starts.

---

## 2026-05-08T16:30Z — INGEST (GB921 Excel master, Service Domain L2s — sub-ingest 1 of 3)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
- **Pages created/updated:**
    - 8 new eTOM L2 pages in `wiki/etom/service-domain/`:
      Service Support Management (1.4.4), Service Activation Management (1.4.5),
      Service Problem Management (1.4.6), Service Performance Management (1.4.7),
      Service Guiding & Mediation (1.4.8), Service Catalog Operational Readiness
      Management (1.4.14), Service Catalog Content Management (1.4.15), Service
      Anomaly Management (1.4.18)
    - `wiki/etom/_index.md` (updated)
    - `wiki/etom/service-domain/_index.md` (updated)
    - `wiki/index.md` (updated — eTOM Service Domain section populated)
    - `wiki/open-questions.md` (updated — OQ-035, OQ-036 filed)
- **Sections skipped (out of scope):**
    - Service Domain Strategy-to-Readiness L2s: Service Strategy Management (1.4.1),
      Service Capability Delivery (1.4.2), Service Specification Lifecycle Management
      (1.4.3), Service Capacity Management (1.4.12), Service Catalog Lifecycle
      Management (1.4.13), Service Catalog Planning Management (1.4.16), Service
      Anomaly Lifecycle Management (1.4.17), Service Specification Management (1.4.19)
    - Other domains' L2s (Market, Sales, Customer, Business Partner, Enterprise) —
      out of corpus scope per CLAUDE.md §3
    - Resource and Product Domain L2s — separate sub-ingest events to follow
- **Lint result:** see next entry
- **Open questions filed:**
    - OQ-035 (Decomposition PDF narrative prose deferred to follow-up ingest)
    - OQ-036 (HANDOFF.md L2 scope cross-walk to v25.5 names — names have evolved;
      cross-walk recorded for reader awareness)
- **Notes:**
    - **Tooling installed:** `pandas` 3.0.2 and `openpyxl` 3.1.5 via pip install
      (with `--break-system-packages` override for Homebrew Python's PEP 668 default).
    - Source extracted to `raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md`
      (1.7MB markdown table, all 3168 rows from sheet `eTOM25,5`). Plus a focused
      digest at `raw/extracted/tmf/etom/_in_scope_l2_digest.md` listing the 29
      filtered in-scope L2s (12 Product + 9 Resource + 8 Service).
    - GB921 Excel master GA confirmed: v25.5, sheet header columns: Process,
      Process identifier, Level, Extended Description, Brief description, Domain,
      Vertical Group, Original Process Identifier, UID, Issue.
    - **eTOM L2 pages use the Excel as authoritative source** for verbatim IDs,
      names, and Extended Descriptions. Each page lists L3 children verbatim
      (filtered by parent ID prefix; deduplicated where source has multiple vertical
      classifications for same L3).
    - Trilateral sections currently file OQ-008 (the existing shared placeholder).
      A bidirectional linking sweep across eTOM↔SID will happen after all eTOM
      domains ingest, to ensure SID entity pages get reciprocal back-links.
    - **HANDOFF.md scope cross-walk recorded as OQ-036.** Names like "Service
      Configuration & Activation" no longer exist verbatim in v25.5; the spirit of
      the original scope is preserved (operational OFAB L2s in S/R/P domains).
    - Two sub-ingest events remain: Resource Domain L2s (9), Product Domain L2s
      (12). Then GB921 decomposition PDFs (Service v24.0, Resource v24.0, Product
      v24.0) for narrative prose layering — separate ingest events.

---

## 2026-05-08T16:45Z — INGEST (GB921 Excel master, Resource Domain L2s — sub-ingest 2 of 3)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
  (already extracted in previous sub-ingest)
- **Pages created/updated:**
    - 9 new eTOM L2 pages in `wiki/etom/resource-domain/`:
      Resource Support Management (1.5.4), Resource Order Management (1.5.5),
      Resource Data Management (1.5.7), Resource Trouble Management (1.5.8),
      Resource Performance Management (1.5.9), Resource Mediation & Reporting
      (1.5.10), Resource Catalog Operational Readiness Management (1.5.16),
      Resource Catalog Content Management (1.5.17), Resource Anomaly Management
      (1.5.21)
    - `wiki/etom/_index.md` (updated)
    - `wiki/etom/resource-domain/_index.md` (updated)
    - `wiki/index.md` (updated — eTOM Resource Domain section populated)
- **Sections skipped (out of scope):**
    - Resource Domain Strategy-to-Readiness L2s: 1.5.1, 1.5.2, 1.5.3, 1.5.14,
      1.5.15, 1.5.18, 1.5.19, 1.5.20
- **Lint result:** see next entry
- **Open questions filed:** none new (existing OQ-008, OQ-035, OQ-036 apply)
- **Notes:**
    - Same generation pattern as Service sub-ingest (Python script via openpyxl,
      filtered by Domain × Vertical). Each page has verbatim L2 ID, name, Extended
      Description, and complete L3 listing.
    - Production-side process layer now in corpus. Resource Domain L2s pair with
      Resource SID entities ([[wiki/sid/resource-abe]]) and ResourceFacingService
      ([[wiki/sid/service/service-abe]]).
    - One sub-ingest remains: Product Domain L2s (12).

---

## 2026-05-08T17:00Z — INGEST (GB921 Excel master, Product Domain L2s — sub-ingest 3 of 3)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
- **Pages created/updated:**
    - 12 new eTOM L2 pages in `wiki/etom/product-domain/` (Product Support
      Management, Product Configuration Management, Product Performance Management,
      Product Inventory Management, Product Usage Management, Product Rating & Rate
      Assignment, Product Balance Management, Product Catalog Operational Readiness
      Management, Product Catalog Content Management, Product Anomaly Management,
      Product Problem Management, Product Order Management)
    - `wiki/etom/_index.md` (updated)
    - `wiki/etom/product-domain/_index.md` (created)
    - `wiki/index.md` (updated — eTOM Product Domain section populated)
- **Sections skipped (out of scope):**
    - Product Domain Strategy-to-Readiness L2s: 1.2.1, 1.2.2, 1.2.7, 1.2.8, 1.2.19,
      1.2.20, 1.2.23, 1.2.24
- **Lint result:** see next entry
- **Open questions filed:** none new (existing OQ-008, OQ-035, OQ-036 apply)
- **Notes:**
    - Same generation pattern as Service and Resource sub-ingests.
    - **eTOM Excel-based ingest now complete for all three in-scope domains.**
      Service (8) + Resource (9) + Product (12) = 29 L2 pages total. The L1
      structure is now traceable in the wiki: 1.2 Product Domain, 1.4 Service
      Domain, 1.5 Resource Domain, with operational L2s populated.
    - Commercial-side process layer now in corpus. Product Domain L2s pair with
      Product ABE entities ([[wiki/sid/product-abe]]) and CustomerFacingService
      ([[wiki/sid/service/service-abe]]). Combined with Service and Resource
      Domains, the corpus now represents the full PSR process layer at L2
      granularity.
    - **Next ingest queue:**
        - eTOM Decomposition PDFs (3 separate ingests for narrative prose layering)
        - eTOM↔SID bidirectional sweep (populate trilateral sections; reciprocal
          links on SID entity pages)
        - GB1022 ODA canonical
        - IG1167 ODA extension

---

## 2026-05-08T17:30Z — INGEST (GB1022 ODA Functional Architecture Guidebook v1.1.0)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
- **Pages created/updated:**
    - 6 new ODA Functional Block pages in `wiki/oda/functional-blocks/`:
      Decoupling & Integration, Engagement Management, Party Management, Core
      Commerce Management, Production, Intelligence Management
    - `wiki/oda/_index.md` (updated — describes ODA Functional Blocks layer)
    - `wiki/oda/functional-blocks/_index.md` (created — block listing with
      Systems of Separation grouping)
    - `wiki/index.md` (updated — ODA section populated)
    - `wiki/open-questions.md` (updated — OQ-037, OQ-038 filed)
- **Sections skipped (out of scope):**
    - GB1022 §1 Introduction, §2 Functional Architecture overview (referenced in
      page narratives but not their own pages)
    - §5 Using the Functional Architecture (procedural)
    - §6 Evolution, §7 Administrative Appendix, §8 Document History, §9
      Acknowledgements
    - Detailed mapping tables in §4.3.2/3, §4.4.2/3, §4.5.2, §4.6.1/2 — preserved
      verbatim in source extract; high-level summary in wiki pages with R20.5
      version mismatch noted in OQ-037
- **Lint result:** see next entry
- **Open questions filed:**
    - OQ-037 (GB1022 mappings reference GB921/GB922 R20.5; corpus uses v25.x —
      version mismatch documented; trilateral sweep will resolve where unambiguous)
    - OQ-038 (Non-business ODA blocks D&I and Engagement Management have structural
      trilateral exemption per source §4.1.1, §4.2.2)
- **Notes:**
    - Source extracted to `raw/extracted/tmf/oda/GB1022_..._v1.1.0.md`. 59 pages
      → 2329 lines. Extraction clean.
    - GB1022 v1.1.0 GA confirmed: "Release Status: Production", "Approval Status:
      TM Forum Approved", v1.1.0 (2021).
    - **Third trilateral leg complete.** All three layers (eTOM, SID, ODA) now
      structurally present in the corpus. The PSR corpus shape is now:
      foundations (1) + process (eTOM L2 ×29) + data (SID ABE ×56) + component
      (ODA ×6) + indices/landings.
    - **PSR mapping ready.** Production/commercial separation explicit in three
      layers:
        - eTOM: Service Domain (production-side) ↔ Product Domain (commercial-side)
        - SID: ResourceFacingService / Resource (production) ↔ Product /
          ProductOffering (commercial); CustomerFacingService bridges
        - ODA: Production block (production) ↔ Core Commerce Management block
          (commercial); Engagement Management (front-end); Party Management +
          Intelligence Management (cross-cutting)
    - **Trilateral sweep remains.** ODA pages reference source mapping tables but
      don't populate full reciprocal wikilinks across eTOM↔SID↔ODA. The bidirectional
      sweep is the next major task — it will resolve OQ-008, OQ-037 where
      unambiguous, and add reciprocal back-links across all three layers.
    - **Next ingest queue (revised):**
        - **IG1167 ODA Exploratory Report** — proposed CRs against canonical GB1022
          (already extracted)
        - eTOM↔SID↔ODA bidirectional trilateral sweep
        - GB921 Decomposition PDFs (Service v24.0, Resource v24.0, Product v24.0)
          — narrative prose layering on existing eTOM L2 pages

---

## 2026-05-08T17:45Z — INGEST (IG1167 ODA Exploratory Report — summary form)

- **File(s):** `raw/tmf/oda/IG1167_ODA_Functional_Architecture_Exploratory_Report_v6.0.0.pdf`
  (already extracted at 2026-05-08T12:40Z)
- **Pages created/updated:**
    - `wiki/oda/_index.md` — IG1167 Proposed Extensions section added
    - `wiki/open-questions.md` — OQ-039 filed
- **Lint result:** see next entry
- **Open questions filed:** OQ-039 (IG1167 ingested as summary in _index.md)
- **Notes:**
    - IG1167 §7 sub-sections share Functional Block names with GB1022 (same blocks).
      Many §7 entries are "TBD" / "Ongoing Study"; concrete proposals reference
      R20.5 versions (same mismatch as OQ-037). Summary in _index.md is the
      pragmatic representation. When proposals formalise, ingest into canonical
      block pages.
    - **Last ingest in the agreed v1 queue.** Sequence: foundations → SID → eTOM
      → ODA canonical → IG1167. All five complete.

---

## 2026-05-08 — v1 corpus complete

- **Total pages:** 117 wiki pages, lint clean, 39 open questions filed.
- **Layers:** 7 foundation + 56 SID + 29 eTOM L2 + 6 ODA + 19 infrastructure.
- **Remaining deferred (post-v1):**
    1. Full eTOM↔SID↔ODA trilateral sweep (16 reciprocals already in place)
    2. GB921 Decomposition PDFs — narrative depth for eTOM L2s
    3. SID BE-level attribute tables (per OQ-009)
    4. User-decision OQs to revisit: OQ-013, OQ-021, OQ-024+OQ-031, OQ-030
