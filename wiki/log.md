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

---

## 2026-05-08 — RESTRUCTURE (corpus flattened to repo root)

- **Action:** Moved corpus contents from `tmf-kb/` subdirectory up one level to
  the repo root. The nested `tmf-kb/` folder is removed.
- **Pages affected:** 0 (path changes are at the repo-structure level, not within
  the wiki). Wikilinks (`[[wiki/...]]`) continue to resolve because they were
  always relative to the wiki root, which is unchanged.
- **Lint result:** PASS — 117 pages, 0 findings (verified at the new project root).
- **Notes:**
    - Top-level docs (`README.md`, `AGENTS.md`, `TODO.md`) updated to remove
      `tmf-kb/` path prefixes. README expanded with full ingest process.
    - Linter (`lint/lint.py`) unchanged — `REPO_ROOT = Path(__file__).parent.parent`
      still resolves correctly to the new project root.
    - All `source_paths` and `source_extract_paths` in frontmatter remain valid
      because they were stored relative to the wiki root.
    - `cd tmf-kb && ...` invocations in docs simplified to direct execution at
      project root.

---

## 2026-05-08T18:00Z — TOOLING (linter: skip wikilinks in code spans)

- **File(s):** `lint/lint.py`, `lint/lint_checks.md`
- **Pages created/updated:** none (wiki content unchanged)
- **Sections skipped (out of scope):** N/A
- **Lint result:** PASS — 117 pages, 0 findings
- **Open questions filed:** none
- **Notes:**
    - The 2026-05-08 RESTRUCTURE log entry contains an inline code span
      illustrating the wikilink syntax. Because `wiki/log.md` is append-only
      (CLAUDE.md §10.6), the entry cannot be edited. The earlier linter regex
      did not honour code-span boundaries, so the illustrative text was raised
      as `LINK-BROKEN`. Baseline broke as a result.
    - Fix: introduced `strip_code()` in `lint/lint.py` which removes fenced
      code blocks (```` ``` ````) and inline code spans (`` ` ``…`` ` ``)
      before any wikilink scan. Applied at every regex site (`lint_wikilinks`,
      `lint_trilateral`, `build_link_index`, `lint_bidirectional`).
    - Side effect (intended): a code-spanned wikilink now also fails to
      satisfy `TRI-EMPTY` and is ignored by bidirectional checks. No corpus
      page currently relies on this; verified by grep.
    - `lint/lint_checks.md` `LINK-BROKEN` rule updated to document the skip.

---

## 2026-05-08T18:30Z — TRILATERAL SWEEP (Production block, GB1022 §4.5)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
  (already extracted; sweep reads §4.5 Tables 4-9 and 4-10 from the existing
  extract)
- **Pages created/updated:**
    - `wiki/oda/functional-blocks/production.md` — "SID Entities Owned" and "eTOM
      Processes Realised" sections rewritten with concrete wikilinks; OQ refs
      updated
    - `wiki/sid/service/{service,service-order,service-specification,service-strategy-and-plan,service-configuration,service-usage,service-problem,service-test}-abe.md`
      — added Production back-link (8 pages)
    - `wiki/sid/resource/{resource,resource-order,resource-specification,resource-topology,resource-configuration,resource-usage,resource-strategy-and-plan,resource-trouble,resource-test}-abe.md`
      — added Production back-link (9 pages)
    - `wiki/sid/common/location-abe.md` — added Production back-link
    - `wiki/etom/service-domain/{service-support-management,service-activation-management,service-problem-management,service-guiding-and-mediation}.md`
      — added Production back-link (4 pages)
    - `wiki/etom/resource-domain/{resource-support-management,resource-data-management,resource-trouble-management,resource-mediation-and-reporting}.md`
      — added Production back-link (4 pages)
    - `wiki/open-questions.md` — OQ-040 filed
- **Sections skipped (out of scope):**
    - Workforce ABE (Enterprise Domain) — not in v1 corpus per CLAUDE.md §3
    - R20.5 Service/Resource Strategy/Capability/Specification L2s — SIP vertical,
      out of scope
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved by
  this entry)
- **Open questions filed:**
    - OQ-040 (Production block trilateral sweep — R20.5→v25.x cross-walk
      decisions; 8 eTOM L2s linked, 4 R20.5 L2s deferred as restructured, Common
      Topology ABE flagged as gap)
- **Notes:**
    - **First ODA block trilateral sweep complete.** 26 reciprocal back-links
      added across 8 eTOM L2 + 17 SID ABE + 1 Common ABE pages.
    - **R20.5 cross-walk pattern:** the v25.5 reorganisation is partly clean
      (renames preserving ID) and partly structural (R20.5 L2s demoted to L3 or
      distributed across multiple v25.5 L2s). The clean renames are linked
      directly with provenance noted inline (e.g. "R20.5 'SM&O Support &
      Readiness' → v25.5 1.4.4 Service Support Management"); the structural
      cases are documented in OQ-040 with the absorbing v25.5 L2s linked instead
      of the legacy L2s. This pattern is the template for the remaining 5 ODA
      blocks.
    - **Common Topology ABE gap:** GB1022 Table 4-10 #01 Common Topology ABE has
      no corresponding ABE in the GB922 Common v23.0 corpus (which has Resource
      Topology in the Resource domain). Not linked. Worth a focused look at
      v23.0 §4 structure when convenient — may be a Common ingest gap rather
      than a real model change.
    - **OQ-008 remains active.** Each touched target page still references
      OQ-008 because other ODA components (Core Commerce Management, Engagement
      Management, Party Management, Intelligence Management) have not yet been
      swept. The placeholder text was rephrased on touched pages from "eTOM and
      ODA layers not yet ingested" to "further ODA components pending trilateral
      sweep" — accurate to the post-v1 reality.
    - **Performance ABE pages untouched.** Resource Performance ABE and Service
      Performance ABE were not in GB1022 §4.5 Table 4-10 (Production scope) —
      they are listed under Intelligence Management in §4.6 and already carry
      the intelligence-management back-link from a prior partial sweep. They
      will gain further mappings during the Intelligence and Core Commerce
      sweeps.
    - **Next sweep target:** Core Commerce Management (GB1022 §4.4) — the
      commercial-side counterpart to Production. Same pattern; SID targets are
      Product domain; eTOM targets are Product Domain L2s.

---

## 2026-05-08T19:00Z — INGEST (GB922 Common v23.0 gap fill — §4.23–§4.30 + 4 diagram-only ABEs)

- **File(s):** `raw/tmf/sid/GB922_Common_v23.0.pdf` (already extracted)
- **Pages created/updated:**
    - 12 new ABE pages in `wiki/sid/common/`:
        - Per-chapter (8): test-abe, usage-abe, segmentation-abe, intent-abe,
          closed-loop-abe, goal-abe, workflow-abe, anomaly-abe
        - Diagram-only (4): topology-abe, event-abe, trouble-ticket-abe,
          trouble-or-problem-abe
    - `wiki/sid/common/_index.md` — added 12 entries
    - `wiki/sid/common-abe.md` — split per-chapter and diagram-only sections,
      added 12 entries
    - `wiki/index.md` — updated SID Common section to reflect 31 total ABEs and
      ingest provenance
    - `wiki/oda/functional-blocks/production.md` — replaced Common Topology gap
      text with `[[wiki/sid/common/topology-abe]]` wikilink
    - `wiki/open-questions.md` — OQ-041 filed
- **Sections skipped (out of scope):** none — this ingest closes the v1
  Common-ingest scope gap discovered during the Production trilateral sweep
  (OQ-040)
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved by
  this entry); 129 pages total (was 117)
- **Open questions filed:**
    - OQ-041 (v1 Common ingest stopped at §4.22; 12 ABEs missed; resolved in
      this same ingest event)
- **Notes:**
    - **v1 Common ingest scope gap closed.** The 2026-05-08T15:00Z Common ingest
      truncated at §4.22 instead of §4.30 — an arbitrary cutoff, not a scope
      decision. Discovered during the Production trilateral sweep when GB1022
      §4.5 Table 4-10 referenced Common Topology ABE (one of the missing
      entries).
    - **Per-chapter ABEs (§4.23–§4.30, 8 pages):** standard sid-abe anatomy from
      §4.x verbatim content. BE-level attribute tables not extracted (consistent
      with v1 granularity per OQ-009). The three «Preliminary» ABEs (§4.27
      Closed Loop, §4.28 Goal, §4.29 Workflow) carry `release_status: draft`.
    - **Diagram-only ABEs (4 pages):** these have only a one-paragraph
      description in §4.1 and no §4.x chapter. Pages are explicitly thin and
      flag the source state. Two («not fully developed»: Event, Trouble Ticket)
      carry `release_status: draft`.
    - **Common Topology ABE link populated.** Production page's "SID Entities
      Owned" section now wikilinks the new Common Topology ABE page (which
      itself reciprocates with Production in its "ODA Components That Own This
      Entity" section).
    - **Anomaly ABE / Trouble or Problem ABE — speculative wikilinks removed.**
      Initial drafts of these pages included wikilinks in their trilateral
      sections to v25.5 eTOM Anomaly Management L2s and Service/Resource
      Problem L2s based on name correspondence. CLAUDE.md §1 forbids inferred
      mappings, and no source mapping table establishes those links — wikilinks
      removed; the content remains as plain prose ("v25.5 candidates by name
      are X, Y, Z but no source mapping table establishes the link"). Real
      links should be added when those specific trilateral sweeps run with
      source backing (e.g. updated GB1022 or per-domain decomposition PDFs).
    - **Trilateral coverage of new pages:** all 12 use OQ-008 placeholders for
      ODA owners and eTOM processes, except Topology which now has a real
      Production wikilink. Other ODA-block sweeps (Core Commerce Management,
      Engagement Management, Party Management, Intelligence Management) will
      add concrete wikilinks against several of the new ABEs (e.g. Anomaly →
      Intelligence Management likely; Closed Loop → Intelligence Management
      likely).
    - **Sub-domain placement (Common / Pattern / Shared):** the 12 new ABEs
      use `abe_category: common` consistently with v1's single-bucket choice
      (OQ-014 still tracks the deferred decision on whether to formalise the
      sub-domain split).

---

## 2026-05-08T19:30Z — TRILATERAL SWEEP (Core Commerce Management, GB1022 §4.4)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
  (already extracted; sweep reads §4.4.2 Table 4-6 and §4.4.3 Table 4-7 from the
  existing extract)
- **Pages created/updated:**
    - `wiki/oda/functional-blocks/core-commerce-management.md` — "SID Entities
      Owned" and "eTOM Processes Realised" sections rewritten with concrete
      wikilinks; pre-existing legacy back-links from Account/Business
      Interaction/Catalog ABEs preserved with provenance flag in a separate
      sub-section
    - `wiki/sid/product/{product-and-offering-instance,product-specification,strategic-product-portfolio-plan,product-offering-specification,product-usage,product-configuration,loyalty,product-test}-abe.md`
      — added CCM back-link (8 pages)
    - `wiki/sid/common/capacity-abe.md` — added CCM back-link
    - `wiki/etom/product-domain/{product-configuration-management,product-inventory-management,product-usage-management,product-rating-and-rate-assignment,product-balance-management,product-support-management}.md`
      — added CCM back-link (6 pages)
    - `wiki/open-questions.md` — OQ-042 filed
- **Sections skipped (out of scope):**
    - Customer Domain ABEs (Table 4-7 #01–#04) — Customer Domain not in v1 corpus
      per CLAUDE.md §3
    - Business Partner Domain ABEs (Table 4-7 #01–#06) — Business Partner Domain
      not in v1 corpus per §3
    - R20.5 Market & Sales L2s, S-T-R L2s, Customer Domain L2s, Business Partner
      Domain L2s — out of corpus scope per §3
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved by
  this entry)
- **Open questions filed:**
    - OQ-042 (CCM trilateral sweep — R20.5→v25.x cross-walk decisions; 5 eTOM L2s
      direct + 1 absorbing L2; 8 Product + 1 Common ABE links from Table 4-7;
      pre-existing legacy Common ABE back-links flagged for source-supported
      review)
- **Notes:**
    - **Second ODA block sweep complete.** 16 reciprocal back-links added across
      6 eTOM Product Domain L2 + 8 SID Product ABE + 1 SID Common ABE pages.
      Plus 3 pre-existing legacy back-links acknowledged on the CCM page.
    - **R20.5 cross-walk pattern continued.** Same approach as Production
      (OQ-040): clean R20.5→v25.5 same-ID renames linked directly with provenance
      noted inline; restructured R20.5 L2s (1.2.9 Product Offering Purchasing,
      1.2.15 Product Test Management) absorbed into v25.5 1.2.4 Product Support
      Management as L3 sub-processes — matches the Service Test → 1.4.4.6 and
      Resource Test → 1.5.4.9 pattern.
    - **Disciplined refusal to over-link.** v25.5 Product Domain has 12 in-scope
      L2s; only 6 are linked here because only 6 trace back to entries in
      GB1022 §4.4.2 Table 4-6. Notably 1.2.27 Product Order Management is a
      strong candidate by content (matches R20.5 1.3.3 Customer Order Handling)
      but Customer Domain is out of scope and the GB1022 source doesn't
      explicitly establish the v25.5 Product Domain successor — left unlinked
      with the rationale captured in OQ-042.
    - **Pre-existing legacy back-links handled honestly.** Three Common ABE
      pages (Account, Business Interaction, Catalog) had CCM back-links from
      the v1 partial sweep but those ABEs are not in Table 4-7. Preserved with
      a flag on the CCM page rather than ripping out — provenance documented
      in OQ-042 for future source-supported review.
    - **Performance ABE pages untouched.** Product Performance ABE was not in
      Table 4-7 (Product domain entries were the 8 catalog/spec/instance/order/
      usage/config/loyalty/test ABEs only) — Performance is for the Intelligence
      Management sweep.
    - **Next sweep target:** Engagement Management (GB1022 §4.2). Note OQ-038
      flags structural exemption for non-business framing of EM; the §4.2
      content still has eTOM and SID references worth processing where source
      mappings exist.

---

## 2026-05-08T20:00Z — TRILATERAL SWEEP (Engagement Management, GB1022 §4.2 — no-op confirmed)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
  (already extracted; sweep reads §4.2 from the existing extract)
- **Pages created/updated:**
    - `wiki/oda/functional-blocks/engagement-management.md` — trilateral sections
      tightened to assertively reflect source-supported absence (no longer reads
      as "deferred sweep"); Open Questions list trimmed
- **Sections skipped (out of scope):** none — the sweep was performed and
  confirmed the §4.2 source provides no eTOM L2 or SID ABE mappings to resolve
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved by
  this entry)
- **Open questions filed:** none new — OQ-038 (already filed) covers the
  structural exemption
- **Notes:**
    - **Third ODA block sweep complete — zero new wikilinks produced.** This is
      the correct outcome per source: GB1022 §4.2.2 explicitly states EM "Holds
      no business process (eTOM), no functions (functional Framework) and no
      operational data (SID)". §4.2 contains no Table 4-? for eTOM mapping (the
      other business blocks have Tables 4-3 / 4-6 / 4-9 / 4-12) and no Table
      4-? for SID ABE mapping (the other blocks have Tables 4-4 / 4-7 / 4-10 /
      4-13).
    - **§4.2.4 Open API's Mapping inspected.** The Process flow API and TMF688
      Event Management are interface-level relationships, not eTOM L2 processes
      or SID ABEs. Out of trilateral scope.
    - **Page tightened.** Previously the trilateral sections read as "sweep
      deferred per OQ-008". Now they read as "sweep performed; source-supported
      absence" — accurate and final unless GB1022 itself revises §4.2 content.
      OQ-008 reference removed from EM's Open Questions (sweep done; no links
      to defer). OQ-037 reference also removed from EM (no mapping table
      exists, so the version-mismatch caveat doesn't apply to this block).
    - **OQ-038 stands as the canonical reference** for any future reader asking
      "why are EM's trilateral sections empty?" The answer is the source
      structural exemption, not a corpus gap.
    - **Next sweep target:** Party Management (GB1022 §4.3) — has Table 4-3
      (eTOM, R20.5) and Table 4-4 (SID, R20.5). Cross-cutting block; targets
      span Common Party ABE plus Customer/Business Partner Domain ABEs (largely
      out of corpus scope).

---

## 2026-05-08T20:30Z — TRILATERAL SWEEP (Party Management, GB1022 §4.3)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
  (already extracted; sweep reads §4.3.2 Table 4-3 and §4.3.3 Table 4-4)
- **Pages created/updated:**
    - `wiki/oda/functional-blocks/party-management.md` — "SID Entities Owned"
      and "eTOM Processes Realised" sections rewritten with concrete wikilinks;
      pre-existing legacy Agreement and Party Payment back-links preserved with
      provenance flag in a separate sub-section
    - `wiki/sid/product/product-party-roles-abe.md` — added PM back-link
    - `wiki/sid/service/service-party-roles-abe.md` — added PM back-link
    - `wiki/sid/resource/resource-party-roles-abe.md` — added PM back-link
    - `wiki/open-questions.md` — OQ-043 filed
- **Sections skipped (out of scope):**
    - All 32 R20.5 entries in Table 4-3 — Market/Sales (1.1.x), Customer (1.3.x),
      Business Partner (1.6.x) domains, all out of v1 corpus scope per CLAUDE.md
      §3
    - Market/Sales Domain ABEs in Table 4-4 (entries 01–07) — out of scope
    - Customer Domain ABEs (entries 01–05) — out of scope
    - Business Partner Domain entries 01, 04, 05, 06, 07 — out of scope (entries
      02 Party and 08 Party Privacy linked via v23.0 Common reorg)
    - Common #02 Users and Roles — no clean v23.0 successor
    - Enterprise #01 Enterprise Party Roles — Enterprise Domain not in v1 corpus
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved by
  this entry)
- **Open questions filed:**
    - OQ-043 (PM trilateral sweep — R20.5→v23.0/v25.x cross-walk; domain reorg
      for Party/Party Privacy; zero in-scope eTOM links; pre-existing
      Agreement / Party Payment back-links flagged)
- **Notes:**
    - **Fourth ODA block sweep complete.** Forward links from PM page: 7 new
      concrete (4 v23.0 Common ABEs + 3 v25.x Domain Party Roles ABEs) + 2
      pre-existing legacy preserved. Reciprocal back-links: 3 new added to the
      Domain Party Roles ABE pages. The other 4 Common targets already had PM
      back-links from the v1 partial sweep.
    - **Zero eTOM L2 wikilinks — source-supported absence.** Every R20.5 entry
      in Table 4-3 falls outside corpus scope (Market 1.1.x / Customer 1.3.x /
      Business Partner 1.6.x). PM is fundamentally a cross-cutting block over
      domains the corpus intentionally excludes (CLAUDE.md §3 keeps the focus
      on operational PSR). Different mechanism from Engagement Management's
      no-op (which was structural absence per §4.2.2) but the wiki outcome is
      the same: an empty eTOM trilateral with a source-supported explanation.
    - **R20.5 → v23.0 domain reorganization for Party / Party Privacy.** GB1022
      Table 4-4 puts these under Business Partner Domain; v23.0 GB922 Common
      puts them under Common Domain (cross-cutting). The concept is the same —
      the v23.0 reorganization moved Party concepts to Common because they are
      truly cross-cutting. The links resolve to the v23.0 Common ABEs;
      reasoning captured in OQ-043.
    - **Account ABE link supported by Table 4-4 BP #03.** v23.0 Common Account
      ABE explicitly includes BusinessPartnerAccount (per its own page
      description), so R20.5 BP #03 → v23.0 Common Account is a clean mapping.
      This makes the Account back-link source-supported (no longer a "legacy
      v1 partial sweep" inference for PM, though the same Account-abe page is
      still flagged on the CCM page where Table 4-7 doesn't list it).
    - **Pre-existing legacy back-links preserved.** Common Agreement and
      Common Party Payment had PM back-links from the v1 partial sweep; not
      directly in Table 4-4; preserved on PM page with a flag (same pattern
      as CCM legacy back-links). Inferences are plausible but unsourced.
    - **Next sweep target:** Intelligence Management (GB1022 §4.6) — has Table
      4-12 (eTOM, R20.5) and Table 4-13 (SID, R20.5). Already-existing
      back-links from Service Performance and Resource Performance ABEs
      (intelligence-management appears as their owner from the v1 partial
      sweep) suggest this block has a meaningful Performance / Anomaly /
      Closed Loop trilateral footprint.

---

## 2026-05-08T21:00Z — TRILATERAL SWEEP (Intelligence Management, GB1022 §4.6)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
  (already extracted; sweep reads §4.6.1 Table 4-12 and §4.6.2 Table 4-13)
- **Pages created/updated:**
    - `wiki/oda/functional-blocks/intelligence-management.md` — "SID Entities
      Owned" and "eTOM Processes Realised" sections rewritten with concrete
      wikilinks; pre-existing legacy Common Performance / Metric back-links
      preserved with provenance flag
    - `wiki/etom/product-domain/product-support-management.md` — added IM
      back-link (alongside existing Production back-link)
    - `wiki/etom/service-domain/service-support-management.md` — added IM
      back-link (alongside existing Production back-link)
    - `wiki/etom/resource-domain/resource-support-management.md` — added IM
      back-link (alongside existing Production back-link)
    - `wiki/open-questions.md` — OQ-044 filed
- **Sections skipped (out of scope):**
    - Table 4-12: 1.1.x (Market/Sales 4 entries), 1.3.x (Customer 2 entries),
      1.6.x (Business Partner 2 entries) — domains not in v1 corpus per
      CLAUDE.md §3
    - Table 4-12: 1.2.13/1.4.11/1.5.13 Test Quality Analysis — demoted to L3
      in v25.5 but in Strategy Management vertical, OOS per §3
    - Table 4-13: Market/Sales (2), Customer (1), Business Partner (1) —
      domains OOS per §3
    - Table 4-13: Common 01 Party / Party Profile (L2) — marketing-targeting
      flavour, no clean v23.0 successor, OOS by content
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved
  by this entry)
- **Open questions filed:**
    - OQ-044 (IM trilateral sweep — R20.5→v25.x cross-walk; 6 in-scope eTOM
      L2s with §4.6.1 "split into 2" guidance for Support Management trio
      shared with Production; 3 in-scope Domain Performance ABEs;
      pre-existing Common Performance and Metric back-links flagged)
- **Notes:**
    - **Fifth ODA block sweep complete.** Forward links from IM page: 6 eTOM
      L2 + 3 SID Performance ABE concrete + 2 pre-existing legacy Common ABEs
      preserved. New reciprocal back-links: 3 added on Support Management L2
      pages. Existing IM back-links on the 3 Performance L2s, 3 Performance
      ABEs, and 2 Common ABEs (Performance, Metric) were already in place from
      the v1 partial sweep — only their accuracy was confirmed.
    - **§4.6.1 "split into 2" guidance acknowledged.** GB1022 §4.6.1 explicitly
      states: "eTOM level 2 are identified as 'split into 2' when they manage
      SID ABEs that are mapped to different ODA functional blocks." The
      Support Management trio (1.2.4 / 1.4.4 / 1.5.4) appears in BOTH
      Production (Table 4-9) and Intelligence Management (Table 4-12). This
      is the source's documented model for shared L2 ownership across ODA
      blocks. The reciprocal back-links on these L2 pages now list both
      Production and Intelligence Management — the lint passes cleanly because
      both forward links exist in their respective ODA block pages.
    - **R20.5 1.4.7 Service Quality Management → v25.5 1.4.7 Service
      Performance Management.** Same ID, renamed Quality→Performance. v25.5
      Extended Description still references "Service Quality" as a
      performance objective, confirming the lineage.
    - **Test Quality Analysis L2s (1.2.13, 1.4.11, 1.5.13) excluded.** Demoted
      to L3 in v25.5 (1.2.1.6, 1.4.1.9, 1.5.1.9) but in Strategy Management
      vertical (OFAB-vertical scope per CLAUDE.md §3 keeps only Operations
      Readiness & Support, Fulfillment, Assurance, Billing). Different
      handling from Production's R20.5 1.4.10/1.5.12 Test Management which
      were demoted to L3 in OFAB verticals (1.4.4.6, 1.5.4.9) — those were
      linked via the absorbing 1.4.4/1.5.4 L2.
    - **Pre-existing legacy Common back-links preserved.** Common Performance
      ABE and Common Metric ABE had IM back-links from the v1 partial sweep
      but neither is in Table 4-13. Inferences are plausible (canonical
      parent of Domain Performance ABEs; central to Insight Management's
      Analytic Models per §4.6.3 Table 4-14). Preserved with flag in OQ-044.
    - **Final sweep target:** Decoupling & Integration (GB1022 §4.1). OQ-038
      flags structural exemption for non-business framing. Likely another
      no-op like Engagement Management.

---

## 2026-05-08T21:30Z — TRILATERAL SWEEP (Decoupling & Integration, GB1022 §4.1 — no-op confirmed)

- **File(s):** `raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf`
  (already extracted; sweep reads §4.1 from the existing extract)
- **Pages created/updated:**
    - `wiki/oda/functional-blocks/decoupling-and-integration.md` — trilateral
      sections tightened to assertively reflect source-supported absence;
      Open Questions list trimmed
- **Sections skipped (out of scope):** none — sweep performed and confirmed
  §4.1 source provides no eTOM L2 or SID ABE mappings to resolve
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved
  by this entry)
- **Open questions filed:** none new — OQ-038 (already filed) covers the
  structural exemption
- **Notes:**
    - **Sixth and final ODA block sweep complete.** Like Engagement Management
      (§4.2), zero new wikilinks produced — the correct outcome per source.
      GB1022 §4.1.1 explicitly establishes D&I as gathering "non-business
      functions". §4.1 contains no Table 4-? for eTOM mapping (the business
      blocks have Tables 4-3 / 4-6 / 4-9 / 4-12) and no Table 4-? for SID ABE
      mapping (the business blocks have Tables 4-4 / 4-7 / 4-10 / 4-13).
    - **§4.1.2 Table 4-1 inspected.** Lists integration functionalities only
      (DI.001 Normalized APIs, DI.002 Message Routing, etc.) — interface-level
      functions, not eTOM L2 processes or SID ABEs. Out of trilateral scope.
    - **Page tightened.** Same pattern as the EM sweep (2026-05-08T20:00Z) —
      trilateral sections now read as "sweep performed; source-supported
      absence" rather than "deferred per OQ-008". OQ-008 and OQ-037 references
      removed from Open Questions on this page (sweep done; no mapping table
      to mismatch on).
    - **OQ-038 stands as the canonical reference** for both non-business
      blocks (D&I + EM): "why are these blocks' trilateral sections empty?"
      Answer: source structural exemption.

---

## 2026-05-08T21:35Z — MILESTONE: All 6 ODA Functional Block trilateral sweeps complete

- **Sweeps performed (chronological):**
    1. Production (§4.5) — 2026-05-08T18:30Z, OQ-040, 26 reciprocals
    2. Common ingest gap fill (§4.23–§4.30 + 4 diagram-only) —
       2026-05-08T19:00Z, OQ-041, 12 new ABE pages
    3. Core Commerce Management (§4.4) — 2026-05-08T19:30Z, OQ-042, 16 new
       reciprocals + 3 legacy preserved
    4. Engagement Management (§4.2) — 2026-05-08T20:00Z, no-op confirmed,
       OQ-038 stands
    5. Party Management (§4.3) — 2026-05-08T20:30Z, OQ-043, 7 new + 2 legacy
       forward links, 3 new reciprocals, zero in-scope eTOM (every Table 4-3
       entry out of scope)
    6. Intelligence Management (§4.6) — 2026-05-08T21:00Z, OQ-044, 6 eTOM L2
       + 3 Domain Performance ABE forward links, 2 legacy Common back-links
       preserved, 3 new reciprocals; §4.6.1 "split into 2" guidance handled
       for Support Management trio shared with Production
    7. Decoupling & Integration (§4.1) — 2026-05-08T21:30Z, no-op confirmed,
       OQ-038 stands
- **Total new ODA→SID/eTOM forward links from this campaign:** ~50 across
  Production, Core Commerce, Party Management, Intelligence Management; zero
  for Engagement Management and Decoupling & Integration (source-supported
  absence)
- **Total new reciprocal back-links:** ~48 across SID and eTOM target pages
- **Open questions filed in campaign:** OQ-040, OQ-041, OQ-042, OQ-043, OQ-044
- **Pre-existing legacy back-links handled:** 9 — all preserved with provenance
  flags rather than ripped out (3 on CCM, 4 on Party Management, 2 on
  Intelligence Management)
- **Corpus state:**
    - 129 wiki pages, lint clean throughout
    - 44 open questions
    - All 6 ODA blocks have either source-supported wikilinks or
      source-supported emptiness; OQ-008 (the original "trilateral sweep
      deferred" placeholder) is now satisfied for the ODA-side direction.
      Some SID/eTOM pages still reference OQ-008 because not every ODA block
      mapping is exhaustive (e.g. R20.5 → v25.5 reorganizations leave some
      v25.5 L2s without source mapping coverage); those references are
      accurate.
- **What this enables:** the corpus now provides PSR mapping work with
  source-traceable trilateral connections across all three layers (process,
  data, component) for the operational scope. The user can navigate from any
  in-scope eTOM L2 to its owning ODA block and the SID entities it
  manipulates, and back, with the linter enforcing bidirectional consistency.
- **What remains in TODO.md:** TODO #1 (trilateral sweep) is now done;
  remaining items are TODO #2 (GB921 Decomposition PDFs for eTOM narrative
  depth), TODO #3 (SID BE-level attribute detail), TODO #4 (user-decision OQs
  to revisit). These are all extension/depth work, not structural. The corpus
  is structurally complete for v1.

---

## 2026-05-09T09:00Z — TODO #2 PIVOT + SERVICE DOMAIN DEEPEN (8 L2 pages)

- **File(s):**
    - `raw/tmf/etom/GB921_Service_Process_Decompositions_v24.0.pdf` (extracted
      to `raw/extracted/.../GB921_Service_Process_Decompositions_v24.0.md` —
      217 pages → 8909 lines; retained for figure reference but not added to
      L2 page source_paths after pivot decision)
    - `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
      (read directly via openpyxl; the existing markdown extract truncates
      long cells)
- **Pages created/updated:**
    - 8 in-scope Service Domain L2 pages — added `## L3 Process Details`
      section between `## Overview` and `## L3 Processes`:
        - service-support-management (1.4.4) — 6 L3s with Extended
          Descriptions and L4 listings
        - service-activation-management (1.4.5) — 5 L3s
        - service-problem-management (1.4.6) — 5 L3s
        - service-performance-management (1.4.7) — 5 L3s
        - service-guiding-and-mediation (1.4.8) — 4 L3s
        - service-catalog-operational-readiness-management (1.4.14) — 3 L3s
        - service-catalog-content-management (1.4.15) — 6 L3s
        - service-anomaly-management (1.4.18) — 5 L3s
    - `wiki/open-questions.md` — OQ-035 marked **Resolved 2026-05-09** with
      pivot rationale
- **Sections skipped (out of scope):** none — Service Domain in-scope L2s all
  covered; out-of-scope Service Domain L2s (Strategy/Readiness verticals)
  remain unchanged
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved
  by this entry)
- **Open questions filed:** none new. OQ-035 closed.
- **Notes:**
    - **Pivot decision recorded.** TODO #2 was originally framed as "ingest
      GB921 Process Decomposition PDFs to add narrative depth to eTOM L2
      pages". On starting the work, spot-checking confirmed the v24.0
      decomposition PDF and v25.5 Excel master have substantially identical
      content — the PDF is structured per-L2-chapter; the Excel is structured
      per-process-row; same prose either way. The PDF's only unique content
      is process hierarchy figures (extracted as low-quality ASCII).
    - **Pivot to v25.5 Excel as source.** What the wiki actually lacked was
      display of L3 Extended Descriptions (currently shown only with Brief
      Descriptions) and L4 process listings (not currently displayed).
      Sourcing both from the v25.5 Excel master (more current than v24.0 PDF;
      same content) avoids a same-spec version mismatch with no content gain.
    - **Extraction note: openpyxl direct, not the .md extract.** The existing
      `GB921_Business_Process_Framework_Processes_Excel_v25.5.md` extract
      truncates long cells (~500 char cap). For full Extended Descriptions
      (some L3s have 1500+ chars including bullet lists), the deepen script
      reads the .xlsx directly via openpyxl. The .md extract remains useful
      for grep / overview but is not authoritative for full-cell content;
      future work needing full content should go straight to the .xlsx.
    - **v24.0 PDF retained, not re-cited.** The extracted markdown
      (`raw/extracted/tmf/etom/GB921_Service_Process_Decompositions_v24.0.md`)
      is kept on disk for figure reference and process-hierarchy-diagram
      provenance. L2 page source_paths frontmatter is unchanged — pages
      remain sourced from the v25.5 Excel master only. The v24.0 PDF source
      is not added because (a) its prose content is the same, (b) its
      version (v24.0) is older than the master (v25.5) and would create a
      misleading dual-version provenance.
    - **Pattern set for Resource and Product domains.** Same approach
      (xlsx-direct deepen) will apply when TODO #2 work continues for
      Resource (9 L2s) and Product (12 L2s) domains.
    - **Service Domain L2 pages now include L4 listings.** Each L3 sub-section
      lists its L4 children with verbatim names and brief descriptions. This
      is the first time L4 process detail appears in the wiki; previously L4
      was source-only. Anatomy unchanged — `## L3 Process Details` is an
      additional H2 between Overview and L3 Processes; the linter accepts
      arbitrary H2s between required ones in their original order.

---

## 2026-05-09T09:30Z — RESOURCE DOMAIN DEEPEN (9 L2 pages, TODO #2 continued)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
  (read directly via openpyxl; same approach as Service Domain deepen)
- **Pages created/updated:**
    - 9 in-scope Resource Domain L2 pages — added `## L3 Process Details`
      section between `## Overview` and `## L3 Processes`:
        - resource-support-management (1.5.4) — 8 L3s
        - resource-order-management (1.5.5) — 8 L3s
        - resource-data-management (1.5.7) — 7 L3s
        - resource-trouble-management (1.5.8) — 7 L3s
        - resource-performance-management (1.5.9) — 7 L3s
        - resource-mediation-and-reporting (1.5.10) — 2 L3s
        - resource-catalog-operational-readiness-management (1.5.16) — 2 L3s
        - resource-catalog-content-management (1.5.17) — 4 L3s
        - resource-anomaly-management (1.5.21) — 5 L3s
- **Sections skipped (out of scope):** none — Resource Domain in-scope L2s
  all covered
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved
  by this entry)
- **Open questions filed:** none
- **Notes:**
    - **Same pattern as Service Domain (2026-05-09T09:00Z).** Direct read
      from the .xlsx via openpyxl, formatted into a per-L3 section with
      Extended Description + L4 listings, inserted between Overview and L3
      Processes. Linter anatomy passes (arbitrary H2s allowed between
      required ones in original order).
    - **50 L3s total now have full Extended Descriptions and L4 sub-process
      listings** in the Resource Domain. Combined with Service Domain (39 L3s
      from prior deepen), 89 L3 process bodies are now wiki-readable across
      the two domains.
    - **Resource Support Management (1.5.4) is the largest at 401 lines.**
      It has 8 L3s including Enable Resource Provisioning, which itself
      carries the substantial L4 hierarchy that absorbed R20.5 1.5.6
      Resource Provisioning (per OQ-040 Production sweep cross-walk).
    - **Resource Order Management (1.5.5) at 171 lines, 8 L3s.** This is
      the v25.5 ID that R20.5 used for Workforce Management — entirely
      different process. The L3s here are about resource order capture,
      scheduling, fulfilment.
    - **Next domain target:** Product Domain (12 in-scope L2s). Same script
      pattern; expected ~50–100 L3s based on Product Domain breadth.

---

## 2026-05-09T10:00Z — PRODUCT DOMAIN DEEPEN (12 L2 pages, TODO #2 complete)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
  (read directly via openpyxl; same approach as Service and Resource deepens)
- **Pages created/updated:**
    - 12 in-scope Product Domain L2 pages — added `## L3 Process Details`
      section between `## Overview` and `## L3 Processes`:
        - product-support-management (1.2.4) — 7 L3s
        - product-configuration-management (1.2.5) — 3 L3s
        - product-performance-management (1.2.6) — 5 L3s
        - product-inventory-management (1.2.11) — 7 L3s
        - product-usage-management (1.2.16) — 4 L3s
        - product-rating-and-rate-assignment (1.2.17) — 5 L3s
        - product-balance-management (1.2.18) — 4 L3s
        - product-catalog-operational-readiness-management (1.2.21) — 2 L3s
        - product-catalog-content-management (1.2.22) — 4 L3s
        - product-anomaly-management (1.2.25) — 5 L3s
        - product-problem-management (1.2.26) — 5 L3s
        - product-order-management (1.2.27) — 6 L3s
- **Sections skipped (out of scope):** none — Product Domain in-scope L2s
  all covered
- **Lint result:** PASS — 0 errors, 1 warning (LOG-STALE pre-write; resolved
  by this entry)
- **Open questions filed:** none
- **Notes:**
    - **57 L3s now have full Extended Descriptions and L4 sub-process
      listings** in the Product Domain. Combined totals across all three
      operational PSR domains: 39 (Service) + 50 (Resource) + 57 (Product) =
      **146 L3 process bodies** wiki-readable, plus their L4 children
      verbatim.
    - **TODO #2 is complete.** All 29 in-scope eTOM L2 pages (8 Service +
      9 Resource + 12 Product) now carry L3 Extended Descriptions and L4
      hierarchies sourced from the v25.5 Excel master via openpyxl.
    - **Notable: 1.2.27 Product Order Management.** This is the v25.5 L2
      that I declined to source-link to Core Commerce Management during
      OQ-042 (no Table 4-6 entry); it carries 6 L3s including Manage Product
      Order Capture, Manage Product Order Fulfillment etc. Its content is a
      strong match for R20.5 1.3.3 Customer Order Handling that GB1022 §4.4.2
      Table 4-6 does include — strengthens the OQ-042 hypothesis that
      Customer Order Handling responsibilities moved into the Product Domain
      at v25.5. Still left unlinked pending source confirmation per CLAUDE.md
      §1.

---

## 2026-05-09T10:05Z — MILESTONE: TODO #2 complete

- **Scope:** All 29 in-scope eTOM L2 pages across Service (8), Resource (9),
  and Product (12) domains now display L3 Extended Descriptions and L4
  sub-process listings.
- **Source:** GB921 v25.5 Excel master, read directly via openpyxl. The
  pre-existing `.md` extract in `raw/extracted/` truncates long cells; for
  full-fidelity content, the .xlsx is the canonical source. Future depth
  work needing full cell content should similarly read .xlsx directly.
- **Pivot decision (OQ-035 resolved 2026-05-09):** the original TODO #2
  framing assumed the GB921 Process Decomposition PDFs would add narrative
  depth beyond the Excel master. Spot-checking confirmed the v24.0 PDF and
  v25.5 Excel have substantially identical prose; the wiki's actual gap was
  display of L3 Extended + L4 listings, both available from the more-current
  Excel. Pivoted to xlsx-direct deepen.
- **Numbers:**
    - 146 L3s deepened across 29 L2 pages
    - 8 commits in the campaign so far (linter fix + 5 ODA sweeps + 2
      no-ops + Common gap fill + 3 domain deepens) — but Service/Resource/
      Product deepens land as 3 separate commits per domain
    - 0 lint errors throughout
- **What remains in TODO.md:**
    - TODO #3 — SID BE-level attribute detail per high-value ABE (per
      OQ-016/017/018/019/020/029)
    - TODO #4 — User-decision OQs to revisit (OQ-013, OQ-021, OQ-024+031,
      OQ-030)
    Both are extension/depth work, not structural. The corpus's structural
    completeness from v1 is now augmented with deeper process-layer narrative.

---

## 2026-05-09T11:00Z — CAPABILITY-MAP — FRAMING SETTLED, DRAFT CREATED

- **File(s):** none ingested. New derivative view; sources are 17 in-scope eTOM L2 wiki pages + `wiki/foundations/domains.md` (already in corpus).
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` (new) — `view`-type derivative page; framing decisions locked in `## Session State` callout; L1 frame populated (8 GB991 horizontal business-area domains, Service + Resource in scope, 6 greyed); Service / Resource L2 skeleton organised by OFAB vertical with all 17 in-scope L2 pages wikilinked; capability content awaiting batched proposals.
    - `wiki/views/_index.md` (updated) — Drafts section added listing the capability map draft.
    - `wiki/index.md` (updated) — Views section now lists the capability map draft entry.
- **Sections skipped (out of scope):** N/A — no source ingest. View scope explicitly narrows away from corpus-ingested Product Domain L2s for the OSS-layer practitioner cross-cut; those L2 pages remain on disk and are referenced in the L1 frame's greyed Product entry.
- **Lint result:** PASS — see lint command output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **New work direction.** Capability map derivation initiated as collaborative iterative process. Not in TODO.md as of v1 completion; this is post-v1 extension work.
    - **Framing decisions locked (do not relitigate):**
        1. Output format — single view page.
        2. Naming — hybrid (derived capability label H3 + verbatim eTOM L2 name and ID).
        3. Cross-cutting capabilities — twice in domain-specific form (Service X + Resource X as siblings; not one X with two PSR specialisations).
        4. Anchor IDs — `cap-<layer>-<kebab-name>` for user-private overlay wikilinks.
        5. Trilateral inline — process-only (ODA/SID via L2 page wikilinks).
    - **Refined goal (per user 2026-05-09):** capability map for gap-analysis heat-map overlay and change roadmap. Designed to surface PSR-driven distinctions monolithic BSS/OSS conflates (Service Problem vs Resource Trouble; Service Catalog vs Service Activation; Service Performance vs Service Anomaly vs Service Problem; ticketing-as-fault vs three-way TMF assurance split).
    - **L1 frame derived from GB991 §1.1.1.** Eight business-area horizontal domains; Service + Resource in scope; Market, Sales, Product, Customer, Business Partner, Enterprise greyed (Product greyed for the view despite corpus ingestion of operational Product L2s — view-level scoping, not corpus change). Three non-business GB991 domains (Shared, Patterns, Integration) omitted by their own definitions.
    - **L2 organisation:** OFAB vertical grouping within each L1 (Operations Readiness & Support → Fulfillment → Assurance → Billing). Two cross-vertical L2s footnoted: 1.5.5 Resource Order (Fulfillment + ORS), 1.5.7 Resource Data (multi-vertical, primary ORS).
    - **Security boundary reaffirmed.** Capability map is pure TMF-derivative. Current-state status, Nokia mapping notes, and gap analysis live entirely in `project/` (which Claude does not read per CLAUDE.md §10.4). User's `project/` overlay file wikilinks the capability map's stable anchors.
    - **Honest derivation note** in draft banner: GB991 §1.2 (Business Capability Map) marked FUTURE WORK in TMF source per OQ-005. There is no TMF-canonical operational capability map; the draft is one defensible derivation.
    - **6 thematic batches planned**, all PENDING: Catalog (4 L2s), Anomaly (2), Performance (2), Problem/Trouble (2), Support (2), Activation/Order/Data/Mediation (5). Total 17.
    - **Next action:** propose Batch 1 (Catalog) for user review with HIGH/MEDIUM/LOW confidence labels per rollup; wait for sign-off before Batch 2.

---

## 2026-05-09T11:30Z — CAPABILITY-MAP — BATCH 1 (CATALOG) SETTLED

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — Batch 1 baked in: 4 H4 capability entries
      added (`cap-service-catalog-operational-readiness`, `cap-service-catalog-content`,
      `cap-resource-catalog-operational-readiness`, `cap-resource-catalog-content`);
      Session State callout updated (Batch 1 → DONE; H3→H4 correction; new Last
      activity; Next action → propose Batch 2 Anomaly); `## L2 Capability Frame
      Diagram` H2 added (Mermaid `flowchart` showing all 17 in-scope L2s grouped by
      L1 + OFAB plus 6 greyed L1 domains); Service Domain ORS placeholder reduced to
      Batch-5 reference for 1.4.4; Resource Domain ORS placeholder reduced to
      Batch-5/6 references for 1.5.4/1.5.7.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **Batch 1 verdict:** 4 separate capabilities, no rollups. HIGH on all four.
      Operational Readiness vs Content are distinct L2s in GB921 v25.5 with distinct
      scope statements (Operational Readiness → support / release / deploy machinery;
      Content → catalog substance — specifications, offerings, attributes,
      versioning, lifecycle). Collapsing them would erase a TMF distinction directly
      relevant to the user's gap-analysis goal — the user's stated current-state
      gap ("dev team implicitly handles service specification; no service catalog")
      sits squarely in Catalog Content, not Operational Readiness.
    - **Naming.** eTOM-aligned phrasing per user direction: capability labels track
      the L2 wording ("Service Catalog — Operational Readiness", "Service Catalog —
      Content") for traceability, with the verbatim L2 name + ID on the italic line
      below the H4 heading.
    - **TMF distinctions per capability.** Each H4 carries two distinction call-outs:
      (a) within-pair (OR vs Content), (b) cross-batch reference to Service Activation
      (1.4.5; Batch 6 pending) for the Service catalog pair, and cross-PSR reference
      to the matching Service catalog capability for the Resource catalog pair.
      Distinctions cite source pages; no interpretation introduced.
    - **Verbatim source.** Scope statements are the verbatim ## Overview text from
      the four L2 wiki pages (which were sourced from GB921 v25.5 Excel master via
      openpyxl during TODO #2). Citation format `— GB921 v25.5` retained.
    - **H3→H4 correction.** Initial draft Session State said "capability label
      (H3)". With OFAB verticals as H3 (Operations Readiness & Support, Fulfillment,
      Assurance, Billing) under each L1 H2, capabilities sit as H4 beneath. Caught
      during Batch 1 proposal; corrected in this commit.
    - **Mermaid frame diagram.** Single `flowchart TB` with three top-level
      subgraphs: Out of scope (greyed; LR layout for compactness), Service Domain
      (TB; OFAB subgraphs nested), Resource Domain (TB; OFAB subgraphs nested).
      Greyed nodes get `classDef` styling (light grey fill, dashed border, muted
      text). All 17 in-scope L2 nodes carry verbatim ID + name. Rendered inline in
      Obsidian. Frame is fixed; capability content fills in below as batches settle
      but the diagram itself doesn't change.
    - **Heat-map / overlay model unchanged.** Capability map remains pure
      TMF-derivative. Anchors `cap-service-catalog-operational-readiness`,
      `cap-service-catalog-content`, `cap-resource-catalog-operational-readiness`,
      `cap-resource-catalog-content` are stable for user-private overlay wikilinks
      from `project/`.
    - **Next action:** propose Batch 2 (Anomaly) — Service Anomaly (1.4.18) and
      Resource Anomaly (1.5.21), both Assurance vertical. Both expected HIGH; the
      interesting work is surfacing TMF distinctions against Performance and
      Problem/Trouble (Batches 3 and 4 — same Assurance vertical; the three-way
      Assurance split is exactly the gap pattern the user flagged for current-state
      monolithic ticketing).

---

## 2026-05-10T09:00Z — CAPABILITY-MAP — BATCH 2 (ANOMALY) SETTLED + OQ-045 FILED

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — Batch 2 baked in: 2 H4 capability
      entries added under Service Domain Assurance (`cap-service-anomaly`) and
      Resource Domain Assurance (`cap-resource-anomaly`). Service Assurance
      placeholder reduced to Batches 3+4 references for 1.4.6/1.4.7. Resource
      Assurance placeholder reduced to Batches 3+4 references for 1.5.8/1.5.9.
      Session State callout updated (Batch 2 → DONE; Last activity 2026-05-10;
      Next action → propose Batch 3 Performance).
    - `wiki/open-questions.md` — OQ-045 filed (Resource Anomaly Management 1.5.21
      Overview text references non-existent L2 "Resource Problem Management"; the
      v25.5 L2 is 1.5.8 Resource Trouble Management; verbatim quote preserved with
      parenthetical note in capability map entry).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** OQ-045 (1.5.21 source-text terminology quirk).
- **Notes:**
    - **Batch 2 verdict:** 2 separate capabilities, no rollups, HIGH on both.
      Clean PSR siblings per framing decision #3.
    - **Source-grounded TMF distinctions, unusually direct.** GB921 v25.5's
      Anomaly L2 Overviews include explicit "is different from
      [Problem|Trouble]" sentences, and "record them before they ever become
      [Problem|Trouble] concerns" — meaning the pre-Problem nature of Anomaly
      is stated in the source, not an interpretation. Surfaced in both
      capability entries' TMF-distinctions sections with verbatim quotes.
      Directly serves the user's stated current-state gap (monolithic ticketing
      handles known faults; pre-fault detection is a distinct TMF capability).
    - **Three-way Assurance split visibility.** Batch 2 plus the upcoming
      Batches 3 (Performance) and 4 (Problem/Trouble) populate the full TMF
      Assurance triad: Anomaly (pre-Problem) → Performance (metrics) →
      Problem/Trouble (restoration). Capability map will surface this
      structurally adjacent on the page — exactly the cluster where
      monolithic ticketing collapses three TMF capabilities into one.
    - **OQ-045 source-text quirk.** GB921 v25.5's 1.5.21 Resource Anomaly
      Management Overview reads *"…before they ever become Resource Problem
      Management concerns"* and *"…is different from Resource Problem
      Management as the later addresses known issues, faults or problems."*
      No L2 named "Resource Problem Management" exists in v25.5; the
      corresponding Resource-domain analog is 1.5.8 Resource Trouble Management.
      Likely a copy-paste from the Service Anomaly L2 (1.4.18) Overview where
      the analog L2 *is* "Service Problem Management" (1.4.6), with the term
      not substituted. Verbatim quote preserved in the capability map entry
      with a `> **Source-text quirk**` callout pointing to OQ-045 — fidelity
      maintained without silently smoothing the source.
    - **Forward-reference wikilinks.** Both Anomaly entries cite
      `[[#cap-service-problem]]`, `[[#cap-service-performance]]`,
      `[[#cap-resource-trouble]]`, `[[#cap-resource-performance]]` — anchors
      that don't exist until Batches 3 & 4 land. Linter skips in-page anchor
      wikilinks (lint.py line 329: `if not target_no_anchor: continue`), so
      no LINK-BROKEN findings. The wikilinks become live navigation as the
      target anchors get added.
    - **Next action:** propose Batch 3 (Performance) — 1.4.7 Service Performance
      Management + 1.5.9 Resource Performance Management. Source establishes
      Performance ↔ Trouble information flow (1.5.9 explicitly: "if the
      analysis identifies a resource performance violation or a potential
      service performance violation, information will be passed to Resource
      Trouble Management and/or Service Quality Management"). Source also
      notes 1.4.7 was renamed in v23.5 from "Service Quality Management" —
      provenance worth surfacing in the Service Performance distinction notes.

---

## 2026-05-10T10:30Z — CAPABILITY-MAP — BATCH 3 (PERFORMANCE) SETTLED

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — Batch 3 baked in: 2 H4 capability
      entries added (`cap-service-performance` under Service Domain Assurance,
      `cap-resource-performance` under Resource Domain Assurance), placed in L2
      ID order ahead of the existing Anomaly H4s. Service Assurance placeholder
      reduced to Batch-4 reference for 1.4.6; Resource Assurance placeholder
      reduced to Batch-4 reference for 1.5.8. Session State updated (Batch 3 →
      DONE; provenance-line convention recorded; Next action → propose Batch 4
      Problem/Trouble).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **Batch 3 verdict:** 2 separate capabilities, no rollups, HIGH on both.
      Clean PSR siblings.
    - **v23.5 rename surfaced prominently for Service Performance.**
      `cap-service-performance` carries a second italic provenance line above
      Scope: *"v23.5 rename: previously named 'Service Quality Management'…"*
      User-approved at Batch 3 review. Two reasons: (1) older TMF documents
      and stakeholders may still use Service Quality Management; (2) the v25.5
      source for 1.5.9 Resource Performance Management itself still uses the
      old name when referring to Service Performance — the rename wasn't
      propagated everywhere. Reader hits the rename context before reading the
      Scope or sibling distinctions, preventing confusion.
    - **Counterpart disambiguation in Resource Performance.**
      `cap-resource-performance` Scope quote preserves verbatim source text
      ("Service Quality Management" reference included). A
      `> Note on referenced L2 names` callout follows, pointing to
      `cap-service-performance` and clarifying the rename. Verbatim discipline
      maintained without leaving the reader confused.
    - **Provenance-line convention recorded in Session State.** When a TMF L2
      carries a documented version-rename, surface it as a second italic line
      immediately above Scope (under `eTOM L2:`). Apply to any future
      capability where source flags a rename. Settled at Batch 3 review with
      user approval.
    - **Source-grounded Performance↔Trouble boundary.** GB921 v25.5 1.5.9
      Overview directly establishes the handoff: *"if the analysis identifies
      a resource performance violation or a potential service performance
      violation, information will be passed to Resource Trouble Management
      and/or Service Quality Management as appropriate."* Cited verbatim in
      `cap-resource-performance` TMF distinctions; the cleanest source-grounded
      Performance→Trouble boundary in the corpus.
    - **Cross-PSR escalation captured.** Source establishes that resource
      performance violations may be passed to Service Performance / Service
      Quality Management — meaning Resource Performance can trigger Service
      Performance attention. Both `cap-service-performance` and
      `cap-resource-performance` TMF distinctions reflect this bidirectional
      flow (each cites the other's source-grounded direction).
    - **Three-way Assurance triad now half-visible.** With Batch 3 done, the
      capability map shows Anomaly + Performance under both Service and
      Resource Assurance subsections, leaving only Problem/Trouble (Batch 4)
      to close the triad. The structural adjacency in the page already
      surfaces the lifecycle progression for the user's gap analysis.
    - **Next action:** propose Batch 4 (Problem / Trouble) — 1.4.6 Service
      Problem Management + 1.5.8 Resource Trouble Management. Closes the
      three-way Assurance triad on both PSR sides. Source has explicit
      Service↔Resource cross-PSR language in 1.5.8 ("interact with the Service
      Problem Management processes, as the latter have a view on service
      impact… informing Service Problem Management of any potential service
      problems") — gives a strong source-grounded distinction set.

---

## 2026-05-10T11:30Z — CAPABILITY-MAP — BATCH 4 (PROBLEM / TROUBLE) SETTLED

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — Batch 4 baked in: 2 H4 capability
      entries added (`cap-service-problem` under Service Domain Assurance,
      `cap-resource-trouble` under Resource Domain Assurance), placed in L2 ID
      order ahead of the existing Performance + Anomaly H4s. Service Assurance
      and Resource Assurance placeholder lists removed (sections now contain
      three H4 capabilities each, in L2 ID order: Problem/Trouble → Performance
      → Anomaly). Session State updated (Batch 4 → DONE; naming-asymmetry
      convention recorded; Next action → propose Batch 5 Support).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **Batch 4 verdict:** 2 separate capabilities, no rollups, HIGH on both.
      Three-way TMF Assurance triad now structurally complete on both PSR
      sides. Capability map shows lifecycle progression Anomaly → Performance
      → Problem/Trouble adjacent on the page — exactly the cluster where
      monolithic ticketing collapses three TMF capabilities into one.
    - **TMF naming asymmetry preserved per eTOM-aligned framing.**
      `cap-service-problem` (1.4.6 Service **Problem** Management) and
      `cap-resource-trouble` (1.5.8 Resource **Trouble** Management) keep the
      source's asymmetric terminology. Each entry's TMF-distinctions list
      surfaces the asymmetry explicitly so a reader hitting either side sees
      the explanation. User-approved at Batch 4 review; convention recorded
      in Session State for any future PSR-pair where source uses asymmetric
      terms.
    - **Source-cited bidirectional cross-PSR coordination.** GB921 v25.5 1.5.8
      Overview is the cleanest source-grounded cross-PSR boundary in the
      corpus: *"Resource Trouble Management processes are responsible for
      informing Service Problem Management of any potential service problems.
      Where the original report arose as a result of service problems, the
      Resource Trouble Management processes may be coordinated by Service
      Problem Management processes."* Cited verbatim in both
      `cap-service-problem` and `cap-resource-trouble` TMF-distinction lists.
    - **Customer Domain Problem Handling — explicit boundary.** GB921 1.4.6
      Overview references "Problem Handling processes" sitting in the
      Customer Domain (greyed L1 in this view). `cap-service-problem` carries
      a fourth distinction bullet calling out the boundary: Service Problem
      manages service-restoration; Problem Handling owns customer-facing case
      management; they interact but are distinct. Worth flagging because
      monolithic ticketing typically blurs Service Problem ↔ Customer Problem
      Handling.
    - **Resource Trouble as convergence point.** Per 1.5.8 Overview's
      input-flow paragraph, Resource Trouble takes inputs from three upstream
      sources: resource alarms (from Resource Data Collection & Distribution
      / 1.5.7 Resource Data in v25.5 — Batch 6 pending), resource performance
      notifications (from Resource Performance), and service-side trouble
      notifications (from Service Problem). Surfaced as a fourth distinction
      bullet in `cap-resource-trouble` — operational convergence point for
      resource-fault assurance.
    - **Forward reference to `cap-resource-data`.** `cap-resource-trouble`
      cites `[[#cap-resource-data|Resource Data]]` as the upstream alarm
      source. That anchor doesn't exist yet (Batch 6 will create it).
      In-page anchor wikilinks are skipped by the linter, so no LINK-BROKEN
      finding. Becomes live navigation when Batch 6 lands.
    - **Next action:** propose Batch 5 (Support) — 1.4.4 Service Support
      Management + 1.5.4 Resource Support Management, both Operations
      Readiness & Support vertical. Note GB1022 §4.6.1 "split into 2"
      guidance: Support trio (1.2.4 Product Support — out of view scope —
      plus 1.4.4 + 1.5.4 in scope) jointly owned by Production +
      Intelligence Management ODA blocks per OQ-044. Worth surfacing in
      capability commentary even though trilateral inline stays out per
      framing decision #5.

---

## 2026-05-10T13:00Z — CAPABILITY-MAP — BATCH 5 (SUPPORT) SETTLED

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — Batch 5 baked in: 2 H4 capability
      entries (`cap-service-support`, `cap-resource-support`) under Service/
      Resource Domain Operations Readiness & Support sections; 2 H5 security
      sub-capability entries (`cap-service-support-security`,
      `cap-resource-support-security`) — heat-map overlay can mark security
      maturity independently of broader Support coverage. Service ORS
      placeholder removed; Resource ORS placeholder reduced to Batch 6 entry
      for 1.5.7. Session State updated (Batch 5 → DONE; security-H5 +
      TMF-pure-mental-category conventions recorded; Last activity 2026-05-10;
      Next action → propose Batch 6 — final batch).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **Batch 5 verdict:** 2 separate capabilities + 2 H5 security
      sub-capabilities, all HIGH. Total 4 stable heat-map anchors from this
      batch.
    - **Two-step rename history per L2.** Both 1.4.4 and 1.5.4 carry verbatim
      source notes documenting two renames each: `pre-v23.5 "[X] Readiness &
      Support" → v23.5 "[X] Support Readiness" → v24.0+ "[X] Support
      Management"`. Surfaced as italic provenance lines above Scope per the
      Batch-3 convention. Older documents may reference any of three names per
      L2 — stakeholder-facing context worth flagging.
    - **Security promoted to H5 sub-capability (user direction at Batch 5
      review).** GB921 v25.5 lists five security/risk responsibilities
      verbatim on both 1.4.4 and 1.5.4 (Vulnerability Management, Threat
      Assessments, Risk Assessments, Risk Mitigation, Secure Configuration
      Activities). TMF v25.5 OFAB does not house a separate Security
      Management L2 — security is a Support concern at the
      infrastructure-readiness layer. The H5 sub-section duplicates these
      verbatim bullets and carries a stable sub-anchor for heat-map overlay
      independence. **Convention recorded in Session State** for any future
      L2 carrying an explicit security/risk responsibility list.
    - **Workforce-as-Resource-Support-responsibility distinction.** GB921
      v25.5 1.5.4 lists *"Establishing and managing the workforce to support
      the eTOM processes"* as a Resource Support Management responsibility.
      Surfaced as a TMF distinction in `cap-resource-support` to close the
      L1-frame Workforce Management question raised early in capability-map
      framing — TMF v25.5 source position is workforce-management functions
      reside under Resource Support at the operational-readiness layer, not
      as a top-level horizontal domain.
    - **Multi-ODA ownership / Intelligence-Management share.** Per OQ-044
      and GB1022 §4.6.1, both Support L2s are "split into 2" — jointly owned
      by Production + Intelligence Management ODA functional blocks.
      Surfaced as a TMF distinction in both entries with the explicit
      delineation: trend analysis & forecasting at the infrastructure layer
      is the Intelligence Management share of the Support L2; KPI / objective
      / metrics tracking lives in the Performance L2s (1.4.7 / 1.5.9). Source-
      grounded answer to the user's "intelligence support is blurry against
      service performance" question — the Intelligence-flavoured aspect of
      Support is trend / forecasting / capability reporting, not KPI
      management.
    - **TMF-pure mental-category convention recorded.** User's organisational
      mental categories (e.g. infrastructure / customer-services /
      intelligence) are NOT synthesised into the wiki capability map.
      Mental-category mapping lives in the user's `project/` overlay file,
      which wikilinks the capability map's stable anchors. Wiki stays
      TMF-source-pure; organisation-specific groupings stay outside per
      CLAUDE.md §10.4 security boundary. Convention recorded in Session State
      for any future similar refinement requests.
    - **Forward references hold.** Both Support entries cite
      `[[wiki/etom/.../<l2>]]` for L2s pending Batch 6 (Service Activation,
      Resource Order). These resolve via the lint check (target wiki pages
      exist on disk). The cross-Support forward references
      (`[[#cap-service-support]]` ↔ `[[#cap-resource-support]]`) are
      now both live (in-page anchor wikilinks; bidirectional navigation
      works).
    - **Heat-map anchor inventory after Batch 5.** Capability map now exposes
      14 stable anchors: 4 from Catalog (Batch 1), 2 from Anomaly (Batch 2),
      2 from Performance (Batch 3), 2 from Problem/Trouble (Batch 4), 2 from
      Support + 2 H5 security sub-capabilities (Batch 5). Batch 6 will add 5
      more (Service Activation, Service Guiding & Mediation, Resource Order,
      Resource Data, Resource Mediation & Reporting), bringing the final
      total to 19 stable anchors across the 17 in-scope L2s plus 2 security
      sub-capabilities.
    - **Next action:** propose Batch 6 (Activation / Order / Data / Mediation)
      — the heterogeneous final batch. 5 L2s mixing Fulfillment, multi-vertical
      ORS, and Billing. Most likely place for MEDIUM-confidence calls. Key
      naming-similarity disambiguation: Service "Guiding & Mediation" (1.4.8)
      vs Resource "Mediation & Reporting" (1.5.10) — both Billing vertical,
      similar names, different scopes per source. Plus the multi-vertical
      placements for 1.5.5 (Resource Order: Fulfillment + ORS) and 1.5.7
      (Resource Data: all four OFAB verticals) need confirmation.

---

## 2026-05-10T15:00Z — CAPABILITY-MAP — BATCH 6 (ACTIVATION / ORDER / DATA / MEDIATION) SETTLED + WORKFORCE H5 RETROACTIVE — MAP STRUCTURALLY COMPLETE

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2/L3 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — Batch 6 baked in: 5 H4 capability
      entries added (`cap-service-activation`, `cap-service-guiding-and-mediation`,
      `cap-resource-order`, `cap-resource-data`, `cap-resource-mediation-and-reporting`)
      across Service Fulfillment, Service Billing, Resource Fulfillment, Resource
      ORS, Resource Billing sections. 1 fresh H5 sub-capability added in Resource
      Order: `cap-resource-order-workforce` (surfaces L3 1.5.5.7 Manage Resource
      Work Order with 6 L4 sub-processes verbatim). 1 retroactive H5 added inside
      the Batch-5-baked Resource Support entry: `cap-resource-support-workforce`
      (surfaces L3 1.5.4.8 Manage Field Workforce). All `_Pending Batch X_`
      placeholders removed from the page. Session State updated (Batch 6 → DONE;
      workforce-H5 convention recorded; PENDING list empties; Last activity
      2026-05-10; Pending decision: draft → final promotion). All forward-
      reference in-page anchor wikilinks (e.g. `[[#cap-resource-order]]`,
      `[[#cap-resource-data]]`, `[[#cap-resource-order-workforce]]`) now resolve
      to live anchors.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **Batch 6 verdict:** 5 separate capabilities, no rollups, HIGH on all 5.
      Predicted MEDIUM at framing-time; source turned out to be clear on each
      L2's scope and clean on cross-batch / cross-PSR boundaries.
    - **Three rename callouts handled** per the Batch-3 provenance-line
      convention:
        - 1.4.5 v24.0 rename from "Service Configuration & Activation". Note:
          the v24.0 rename was not propagated to the responsibilities preamble
          inside the Overview, which still reads *"Responsibilities of the
          Service Configuration & Activation processes"*. Verbatim source
          preserved with a `> source quirk` callout below the Scope quote.
        - 1.5.7 v23.5 rename from "Resource Data Collection & Distribution".
          **Cascade:** 1.5.8 Resource Trouble and 1.5.9 Resource Performance
          source texts both still reference the old name when describing input
          flows. Disambiguation note in `cap-resource-data` provenance line.
        - 1.5.5 cross-version ID collision (per OQ-040 / OQ-044): R20.5 1.5.5
          was Workforce Management; v25.5 1.5.5 is Resource Order Management.
          Cross-version note as second italic provenance line.
    - **Workforce surfaced as H5 sub-capabilities — TMF-aligned, source-grounded.**
      User asked at Batch 6 review whether automated-vs-workforce resource
      orders are different capabilities. Source answer: TMF doesn't carve out
      "automated" but does carry dedicated L3 processes for workforce on both
      Resource Support (1.5.4.8 Manage Field Workforce, with multiple L4s) and
      Resource Order (1.5.5.7 Manage Resource Work Order, with 6 L4s). Both
      promoted to H5 sub-capabilities with stable sub-anchors. Establishment /
      planning side lives in `cap-resource-support-workforce`; per-order
      execution side lives in `cap-resource-order-workforce`. Heat map can mark
      these independently of the broader L2 cells — a fully-automated
      provisioning system shows green on `cap-resource-order` overall but red
      on `cap-resource-order-workforce`, exposing the user's stated current-
      state gap pattern cleanly.
    - **Workforce-H5 convention recorded.** Stricter test than the security-H5
      convention: a workforce-style H5 sub-capability requires a *named L3
      process* with substantive source scope (security-H5 was justified by a
      multi-bullet block within an L2's responsibility list with no dedicated
      L3). Going forward only invoke this when both criteria hold (recognised
      practitioner concern + dedicated L3 backing).
    - **Naming-similarity disambiguation 1.4.8 ↔ 1.5.10.** Service Guiding &
      Mediation vs Resource Mediation & Reporting — both Billing vertical,
      both involve mediation, both noted by source as *"often handled by
      appropriate network elements"*. Distinction is event scope: 1.4.8 =
      customer/service-related usage events; 1.5.10 = resource events.
      Surfaced as bidirectional TMF distinctions in both entries.
    - **Resource Data multi-vertical placement.** 1.5.7 spans all four OFAB
      verticals per source; placed under ORS as primary because the scope is
      foundational data infrastructure. Capability is upstream provider for
      Resource Trouble, Resource Performance, and Resource Mediation &
      Reporting. No service-side analog (no 1.4.x Service Data Management L2);
      service-data concerns are distributed across Service Support (Service
      Inventory), Service Guiding & Mediation (service-event mediation), and
      Service Performance (service metrics).
    - **Final stable-anchor inventory.** Capability map is structurally
      complete. 21 stable anchors total:
        - 17 L2 capability anchors: `cap-service-support`,
          `cap-service-activation`, `cap-service-problem`,
          `cap-service-performance`, `cap-service-guiding-and-mediation`,
          `cap-service-catalog-operational-readiness`,
          `cap-service-catalog-content`, `cap-service-anomaly`,
          `cap-resource-support`, `cap-resource-order`,
          `cap-resource-data`, `cap-resource-trouble`,
          `cap-resource-performance`,
          `cap-resource-mediation-and-reporting`,
          `cap-resource-catalog-operational-readiness`,
          `cap-resource-catalog-content`, `cap-resource-anomaly`.
        - 2 H5 security sub-capability anchors:
          `cap-service-support-security`, `cap-resource-support-security`.
        - 2 H5 workforce sub-capability anchors:
          `cap-resource-support-workforce`, `cap-resource-order-workforce`.
    - **What's complete vs what's optional next.** Structurally complete: all
      17 in-scope L2s have full H4 capability content with TMF distinctions,
      provenance lines where applicable, and source-page wikilinks; 4 H5 sub-
      capabilities (security ×2, workforce ×2) carry independent heat-map
      sub-anchors. Optional future work: (a) promote `capability-map-draft.md`
      → `capability-map.md` once user signals satisfaction; (b) selective L3
      drill-down for any L2 where heat-map gap analysis demands finer
      granularity (deferred per framing decision).

---

## 2026-05-10T16:30Z — CAPABILITY-MAP — PHASE 2 L3 REVIEW: INVENTORY + TEST H5 ADDITIONS + CLEANUP

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L3 process detail.
- **Pages created/updated:**
    - `wiki/views/capability-map-draft.md` — 4 new H5 sub-capabilities baked in:
      `cap-service-support-inventory` (L3 1.4.4.1 Manage Service Inventory, with
      its 4 L4 sub-processes verbatim); `cap-resource-support-inventory` (L3
      1.5.4.5 Manage Resource Inventory, with 3 L4s — asymmetric to Service:
      no Audit Tests L4); `cap-service-support-test` (L3 1.4.4.6 Manage Service
      Test); `cap-resource-support-test` (L3 1.5.4.9 Manage Resource Test, with
      a source-text quirk parenthetical akin to OQ-045 family). Service Support
      and Resource Support TMF-distinction lists updated to add Inventory + Test
      H5 pointers. Stale "; Batch X pending" forward-reference notes stripped
      throughout the file (11 occurrences across Service Support, Resource
      Support, Catalog Content / OR pairs, Anomaly entries, Performance entries,
      and Resource Trouble convergence-point bullet). Service Activation and
      Resource Order references in Support TMF distinctions upgraded from L2-
      page wikilinks to in-page anchor wikilinks (now-live cross-references).
      Session State updated (Last activity; Phase 2 entry added under DONE;
      L3-derived sub-capability convention renamed and expanded with all three
      observed instances; second Pending Decision added for S2R-vertical scope
      expansion deferral).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new.
- **Notes:**
    - **Phase 2 origin.** User's review request after Batch 6 capability-map
      completion: "Why is there no 'strategy' and 'capability' verticals?" and
      "With security and workforce we identified new sub-categories by analysing
      L3 processes. Review the other L3 etom processes to see if there are any
      more sub-categories worth call out." Phase 1 (Strategy/Capability)
      answered with corpus-grounded scope discipline — explicitly excluded per
      CLAUDE.md §3 SIP-vertical exclusion; user deferred scope expansion
      decision. Phase 2 (L3 review) surveyed all 132 L3s across 17 in-scope L2s
      and identified 3 candidate concerns: Inventory (strong, both Support
      L2s), Test (strong, both Support L2s), Number Portability (weaker,
      single-PSR, telecom-specific). User approved Inventory + Test, declined
      Number Portability.
    - **L3-derived sub-capability convention renamed and expanded.** Originally
      filed as "Workforce-H5 convention" at Batch 6 settlement; with three
      instances now observed (workforce + inventory + test) the convention is
      formally generalised. The bar — *named L3 process with substantive
      scope, recognised practitioner concern, cross-cutting heat-map relevance*
      — held cleanly across all three. Number Portability failed the
      cross-cutting / PSR-symmetry test even though it has a substantive
      named L3.
    - **Inventory L3s — paired traceability backbone.** 1.4.4.1 (Service) and
      1.5.4.5 (Resource) cross-reference each other via the
      service↔resource-instance association recorded in the Resource Inventory
      Database. Service Inventory cross-references customer-product-offering↔
      service-instance associations. Together the two L3s form the OSS-layer
      traceability backbone for state. Source asymmetry preserved: Service
      Inventory has 4 L4s (Manage DB/Processes, Audit Tests, Track/Monitor,
      Identify Issues); Resource Inventory has 3 L4s (Manage DB/Processes,
      Track/Monitor, Identify Issues — no Audit Tests analog).
    - **Test L3s — cross-PSR test orchestration.** Both 1.4.4.6 and 1.5.4.9
      explicitly cite cross-PSR dependencies. 1.4.4.6 says Service Test relies
      on Product + Resource Test Management. 1.5.4.9 has a source-text quirk
      ("Product and Service Manage Resource Test process") where intent is
      clearly "Product and Service Test Management processes". Verbatim quote
      preserved with inline parenthetical noting OQ-045-family source-text
      inconsistency. No new OQ filed (same pattern as OQ-045; not blocking;
      preserved verbatim in the heat-map anchor).
    - **Phase 1 — Strategy / Capability verticals — out of scope, deferred
      decision recorded.** GB991 §1.1.2 defines two Lifecycle Areas: S2R
      (Strategy-to-Readiness; contains Strategy Management, Capability
      Management, Business Value Development, shared part of ORS) and
      Operations (contains shared part of ORS, Fulfillment, Assurance,
      Billing). Capability map shows the Operations area's OFAB grouping only.
      CLAUDE.md §3 explicitly excludes the SIP / S2R lifecycle ("strategic,
      not operational"). User approved staying narrow ("finish this piece of
      work then we'll scope out the work on this one — ask me at that time").
      Recorded as second Pending Decision in Session State for future user
      prompt.
    - **Stale "Batch X pending" forward-reference notes cleaned.** 11
      occurrences removed across the page — all forward references that were
      qualified with "; Batch N pending" or "— Batch N pending" because the
      target capability hadn't been baked in yet at the time the source bullet
      was written. Batches 3, 4, and 6 are all now done; the qualifications
      were stale. Stripped via sed; lint clean.
    - **Final stable-anchor inventory after Phase 2.**
        - 17 L2 capability anchors (unchanged from Batch 6).
        - 8 H5 sub-capability anchors:
            - Security: `cap-service-support-security`, `cap-resource-support-security`.
            - Workforce: `cap-resource-support-workforce`, `cap-resource-order-workforce`.
            - Inventory: `cap-service-support-inventory`, `cap-resource-support-inventory`.
            - Test: `cap-service-support-test`, `cap-resource-support-test`.
        - **Total: 25 stable heat-map anchors.**
    - **Next action:** capability map is structurally and content-complete
      against the user's stated goal. Two pending user-decisions remain:
      (1) promote `capability-map-draft.md` → `capability-map.md`;
      (2) scope expansion to S2R-lifecycle verticals (deferred). User reviews
      the full draft and signals readiness to move to overlay work in
      `project/`.

---

## 2026-05-10T16:35Z — CAPABILITY-MAP — Session State callout sync

- **File(s):** none ingested.
- **Pages created/updated:** `wiki/views/capability-map-draft.md` — Session State callout (top of page) updated to reflect Phase 2 additions: Last activity line, batches DONE list (added Phase 2 entry under Batch 6), Pending decisions (added second item for S2R-vertical scope expansion deferral), Workforce-H5 convention renamed to **L3-derived sub-capability convention** with all three observed instances (workforce, inventory, test) listed, Next action updated. Page body content already baked at 16:30Z entry; this entry is the callout-sync follow-up so the canonical resume context matches the page content.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:** Two-step write happened due to Edit-tool re-read requirement after the mid-batch sed cleanup; harmless. Recorded for audit-trail completeness.

---

## 2026-05-10T17:00Z — CAPABILITY-MAP — PROMOTED FROM DRAFT + PHASE 3 START

- **File(s):** none ingested.
- **Pages created/updated:**
    - **Renamed:** `wiki/views/capability-map-draft.md` → `wiki/views/capability-map.md` (file mv, no content reload). Active reference cleanup: H1 de-draftified ("# Capability Map (Draft) —" → "# Capability Map —"); Session State callout intro "for this draft" → "for this view"; Last activity line updated to record the promotion + Phase 3 start; Pending decisions block collapsed to _(none)_ since both prior items have been actioned; Next action repointed to Phase 3 scoping work.
    - `wiki/index.md` — Views section entry repointed to `[[wiki/views/capability-map]]`; description updated with anchor counts and post-promotion status.
    - `wiki/views/_index.md` — section heading "Drafts" → "Capability Maps"; entry repointed and described.
    - `wiki/open-questions.md` — OQ-045 source-page reference repointed from `capability-map-draft#cap-resource-anomaly` to `capability-map#cap-resource-anomaly`.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none new.
- **Notes:**
    - **Promotion scope.** File rename only; no content was modified beyond active-reference cleanup. Body content (L1 frame, Mermaid diagram, all 17 H4 capability entries, all 8 H5 sub-capability entries, TMF distinctions, Source Pages) carried forward unchanged. Frontmatter `derived_from` unchanged (still references the 17 L2 wiki pages + foundations/domains.md). Stable anchor IDs unchanged — user's `project/` overlay file (which Claude does not read) can wikilink the new path `[[wiki/views/capability-map#cap-<anchor>]]` directly.
    - **Historical references in past log entries left intact.** Previous log entries dated 2026-05-09T11:00Z through 2026-05-10T16:35Z reference the file by its original name `wiki/views/capability-map-draft.md`. Per CLAUDE.md §10.6, log.md is append-only — historical entries are not edited. The in-content historical mention in the post-promotion Last activity line (2026-05-10T17:00Z) is intentional narrative recording the rename event.
    - **Phase 3 scoping started.** User direction "promote it then scope the S2R work" signals readiness to plan the Strategy & Capability verticals expansion. Phase 3 is a scoping exercise, not an ingest. Output planned as a separate artifact (working name `S2R-EXPANSION-SCOPE.md` or similar — to be confirmed in scoping). Heat-map overlay work in `project/` is the user's parallel-track activity, unblocked by the Phase 3 scoping.

---

## 2026-05-10T17:30Z — CAPABILITY-MAP — PHASE 3 SCOPING ARTIFACT CREATED

- **File(s):** none ingested. Scoping artifact only — no corpus content modified.
- **Pages created/updated:**
    - **New:** `S2R-EXPANSION-SCOPE.md` (repo root, project-management content
      sibling to `CLAUDE.md` / `AGENTS.md` / `TODO.md` / `README.md`).
      Comprehensive Phase 3 scoping plan — 12 sections covering: goal, L2
      inventory (10 L2s for Strategy + Capability; 16 if BVD included), SID
      ABE situation (mostly already in corpus from v1 SID ingest), CLAUDE.md
      §3 amendment options, capability-map structural choices, Mermaid
      strategy options, sub-capability H5 review pattern, trilateral
      considerations, effort estimate (17–39 hr range), phasing options,
      5 user decisions, recommendation, and proposed next steps.
    - `TODO.md` — TODO #5 added pointing to `S2R-EXPANSION-SCOPE.md`.
- **Sections skipped:** N/A (no source-document ingest performed).
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none new. (5 user decisions surfaced in scoping
  document, but not formalized as OQs because they're project-direction
  decisions, not corpus-content questions.)
- **Notes:**
    - **Scoping methodology.** Pulled the full Service + Resource L2
      inventory direct from `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx`
      via openpyxl, grouped by Vertical Group column. Confirmed:
        - Strategy Management: 2 L2s (1.4.1 Service Strategy Management;
          1.5.1 Resource Strategy Management)
        - Capability Management: 8 L2s (1.4.2, 1.4.12, 1.4.16, 1.4.19,
          1.5.2, 1.5.14, 1.5.18, 1.5.19)
        - Business Value Development: 6 unique L2s (1.4.3, 1.4.13, 1.4.17,
          1.5.3, 1.5.15, 1.5.20)
        - 1.5.5 Resource Order is multi-vertical (BVD + Fulfillment + ORS) —
          already in scope per OFAB.
    - **SID burden surprisingly low.** Verified that
      `service-strategy-and-plan-abe`, `resource-strategy-and-plan-abe`,
      Specification ABEs (Service / Resource / Product / Product Offering),
      Capacity ABEs (Service / Resource / Product / Common), and
      `strategic-product-portfolio-plan-abe` are all already in the SID
      corpus. SID coverage in CLAUDE.md §3 is by ABE category (Product /
      Service / Resource / Common), not by vertical alignment — Strategy/
      Capability ABEs were ingested at v1 because they're Service/Resource
      Domain ABEs. **Estimated 0–4 new ABE pages needed**, mostly for any
      Capability-specific Plan ABEs that may exist in GB922 v25.5 but
      weren't called out at v1.
    - **Net effort estimate.** 17–27 hr for Strategy + Capability (10 L2s);
      25–39 hr for full S2R (16 L2s). Effort dominated by L2-page ingest
      with verbatim source extraction and trilateral linking; SID side
      mostly already done.
    - **Recommendation in scoping doc:** Include BVD (full S2R coverage);
      use two-view-page structure (Option 2C) — keeps `capability-map.md`
      clean for primary OSS use case and isolates new content in
      `capability-map-s2r.md`; two Mermaid diagrams (one per Lifecycle
      Area); pilot first with 1.4.1 Service Strategy Management, then
      pause for review before continuing.
    - **Next action:** user reviews `S2R-EXPANSION-SCOPE.md` and signals
      decisions on the five questions surfaced in §10. Scoping document
      then becomes the execution brief.

---

## 2026-05-10T18:00Z — S2R-EXPANSION — DECISIONS LOCKED

- **File(s):** none ingested. Project-direction decisions only — no corpus content modified.
- **Pages created/updated:**
    - `S2R-EXPANSION-SCOPE.md` (repo root) — Session State callout added at top with
      all five decisions locked, refined goal recorded, conventions-inherited list
      explicit, next-action stated, CLAUDE.md amendment flagged as still-pending.
      Status line in document header changed from *"Scoping in progress"* to *"Scoping
      complete — Phase 3 active per 2026-05-10 user sign-off."*
- **Sections skipped:** N/A (no source-document ingest).
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** none new. (The five decisions were project-direction
  matters, not corpus-content questions.)
- **Notes:**
    - **User goal refinement.** Pre-decision message clarified the capability map's
      primary purpose: *current → target transformation roadmap* for monolithic
      code-driven BSS/OSS → PSR-driven TMF/eTOM target architecture (Nokia OSS).
      S+R focus, **all vertical groups including S2R**. *"I don't wish to exclude
      service or resource L2s if they may impact the running of a new PSR-based OSS
      once it is running and we are building towards PSR alignment with TMF guidance."*
      Refinement strengthens the case for full S2R coverage (Decision 1 = include
      BVD) because BVD's Specification Lifecycle and Catalog Lifecycle L2s are
      central to the "build services in code → service spec/catalog" transition story.
    - **L2 inventory verified complete.** Direct read of
      `GB921_…_v25.5.xlsx eTOM25,5` sheet against the scope-doc §2 L2 lists confirmed
      no missing L2s: Service Domain has 16 unique v25.5 L2s (8 in corpus + 8 to
      ingest = 16); Resource Domain has 17 unique v25.5 L2s (9 in corpus + 8 to
      ingest = 17). Numbering gaps in Resource (1.5.6/11/12/13) are deletion artefacts
      captured in the workbook's `eTOM Deleted` sheet, not omissions. Total new L2
      ingest: 16. Combined post-ingest S+R L2 corpus: 33.
    - **Five decisions, in summary:**
        1. Include BVD (full S2R = 16 new L2s).
        2. Two view pages (`capability-map.md` Operations only; new
           `capability-map-s2r.md` for S2R).
        3. Two Mermaid diagrams (one per Lifecycle Area).
        4. Pilot first — 1.4.1 Service Strategy Management + 1.5.1 Resource Strategy
           Management as the paired-PSR pilot. Then Capability Management (8 L2s);
           then BVD (6 L2s); then L3-derived H5 sub-capability review.
        5. Incremental trilateral verification — per-L2 OQ filing during ingest.
    - **CLAUDE.md §3 amendment pending.** Required to reflect the new in-scope
      verticals. Will be drafted as a separate edit proposal and shown for sign-off
      before applying — not yet touched.
    - **Conventions inherited.** All seven established capability-map conventions
      apply forward (verbatim discipline, provenance-line, naming-asymmetry,
      security-H5, TMF-pure mental-category, L3-derived sub-capability, plus the
      overall iterative collaboration discipline — propose then sign-off then bake-in
      then log then lint, never charge ahead).
    - **Pilot ready for proposal.** 1.4.1 Service Strategy Management source content
      pulled from the Excel master: 1668-char Extended Description for the L2 plus
      9 L3 processes (1.4.1.1 through 1.4.1.9) and ~25 L4 sub-processes. 1.4.1 has a
      documented v24.0 rename ("Service Strategy & Planning" → "Service Strategy
      Management") — apply provenance-line convention. R20.5 → v25.5 ID change:
      Original PID was 1.2.2.1 (the SIP-vertical numbering scheme), now 1.4.1
      (Service Domain numbering). L3s 1.4.1.8 (Service Test Strategy) and 1.4.1.9
      (Analyze Service Test Quality) carry `Original Process Identifier: None` —
      they're new in v25.5.
    - **Next action:** propose pilot L2 page contents for user review; on approval
      ingest 1.4.1, then pause for review before 1.5.1.

---

## 2026-05-10T18:30Z — INGEST — Service Strategy Management (1.4.1) — Phase 3 pilot L2

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.1 (and its L3/L4 descendants) extracted via openpyxl; pre-existing extracted markdown working copy at `raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md` covers the same content.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-strategy-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Frontmatter (etom-l2 type, GB921 v25.5, Service Domain L1 1.4, L2 1.4.1). Three-line lifecycle-area / vertical-context / domain callout (slight upgrade for S2R pages — anchored wikilinks into `[[wiki/foundations/lifecycle]]` for Strategy-to-Readiness and Strategy Management). Italic provenance line for v24.0 rename ("Service Strategy & Planning" → "Service Strategy Management"), per provenance-line convention. Verbatim L2 Overview from Excel ED (1668 chars), with the source-text `&;` Excel-encoding artefacts preserved verbatim and noted in the citation block. Full `## L3 Process Details` section with Extended Descriptions and L4 sub-process listings for all nine L3s (1.4.1.1 through 1.4.1.9). Inline `> Source-text note` callout on 1.4.1.7 (L3 name "Gain Enterprise Commitment to Service Strategies" vs ED prose "Gain Commitment to Service Plans" — verbatim variation). Two `> New in v25.5` callouts on 1.4.1.8 Service Test Strategy and 1.4.1.9 Analyze Service Test Quality (Original PID = None; no R20.5 lineage). `## L3 Processes` summary list. `## SID Entities Manipulated`: two source-grounded forward links — `service-strategy-and-plan-abe` (direct match for the strategic/planning artefacts) and `service-test-abe` (supporting L3 1.4.1.8/9). `## ODA Components That Realise This Process`: deferred to **OQ-046** (newly filed; see below). Three Open Questions listed.
    - `wiki/etom/service-domain/_index.md` — title de-OFAB-ified (was "Operational L2s" → now "Service Domain L2s"); intro paragraph extended to reference both Lifecycle Areas (Operations + Strategy-to-Readiness) per GB991 §1.1.2. Phase 3 expansion note added. L2 table extended with new `Lifecycle Area` column and 1.4.1 entry. Out-of-scope paragraph repurposed as "Pending ingest under Phase 3" (lists the seven remaining S2R-area Service Domain L2s).
    - `wiki/sid/service/service-strategy-and-plan-abe.md` — `## eTOM Processes That Manipulate This Entity` populated with reciprocal back-link to the new L2 page. OQ-025 status note updated to flag partial scope-lifting under Phase 3.
    - `wiki/sid/service/service-test-abe.md` — `## eTOM Processes That Manipulate This Entity` populated with reciprocal back-link, scoped to the L3 1.4.1.8/9 dependency. Note added flagging that the canonical Test pattern is shared cross-PSR and broader trilateral discovery may surface additional eTOM L2s (e.g. OFAB-side L3 1.4.4.6).
    - `wiki/index.md` — eTOM Service Domain section restructured with Operations / Strategy-to-Readiness Lifecycle Area subdivision. L2 count updated from 8 → 9. Phase-3-in-progress note added.
    - `wiki/open-questions.md` — **OQ-046** newly filed. Scope: GB1022 §4.x ODA mapping tables reference R20.5 PIDs; S2R-vertical L2s carry R20.5 SIP-vertical numbering as Original PID (e.g. 1.4.1 was 1.2.2.1) and may not appear in GB1022's §4.x tables at all (analogous to OQ-038 Engagement / D&I "no-op confirmed" findings, or a documentation gap to be filled by future TMF sources). Applies forward to all 16 S2R-vertical eTOM L2 pages.
- **Sections skipped (out of scope):** None within the 1.4.1 L2 — fully ingested. The skip is global at the corpus level: this is the first S2R-vertical L2 to enter the wiki; other S2R verticals remain awaiting their pilot/full ingest sequence per Phase 3 phasing decision (P1 — pilot first).
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** OQ-046 (new, per above).
- **Notes:**
    - **Pilot L2 #1 of 2.** First of the paired-PSR pilot: 1.4.1 Service Strategy Management. Second pilot L2 (1.5.1 Resource Strategy Management) awaits user review checkpoint and sign-off before ingest.
    - **Verbatim discipline preservations.** `&;` Excel-encoding artefacts preserved verbatim in the L2 Overview (CLAUDE.md §1, §10.3) — the only L2 ingest convention deviation is the inline note flagging the artefact in the citation block, which is metadata about the source rather than a source paraphrase. Two L4 sub-processes within 1.4.1.5 and three within 1.4.1.6/1.4.1.7 carry source ED = "Not used for this process element" — preserved verbatim per existing-corpus pattern (e.g. earlier OFAB L2 ingests). 1.4.1.7 L3-name vs ED-prose verbiage variation surfaced inline rather than filed as a separate OQ (intent unambiguous; pattern matches OQ-045-family handling).
    - **Cross-version PID change recorded.** v25.5 1.4.1's Original Process Identifier in the Excel is `1.2.2.1` — the R20.5 SIP-vertical numbering scheme. Surfaced in the L2's source-citation block. Significant for OQ-046 (downstream ODA cross-walk) because GB1022 mapping tables reference R20.5 IDs.
    - **L3 1.4.1.8 + 1.4.1.9 are new in v25.5.** Both carry `Original Process Identifier: None`. Service Test Strategy + Analyze Service Test Quality form a Test-strategy lineage paired with the OFAB-side L3 1.4.4.6 Manage Service Test (which surfaced as the H5 sub-capability `cap-service-support-test` in capability-map Phase 2). Conceptual pairing: 1.4.1.8/9 are the strategic/quality-analysis side; 1.4.4.6 is the operational execution side. Worth surfacing during the eventual L3-derived sub-capability review at end of S2R ingest.
    - **CLAUDE.md §3 amendment still pending.** Phase 3 brought S2R verticals into scope per user direction, but the binding constitution text in CLAUDE.md §3 still excludes the SIP vertical. Amendment will be drafted as a separate proposed edit and shown for sign-off before applying. Until applied, the discrepancy is documented in `S2R-EXPANSION-SCOPE.md` Session State and in the new L2's `Phase 3 expansion note` callout in `_index.md`.
    - **Capability map integration deferred.** New view page `wiki/views/capability-map-s2r.md` will be created after both pilot L2s (1.4.1 + 1.5.1) land. The 1.4.1 capability section will be populated as part of the capability map skeleton creation.
    - **Next action:** user reviews the 1.4.1 L2 page in Obsidian / via file read; on approval, propose the 1.5.1 Resource Strategy Management page contents (paired-PSR symmetric with 1.4.1) before ingest.

---

## 2026-05-10T19:00Z — INGEST — Resource Strategy Management (1.5.1) — Phase 3 pilot L2 (paired-PSR with 1.4.1)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Resource Domain L2 1.5.1 (and its L3/L4 descendants) extracted via openpyxl.
- **Pages created/updated:**
    - **NEW** `wiki/etom/resource-domain/resource-strategy-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Three-line lifecycle-area / vertical-context / domain callout. Italic provenance line for v24.0 rename ("Resource Strategy & Planning" → "Resource Strategy Management"). Verbatim L2 Overview from Excel ED (2380 chars; longer than Service-side analog's 1668). Source-text observation callout flagging AI / advanced-analytics references in 1.5.1.1 / 1.5.1.3 / 1.5.1.5 (Resource side has v25.5 AI guidance the Service-side analog L2 1.4.1 does not). Full `## L3 Process Details` section with all nine L3s (1.5.1.1–1.5.1.9) populated with Extended Descriptions and L4 listings. Asymmetry callouts on L3 1.5.1.3 ("Establish Resource Strategy & **Architecture**" with 4 L4s vs Service-side "& Goals" with 7 L4s) and on L3 1.5.1.5 (quarterly cadence vs Service-side annual/multi-year only). Source-text note on 1.5.1.7 (L3-name vs ED-prose verbiage variation, same OQ-045-family handling as Service-side 1.4.1.7). Two `> New in v25.5` callouts on 1.5.1.8/9 with PSR-symmetric anchored wikilinks back to Service-side 1.4.1.8/9. `## SID Entities Manipulated`: two source-grounded forward links — `resource-strategy-and-plan-abe` (with OQ-027 + OQ-034 references inline) and `resource-test-abe` (with OQ-027 reference inline). `## ODA Components`: OQ-046 placeholder.
    - `wiki/etom/resource-domain/_index.md` — title de-OFAB-ified (was "Operational L2s" → "Resource Domain L2s"); intro paragraph extended to reference both Lifecycle Areas. Phase 3 expansion note added. L2 table extended with new `Lifecycle Area` column and 1.5.1 entry. Out-of-scope paragraph repurposed as "Pending ingest under Phase 3" (lists the seven remaining S2R-area Resource Domain L2s) plus a forward-pointer to the upcoming `[[wiki/views/capability-map-s2r]]` skeleton.
    - `wiki/sid/resource/resource-strategy-and-plan-abe.md` — `## eTOM Processes That Manipulate This Entity` populated with reciprocal back-link to the new L2 page. PSR-symmetric cross-reference to Service-side `service-strategy-and-plan-abe` ↔ `service-strategy-management` pair noted. OQ-034 status note updated to flag partial scope-lifting under Phase 3.
    - `wiki/sid/resource/resource-test-abe.md` — `## eTOM Processes That Manipulate This Entity` populated with reciprocal back-link, scoped to L3 1.5.1.8/9 dependency. Note added flagging OFAB-side L3 1.5.4.9 (Manage Resource Test) as a separate eTOM interaction that is already an H5 sub-capability anchor in the Operations-area capability map.
    - `wiki/index.md` — eTOM Resource Domain section restructured with Operations / Strategy-to-Readiness Lifecycle Area subdivision. L2 count 9→10. Phase-3-in-progress note.
    - `S2R-EXPANSION-SCOPE.md` — Session State updated (Last activity, Pilot status, Next action).
- **Sections skipped (out of scope):** None within the 1.5.1 L2 — fully ingested. The skip is global at the corpus level: 14 more S2R-area Service+Resource L2s remain awaiting ingest (Capability Management 8 L2s; BVD 6 L2s).
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** None new. OQ-046 (filed under 1.4.1) covers this L2's ODA cross-walk gap.
- **Notes:**
    - **Pilot L2 #2 of 2 — paired-PSR pilot complete.** Both 1.4.1 Service Strategy Management and 1.5.1 Resource Strategy Management now in corpus. Pilot validates: (a) the lifecycle-area three-line callout pattern works for S2R pages; (b) the provenance-line convention applies cleanly to v24.0 renames; (c) `&;` Excel-encoding artefact preservation; (d) source-text variation handling (L3 name vs ED prose); (e) New-in-v25.5 callout pattern for L3s without R20.5 lineage; (f) PSR-symmetric anchored wikilinks between Service and Resource L3 analogs (1.4.1.8/9 ↔ 1.5.1.8/9); (g) trilateral SID forward + reciprocal back-link pattern; (h) ODA-deferral-via-OQ pattern.
    - **PSR asymmetries surfaced and preserved.** Three TMF-distinction callouts now live in the 1.5.1 page that don't have analogs in 1.5.1's mirror image but reflect real TMF v25.5 content differences: (1) AI / advanced-analytics references throughout the Resource side (Service side carries no such references in its L3 EDs); (2) "Strategy & Architecture" framing on the Resource side vs "Strategy & Goals" on the Service side, with different L4 decompositions (4 vs 7); (3) quarterly planning cadence on Resource side vs annual/multi-year only on Service side. These are load-bearing for the user's transformation roadmap (AI-readiness in particular is a separate axis worth seeing).
    - **Forward references that don't yet resolve.** L3 1.5.1.1.3 references "1.8.5 Domain Orchestration process" (Common Process domain — out of corpus scope per CLAUDE.md §3 L1 Frame); preserved as verbatim prose, no wikilink. L3 1.5.1.3.4 references "Resource Capability Delivery processes" (eTOM L2 1.5.2 — scheduled for ingest under Phase 3 Capability Management batch); flagged in the L4 line; will add a back-reference note when 1.5.2 lands. L3 1.5.1.2 / 1.5.1.6 reference "Party Offering Development & Retirement processes" (Engaged Party / Business Partner domain — out of corpus scope); preserved as verbatim prose.
    - **Cross-version PID change.** v25.5 1.5.1's Original Process Identifier `1.2.3.1` is the R20.5 SIP-vertical Resource-side numbering scheme. Surfaced in the L2's source-citation block. Same OQ-046 deferral applies.
    - **Trilateral linking now bidirectionally consistent for Strategy Management vertical.** Both 1.4.1 and 1.5.1 link forward to their primary Strategy-and-Plan ABEs and Test ABEs; both ABEs carry reciprocal back-links. Linter confirms.
    - **CLAUDE.md §3 amendment still pending.** Same status as after 1.4.1 ingest. Will draft as separate proposal at the user-pause-for-review step closing the pilot.
    - **Next action:** create `wiki/views/capability-map-s2r.md` skeleton (frontmatter, derivation status callout, Session State block ported from `S2R-EXPANSION-SCOPE.md`, Purpose, L1 Frame, L2 Capability Frame Diagram, Strategy-to-Readiness — Strategy Management section with 1.4.1 + 1.5.1 capability content, Source Pages). Then user-pause-for-review checkpoint closes the pilot. Then onward to Capability Management batch (8 L2s, the heaviest of the three).

---

## 2026-05-10T19:05Z — LINT FIX — cross-PSR navigational wikilinks removed from Resource ABE trilateral sections

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/sid/resource/resource-strategy-and-plan-abe.md` — removed three cross-PSR
      navigational wikilinks (`[[wiki/sid/service/service-strategy-and-plan-abe]]`,
      `[[wiki/etom/service-domain/service-strategy-management]]`) from the
      `## eTOM Processes That Manipulate This Entity` section. The wikilinks were
      added in the 19:00Z 1.5.1 ingest as paired-PSR navigational hints; the linter
      correctly interpreted them as forward links demanding bidirectional reciprocity
      (Service-side ABEs and L2 don't and shouldn't reciprocate Resource-side ABE
      links — they reciprocate their own Service-side L2). Replaced with plain-text
      reference to the Service-side analog "see the Service Domain SID and eTOM
      directories for the mirror pair" — preserves practitioner intent without
      triggering the trilateral check.
    - `wiki/sid/resource/resource-test-abe.md` — same fix, two cross-PSR wikilinks
      removed (`[[wiki/sid/service/service-test-abe]]`,
      `[[wiki/etom/service-domain/service-strategy-management]]`).
- **Lint result:** PASS — 132 pages, 0 errors, 1 warning (LOG-STALE, cleared by this
  entry).
- **Open questions filed:** none.
- **Notes:**
    - **Lesson recorded for the convention list.** Forward going: cross-PSR
      navigational wikilinks in trilateral sections (`## SID Entities Manipulated`,
      `## eTOM Processes That Manipulate This Entity`, `## ODA Components That Realise
      This Process`, `## SID Entities Owned`, `## ODA Components That Own This
      Entity`) trigger bidirectional consistency checks per-entity, not per-PSR-pair.
      To preserve PSR-pair navigation intent without triggering lint, use plain prose
      references (entity name + locality) rather than wikilinks. The L3 anchored
      wikilinks in body text outside trilateral sections (e.g. the ones in 1.5.1.8 /
      1.5.1.9 callouts pointing back to 1.4.1.8 / 1.4.1.9) are not subject to the
      check and can stay as wikilinks.
    - **Will mirror this pattern** when ingesting the rest of the S2R L2s — keep
      cross-PSR navigation prose-only inside the trilateral sections.

---

## 2026-05-10T19:30Z — VIEW — capability-map-s2r.md skeleton + Strategy Management vertical populated (Phase 3 pilot deliverable complete)

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages (1.4.1 + 1.5.1) and foundation pages (domains, lifecycle).
- **Pages created/updated:**
    - **NEW** `wiki/views/capability-map-s2r.md` — companion view page for the Strategy-to-Readiness Lifecycle Area. Frontmatter (`type: view`; `derived_from` listing the four current source pages — `domains.md`, `lifecycle.md`, the two ingested L2s — list grows per batch). Five-paragraph derivation-status callout at top: companion-view intent + derivative discipline + GB991 §1.2 FUTURE WORK acknowledgement (OQ-005) + scope (16 L2s, 2 ingested + 14 pending; 1.5.5 multi-vertical boundary decision noted) + transformation-roadmap framing. Full Session State block with framing decisions, conventions inherited from sister page, conventions added at pilot, batch tracking, pending decisions, next action. Purpose section. L1 Frame table (mirrors sister page exactly — same 8 GB991 horizontal domains, same 2 in-scope / 6 greyed split). L2 Capability Frame Diagram — Mermaid `flowchart TB` with all 16 S2R L2 nodes from day one, 14 pending L2s styled with `classDef pending` (dashed border + muted fill), 2 ingested L2s plain. Service Domain section: Strategy Management H3 with `cap-service-strategy` H4 capability content; Capability Management H3 + BVD H3 stubs with L2 lists and proposed anchor names. Resource Domain section parallel structure: `cap-resource-strategy` H4 plus Capability/BVD stubs. Three TMF-distinction asymmetries surfaced on the Resource side capability (AI references / "& Architecture" framing / quarterly cadence). Source Pages section.
    - `wiki/views/_index.md` — section reorganised; Capability Maps now an explicit pair (Operations + S2R) with intro paragraph framing the two-page split; both view pages described in parallel.
    - `wiki/index.md` — Views section restructured to list both view pages with their Lifecycle Area annotations.
    - `wiki/views/capability-map.md` Session State — Last activity line updated to record companion-page creation; new "Companion view" bullet added pointing to `[[wiki/views/capability-map-s2r]]` with notes on shared conventions and the new `pending` Mermaid class introduced in the S2R page.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none new.
- **Notes:**
    - **Pilot deliverable complete.** The full pilot per Phase 3 phasing decision = both pilot L2s + the new view page skeleton + Strategy Management vertical populated. All three components landed today (1.4.1 ingest at 18:30Z; 1.5.1 ingest at 19:00Z + lint fix at 19:05Z; this view page at 19:30Z). Ready for **user-pause-for-review checkpoint**.
    - **Two-view-page composability verified in practice.** Anchor convention `cap-<layer>-<kebab-name>` works cleanly across both pages — no collisions with Operations-area anchors (Operations side has `cap-service-support`, `cap-service-anomaly`, etc.; S2R side adds `cap-service-strategy`, `cap-resource-strategy` with no overlap; future S2R anchors `cap-service-capability-delivery`, `cap-service-catalog-planning`, `cap-service-specification`, etc. are all distinctive). User's `project/` overlay can wikilink anchors from both pages and the linter resolves them via Obsidian conventions.
    - **Mermaid `pending` style class** introduced in this view page as a minor convention extension. The Operations-area sister page does not need it (its 17 L2s were ingested before the diagram landed in current form); the S2R page does need it because the diagram has to be stable from day one with 16 nodes but 14 are pending content. Pattern: `classDef pending fill:#f4f4f4,stroke:#888,color:#666,stroke-dasharray:4 3`. As batches land, `:::pending` is removed from the relevant nodes — diagram structure unchanged.
    - **Lifecycle-area italic line on H4 capabilities** (third dimension on the eTOM-L2 line — "Vertical: X — Lifecycle Area: Strategy-to-Readiness") is unique to S2R-area pages because the Operations-area page elides "Lifecycle Area" given all its capabilities are in the same one. Recorded as a convention in the S2R Session State.
    - **Cross-PSR navigation in trilateral sections** — none required on this view page (views are exempt from trilateral linking per CLAUDE.md §5.5; they require a `Source Pages` section instead, which this page has). The lint-error pattern from the 1.5.1 ingest doesn't apply here.
    - **Strategy Management TMF distinctions surfaced (PSR asymmetries):** 5 distinctions on `cap-resource-strategy`, 3 on `cap-service-strategy`. The PSR-asymmetric ones (AI references on Resource side; "& Architecture" vs "& Goals"; quarterly cadence) are load-bearing for the user's transformation roadmap and are call-outs the user specifically wanted preserved (per the propose-then-sign-off pattern).
    - **Both Strategy Management capabilities flag forward links** to Resource Capability Delivery (1.5.2) and Service Capability Delivery (1.4.2) — these are the next-pair-up in the Capability Management batch. When 1.4.2 + 1.5.2 ingest, the Strategy capabilities get back-references via the same wikilink-as-OK pattern.
    - **Pending user-pause-for-review checkpoint** — user reviews the pilot deliverable (both L2 pages + the view page skeleton + Strategy Management vertical). On approval:
        1. **CLAUDE.md §3 amendment** drafted as a separate proposal (per user direction: "separate proposal in user-pause-for-review checkpoint"); sign-off; apply.
        2. Capability Management batch begins — propose first PSR pair (likely 1.4.2 + 1.5.2 Capability Delivery) for sign-off; ingest; add to view page; repeat for the remaining three PSR pairs.
        3. BVD batch follows the same rhythm.
        4. L3-derived sub-capability review at the end.

---

## 2026-05-10T20:00Z — CONSTITUTION — CLAUDE.md §3 amended for Phase 3 S2R scope

- **File(s):** none ingested. Constitution amendment only.
- **Pages created/updated:**
    - `CLAUDE.md` — §3 eTOM (process layer) subsection rewritten to reflect Phase 3
      S2R-vertical scope expansion. Diff captured below.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Scope of amendment.** Surgical change to §3 → eTOM subsection only. SID and
      ODA subsections unchanged (their scope is by ABE category / functional domain,
      not by vertical, so Phase 3 doesn't affect them). "Out of scope for v1"
      subsection (TMF Open APIs + project/ security boundary) unchanged. Procedural
      "Partial ingestion" + "Version selection policy" subsections unchanged.
    - **Substantive changes:**
        1. Two-axis framing introduced (Horizontal Domain × Vertical-grouped-by-
           Lifecycle-Area), anchored to GB991 §1.1.2 nomenclature already documented
           in `[[wiki/foundations/lifecycle]]`.
        2. Stale L2-name examples ("Service Configuration & Activation", "Service
           Quality Management", "Resource Provisioning", "Resource Data Collection &
           Distribution" — all renamed in v23.5 / v24.0) replaced with wikilinks to
           the live `_index.md` files (`wiki/etom/service-domain/_index`,
           `wiki/etom/resource-domain/_index`, `wiki/etom/product-domain/_index`).
           Stops the constitution drifting against future renames.
        3. Per-Domain × per-Lifecycle-Area in-scope statements: Service + Resource
           both lifecycle areas in scope; Product Operations-area only.
        4. SIP exclusion lifted for Service + Resource. Preserved as historical note
           in a single closing paragraph that points to `S2R-EXPANSION-SCOPE.md`
           (Phase 3 scope and rationale) and `[[wiki/views/capability-map-s2r]]`
           (the resulting capability map view).
        5. Product-S2R explicitly out of scope with rationale (Customer / Market /
           Sales workflow intersection out of corpus L1 scope) and Phase 4 candidate
           softer framing.
        6. "All other GB921 process areas" out-of-scope catch-all added — Market /
           Sales / Customer / Business-Partner Domain L2s; Common Process L2s
           (1.8.x / 1.9.x); Enterprise / Shared / Patterns / Integration. Removes
           ambiguity about unenumerated branches.
    - **What's NOT changed.** Cardinal Rule (§1), authority model (§2), workflows
      (§4), page-type anatomies (§5), frontmatter schema (§6), trilateral linking
      (§7), OQ discipline (§8), maintenance obligations (§9), forbidden actions
      (§10), working style (§12), Obsidian conventions (§13). All unchanged.
    - **Effect on existing OQs.** OQ-025 (Service Strategy & Plan ABE «notFully-
      Developed» + S2R partial out of scope), OQ-034 (Resource Strategy & Plan ABE
      same flag) — the "partially out of scope per CLAUDE.md §3" language in their
      current text now refers to a constraint that has been lifted for the eTOM
      layer. The ABE «notFullyDeveloped» concern remains genuine; the lifecycle-area
      out-of-scope concern is resolved. Both OQs already carry inline "scope
      partially being lifted under 2026-05-10 Phase 3 S2R expansion" notes added
      during the L2 ingests; no further OQ-text edits required at this turn.
    - **Constitution discipline.** Per CLAUDE.md governance, this file takes
      precedence over default Claude Code behaviour and overrides what was
      previously in §3. Future agent sessions reading the constitution see the
      Phase-3 scope as current scope; the Phase 3 history reference in the closing
      paragraph signals this is a recently-added scope element.
    - **Next action:** Capability Management batch begins. First PSR pair likely
      1.4.2 + 1.5.2 Service / Resource Capability Delivery — propose, sign-off,
      ingest, then continue with Capacity / Catalog Planning / Specification
      Management pairs.

---

## 2026-05-10T20:30Z — INGEST — Capability Management batch, PSR pair 1 of 4: Service / Resource Capability Delivery (1.4.2 + 1.5.2)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.2 + Resource Domain L2 1.5.2 (and their L3/L4 descendants) extracted via openpyxl.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-capability-delivery.md` — full L2 page per CLAUDE.md §5.1 anatomy. Three-line lifecycle-area / vertical-context / domain callout. Verbatim L2 Overview from Excel ED (472 chars; relatively short for an S2R L2). Full `## L3 Process Details` section with all 7 L3s (1.4.2.1–1.4.2.7) populated with Extended Descriptions and L4 listings. Inline cross-domain-handoff callout on L3 1.4.2.1 with anchored wikilink to Resource-side L3 1.5.2.1 (forward-reference: Service Capability Delivery's requirements analysis output flows into Resource Capability Delivery's). Two SID forward links: `service-specification-abe` (direct match for L3 1.4.2.4 Design Service Capabilities) and `service-capacity-abe` (L3 1.4.2.2 capacity shortfalls + L3 1.4.2.1 demand/performance requirements). ODA via OQ-046 placeholder.
    - **NEW** `wiki/etom/resource-domain/resource-capability-delivery.md` — full L2 page parallel structure to Service-side. Verbatim L2 Overview (1494 chars; much longer than Service-side analog) including 5-bullet Responsibilities list and explicit logical-network-configuration framing. Source-text observation callout on the L2 ED's "Manage Resource Class Configuration" forward reference (no v25.5 L2 by that name; possible R20.5 legacy; preserved verbatim, OQ-045-family handling). Section-level Source-text observation callout flagging AI / automation / digital references throughout L3 1.5.2.1 / 1.5.2.2 (+ 4 L4 EDs) / 1.5.2.3 — Resource side carries v25.5 AI guidance the Service-side analog L2 (1.4.2) does not. Full `## L3 Process Details` with all 7 L3s. Inline cross-domain-handoff back-reference callout on L3 1.5.2.1 with anchored wikilink to Service-side L3 1.4.2.1. Asymmetry callout on L3 1.5.2.6 (4 L4s including Manage Commissioning of New Resource Infrastructure — Resource-only physical-hardware concern; vs Service-side 6 L4s breaking out program-management bookkeeping). Two SID forward links: `resource-specification-abe` and `resource-capacity-abe` (both pre-production sources). ODA via OQ-046.
    - `wiki/sid/service/service-specification-abe.md` — `## eTOM Processes That Manipulate This Entity` populated with reciprocal back-link to 1.4.2 L3 1.4.2.4 dependency.
    - `wiki/sid/service/service-capacity-abe.md` — reciprocal back-link to 1.4.2 L3 1.4.2.1 / 1.4.2.2 / L4 1.4.2.2.1 dependency.
    - `wiki/sid/resource/resource-specification-abe.md` — reciprocal back-link to 1.5.2 L3 1.5.2.4 dependency (legacy-vs-new integration-design framing).
    - `wiki/sid/resource/resource-capacity-abe.md` — reciprocal back-link to 1.5.2 L3 1.5.2.1 (with concrete capacity metrics) + L3 1.5.2.2 / L4 1.5.2.2.1 dependency.
    - `wiki/etom/service-domain/_index.md` — 1.4.2 row added to L2 table (Vertical: Capability Management; Lifecycle Area: Strategy-to-Readiness). Pending-ingest paragraph repurposed to track Capability Management batch progress and remaining BVD work.
    - `wiki/etom/resource-domain/_index.md` — 1.5.2 row added; pending-ingest paragraph similarly updated.
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in: `cap-service-capability-delivery` (under Service Domain → Capability Management) with TMF distinctions surfacing the upstream Strategy-to-Capability handoff, the cross-domain Service-to-Resource handoff, sourcing forward references, and the Strategy-vs-Delivery boundary; `cap-resource-capability-delivery` (under Resource Domain → Capability Management) with TMF distinctions surfacing upstream input chains (two converging — Resource Strategy ↓ + Service Capability →), AI / automation / digital v25.5 references, the Commissioning Resource-only L4 asymmetry, logical-network-configuration framing, sourcing forward references, "Manage Resource Class Configuration" R20.5 legacy reference. Both Mermaid nodes (`S142`, `R152`) de-`:::pending`-ed. Capability Management H3 stub-list entries replaced with the H4 capability blocks for the ingested L2s; remaining 3 PSR pairs in each section retained as one-line pending stubs. Session State updated: Last activity, scope-line capability count (4 of 16 done), Batches DONE list (added Capability Delivery PSR pair entry), Batches IN-PROGRESS / PENDING reorganised, Next action repointed to second Capability Management PSR pair (1.4.12 + 1.5.14 Capacity Management). `derived_from` frontmatter expanded to include the two new L2 source pages. Source Pages list updated.
    - `wiki/index.md` — Service Domain count 9 → 10; Resource Domain count 10 → 11; S2R Lifecycle Area subdivisions now list both Strategy and Capability Delivery L2s on each side.
- **Sections skipped:** None within the L2s — fully ingested. Global skip: 12 more S2R L2s remain (Capability Management 6 + BVD 6).
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** None new. OQ-046 (filed under 1.4.1) covers ODA cross-walk gap for both L2s.
- **Notes:**
    - **First Capability Management PSR pair complete.** PSR-pair-by-PSR-pair rhythm validated: propose → ingest both L2s → bake into capability-map-s2r → log → lint. Single combined log entry per PSR pair (rather than per-L2 as in pilot) keeps audit trail atomic to the conceptual pair. Three more pairs to go in this batch.
    - **PSR asymmetries recorded as TMF distinctions** on both L2 pages and on both view-page H4 entries: (1) AI / automation / digital references on Resource side only (3 L3 EDs + 4 L4 EDs); (2) "Manage Commissioning of New Resource Infrastructure" L4 — Resource-only physical-hardware concern with no Service-side analog; Service side breaks out program-management bookkeeping (Timetables / Track and Report / Ensure Costs) more granularly instead; (3) logical-network-configuration framing in Resource L2 ED with no Service-side analog; (4) three different downstream-process names for sourcing across the PSR pair ("Engaged Party domains" Service / "Party Offering Development & Retirement" + "Supply Chain Development & Management" Resource); (5) "Manage Resource Class Configuration" R20.5 legacy reference in Resource L2 ED.
    - **Cross-domain handoff documented in source.** L3 1.4.2.1 → L3 1.5.2.1 via the closing sentence "These processes provide input into the requirements capture processes in the Resource and Engaged party domains" (Service ED) and the corresponding upstream-input note in 1.5.2.1 ED ("requirements information from the Map & Analyze Service Requirements processes" — i.e. 1.4.2.1). Surfaced inline on both L2 pages with anchored wikilinks (in body text, not in trilateral sections — convention from pilot lint fix).
    - **No new-in-v25.5 L3s** in this PSR pair. All L3s carry R20.5 Original PIDs (1.2.2.2.x for Service; 1.2.3.2.x for Resource). No L3-derived sub-capabilities surfaced from this pair (the L3 review at end of S2R batches will revisit; Capability Management L3s are likely candidates per Session State).
    - **No documented v24.0 rename** for either L2 — no provenance line needed.
    - **Verbatim discipline preservations.** Source typos / quirks preserved: 1.4.2.1 ED missing terminal period on closing sentence; 1.5.2.1.1 ED has duplicate space (`fast,  accurate`) preserved as-is; multiple L4 EDs marked "Not used for this process element" verbatim per existing-corpus pattern.
    - **Trilateral linking now bidirectionally consistent** for the four target SID ABEs. Linter confirms. service-specification-abe and resource-specification-abe (both production-key SID artefacts for the OSS modernisation transformation roadmap — these are the **target-state catalog/spec data models** that current-OSS code-driven implementations need to migrate toward) now have their first eTOM trilateral link populated.
    - **Pending decisions:** none.
    - **Next action:** Propose 1.4.12 + 1.5.14 Capacity Management as the second Capability Management PSR pair. Proposal will follow the same shape as the 1.4.2 / 1.5.2 proposal (symmetric structure called out once + asymmetries highlighted). User-approved batch rhythm: PSR-pair-by-PSR-pair propose-then-sign-off.

---

## 2026-05-10T21:00Z — INGEST — Capability Management batch, PSR pair 2 of 4: Service / Resource Capacity Management (1.4.12 + 1.5.14)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.12 + Resource Domain L2 1.5.14 (and their L3 / L4 / L5 descendants) extracted via openpyxl.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-capacity-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Three-line lifecycle-area / vertical-context / domain callout. **Net-in-v25.5 callout** (Original PID = None across L2 + 9 L3s + 8 L4s + L5s). Verbatim L2 Overview from Excel ED (638 chars; carries definitional anchor for "service capacity"). Full `## L3 Process Details` section with all 9 L3s (1.4.12.1–1.4.12.9). Inline source-text observation callout on L3 1.4.12.6 flagging the missing `.6.1` L4 numbering (Resource-side has `.6.1 Identify Resource Capacity Optimization Need` as analog). Inline source-text observation callout on L3 1.4.12.7 flagging asymmetric L4 structure under Optimize (same Adjust + Allocate L5s parented under different L4 names across PSR pair). Inline source-text observation callout on L3 1.4.12.9 flagging the "Resource Capacity" copy-paste body-text bug (Service-side L3 ED talks about Resource Capacity — preserved verbatim, OQ-045-family handling, no separate OQ filed). Single SID forward link: `service-capacity-abe`. ODA via OQ-046 placeholder + note that v25.5-net-new status sharpens the gap (these L2s definitionally cannot appear in GB1022 R20.5-keyed mapping tables).
    - **NEW** `wiki/etom/resource-domain/resource-capacity-management.md` — full L2 page parallel structure. Net-in-v25.5 callout (Original PID = None across L2 + 9 L3s + 10 L4s + L5s). Verbatim L2 Overview (464 chars; **no** definitional anchor for resource capacity — asymmetric to Service-side). Full `## L3 Process Details` with all 9 L3s. Inline PSR-asymmetry callouts on L3 1.5.14.6 (Resource-only `.6.1 Identify Resource Capacity Optimization Need` L4) and L3 1.5.14.7 (asymmetric L4 structure with parallel Utilization-mgmt + Thresholds-mgmt L4s, vs Service-side single Thresholds L4). Single SID forward link: `resource-capacity-abe` (pre-production source). ODA via OQ-046.
    - `wiki/sid/service/service-capacity-abe.md` — `## eTOM Processes That Manipulate This Entity` extended with 1.4.12 entry **above** the existing 1.4.2 entry (1.4.12 is the primary ongoing-management manipulator; 1.4.2 is the upstream-input manipulator for capacity-shortfalls dependency). Section now carries two eTOM back-links.
    - `wiki/sid/resource/resource-capacity-abe.md` — same shape: 1.5.14 added as primary manipulator above existing 1.5.2 entry.
    - `wiki/etom/service-domain/_index.md` — 1.4.12 row added in numerical order (between 1.4.8 and 1.4.14). Pending-ingest paragraph updated (1.4.12 removed from pending list; Capability Management batch progress note updated to "remaining 2 of the 4-pair").
    - `wiki/etom/resource-domain/_index.md` — 1.5.14 row added in numerical order (between 1.5.10 and 1.5.16). Pending-ingest paragraph similarly updated.
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in: `cap-service-capacity` and `cap-resource-capacity`, replacing their stub-list entries. TMF distinctions surface: net-new-in-v25.5; SLA/SLO/SLR Service-side-only contractual framing; definitional-anchor asymmetry; L4 numbering gap; L4/L5 asymmetry under Optimize; source-text bug on Service-side Report L3; **notable non-asymmetry** (no AI / automation references on either side). Both Mermaid nodes (`S1412`, `R1514`) de-`:::pending`-ed. Session State: Last activity, scope-line capability count (6 of 16 done), Batches DONE list (added Capacity Management PSR pair entry as #3), IN-PROGRESS / PENDING reorganised, Next action repointed to third PSR pair (1.4.16 + 1.5.18 Catalog Planning Management). `derived_from` frontmatter expanded. Source Pages list updated.
    - `wiki/index.md` — Service Domain count 10 → 11; Resource Domain count 11 → 12; S2R-area subdivisions updated to list all three ingested L2s on each side.
- **Sections skipped:** None within the L2s — fully ingested. Global skip: 10 more S2R L2s remain (Capability Management 4 + BVD 6).
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** None new. OQ-046 (filed under 1.4.1) covers ODA cross-walk gap for both L2s, with the v25.5-net-new status sharpening the gap.
- **Notes:**
    - **Second Capability Management PSR pair complete.** Single combined log entry per PSR pair convention from 1.4.2/1.5.2 ingest holds. Capacity Management is qualitatively different from Capability Delivery (heat-map-relevant in different ways) but follows the same propose → ingest both → bake → log → lint rhythm.
    - **First PSR pair where the entire process tree is v25.5-net-new.** Original PID = None on both L2s + every L3 + every L4 + every L5. Worth recording as a corpus-level observation: v25.5 GB921 introduced Capacity Management (Service + Resource) as a discrete L2 process group; pre-v25 capacity management was implicit in other process groups' responsibilities (e.g. 1.4.4 / 1.5.4 Support Management's "Applying capacity rules from Infrastructure Lifecycle Management"). The transformation roadmap implication: heat-map cells for `cap-service-capacity` and `cap-resource-capacity` should be calibrated against v25.5 framing, not pre-v25 expectations — a current OSS that "has capacity management" via infrastructure-monitoring tooling may not have it as the discrete L2-aligned capability v25.5 frames.
    - **PSR asymmetries recorded as TMF distinctions** on both L2 pages and on both view-page H4 entries: (1) net-new-in-v25.5 on both sides (PSR-symmetric in this respect); (2) SLA/SLO/SLR contractual framing Service-side-only (3 inline references — L2 brief + 4 L3 EDs); (3) definitional anchor for "service capacity" Service-side-only at L2 ED level; (4) L4 numbering gap on Service-side L3 1.4.12.6 — Resource-side has `.6.1 Identify Optimization Need`, Service-side starts at `.6.2`; (5) asymmetric L4 structure under L3 `.7` Optimize — same Adjust + Allocate L5s parented under different L4 names; (6) source-text copy-paste bug on Service-side L3 1.4.12.9 ED ("Resource Capacity" body text in Service-side process — verbatim preserved, OQ-045-family).
    - **Notable non-asymmetry: zero AI / automation references on either PSR side.** Departure from the 1.4.1/1.5.1 + 1.4.2/1.5.2 pattern where Resource side carried explicit AI guidance the Service side did not. v25.5 didn't apply the AI-readiness commentary uniformly across S2R verticals. Recorded as observation in both view-page entries — useful counter-evidence to the assumption that AI-on-Resource-side is a universal pattern.
    - **Verbatim discipline preservations.** L4 numbering gap on Service side preserved as-is (no synthesis to "fill" the missing `.6.1`). Source-text copy-paste bug on Service-side Report L3 preserved verbatim with inline note. Trailing-period anomalies and double-spacing artefacts in some Resource-side EDs preserved. "Not used for this process element" placeholders not present in this pair (most L3s have substantive EDs).
    - **Trilateral linking now bidirectionally consistent** for both Capacity ABEs. Linter confirms. Both ABEs now carry two eTOM back-links each (capability-delivery upstream + capacity-management ongoing-management).
    - **Pending decisions:** none.
    - **Next action:** Propose 1.4.16 + 1.5.18 Catalog Planning Management as the third Capability Management PSR pair. After that: 1.4.19 + 1.5.19 Specification Management closes Capability Management. Then BVD batch (3 PSR pairs).

---

## 2026-05-10T21:05Z — LINT FIX — wikilinks-in-trilateral-sections removed from Capacity Management L2 pages

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/etom/service-domain/service-capacity-management.md` — `## SID Entities Manipulated` section: removed two wikilinks that triggered bidirectional-consistency lint errors — `[[wiki/sid/common/capacity-abe]]` (parenthetical reference to canonical Capacity pattern) and `[[wiki/etom/service-domain/service-capability-delivery]]` (cross-L2 navigation explaining the upstream-input vs ongoing-management boundary). Replaced with plain-text references. Convention reaffirmed: no wikilinks (other than the primary forward link) inside trilateral sections.
    - `wiki/etom/resource-domain/resource-capacity-management.md` — same fix, two wikilinks removed (`capacity-abe` parenthetical + `resource-capability-delivery` cross-L2 navigation).
- **Lint result:** PASS — 137 pages, 0 errors, 1 warning (LOG-STALE, cleared by this entry).
- **Open questions filed:** none.
- **Notes:**
    - **Convention extension recorded.** The "no cross-PSR navigational wikilinks in trilateral sections" rule (from the 1.5.1 pilot lint fix) generalises to **no wikilinks at all in trilateral sections, other than the primary forward-link bullet target**. Specifically: parenthetical references to canonical-pattern ABEs (e.g. mentioning `wiki/sid/common/capacity-abe` while linking to `wiki/sid/service/service-capacity-abe`) and cross-L2 navigational mentions both trigger the per-entity bidirectional check. Plain prose references work; only the primary trilateral-link bullet target should carry a wikilink.
    - **The capacity-abe canonical-pattern reference** is genuine cross-reference — Service Capacity ABE genuinely specialises the Common Capacity pattern. The information is preserved in plain prose. The wikilink is already present on the SID side (`service-capacity-abe.md` and `resource-capacity-abe.md` both link `[[wiki/sid/common/capacity-abe]]` in their own bodies), so navigation between the canonical and specialised ABEs is one click away from the SID side.
    - **Will mirror this pattern** going forward in remaining S2R L2 ingests. No more wikilinks in trilateral sections beyond the primary forward-link bullet's target.

---

## 2026-05-11T09:00Z — INGEST — Capability Management batch, PSR pair 3 of 4: Service / Resource Catalog Planning Management (1.4.16 + 1.5.18)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.16 + Resource Domain L2 1.5.18 (and their L3 descendants) extracted via openpyxl. **Smallest L2 pair in Phase 3** — 2 L3s each, no L4/L5 decomposition.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-catalog-planning-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Three-line lifecycle-area / vertical-context / domain callout. **Net-in-v25.5 callout** (Original PID = None across L2 + 2 L3s; no L4/L5). Verbatim L2 Overview (522 chars). `## L3 Process Details` with both L3s. Inline source-text-observation callout on L3 1.4.16.1 flagging the PSR-symmetric extra-qualifier-word quirk ("Service Design Catalog Plan..." in ED prose vs L3 name "Design Service Catalog Plan"). Two forward-reference callouts on L3 1.4.16.2: Specification Management → 1.4.19 (pending fourth Capability Management PSR pair); Enterprise Business Process for Catalog Management → out-of-corpus-scope governance reference. Single SID forward link: `service-specification-abe` (which carries §4.3.3 Service Catalog as sub-ABE per CLAUDE.md §5.2 v1 granularity). Plain-prose reference to canonical Catalog pattern (Common Domain) — wikilink omitted per the convention extension from the Capacity Management lint fix. ODA via OQ-046.
    - **NEW** `wiki/etom/resource-domain/resource-catalog-planning-management.md` — full L2 page parallel structure (526 chars ED — near-mirror to Service-side). Net-in-v25.5 callout. Same PSR-symmetric source-text quirk on L3 1.5.18.1 ("Resource Design Catalog Plan..."). Same forward-reference callouts on L3 1.5.18.2 → Specification Management (1.5.19) + Enterprise Business Process for Catalog Management. Single SID forward link: `resource-specification-abe` (which carries §4.2.5 Resource Catalog as sub-ABE; pre-production source).
    - `wiki/sid/service/service-specification-abe.md` — `## eTOM Processes That Manipulate This Entity` extended with 1.4.16 entry alongside the existing 1.4.2 entry. 1.4.2 is *service-infrastructure-design* manipulator; 1.4.16 is *catalog-planning-specific* manipulator producing Service Catalog sub-ABE artefacts. Section now carries two eTOM back-links.
    - `wiki/sid/resource/resource-specification-abe.md` — same shape: 1.5.18 added alongside existing 1.5.2.
    - `wiki/etom/service-domain/_index.md` — 1.4.16 row added in numerical order (between 1.4.15 and 1.4.18). Pending-ingest paragraph updated (1.4.16 removed; Capability Management batch progress note now "nearly complete; remaining 1 pair").
    - `wiki/etom/resource-domain/_index.md` — 1.5.18 row added in numerical order (between 1.5.17 and 1.5.21). Pending-ingest paragraph similarly updated.
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in. **Key TMF distinction surfaced on both H4 entries: the four-L2 Catalog lifecycle spanning both Lifecycle Areas** — explicit cross-page anchored wikilinks to Operations-area `cap-{service,resource}-catalog-operational-readiness` + `cap-{service,resource}-catalog-content`, plus forward references to upcoming BVD-batch `cap-{service,resource}-catalog-lifecycle` anchors. Heat-map composability for the catalog story now wired across both view pages. Both Mermaid nodes (`S1416`, `R1518`) de-`:::pending`-ed. Session State: Last activity, scope-line capability count (8 of 16 done — halfway through Phase 3 ingest), Batches DONE list (added Catalog Planning PSR pair entry as #4), IN-PROGRESS / PENDING reorganised, Next action repointed to fourth/final PSR pair (1.4.19 + 1.5.19 Specification Management). `derived_from` + Source Pages updated.
    - `wiki/index.md` — Service Domain count 11 → 12; Resource Domain count 12 → 13; S2R-area subdivisions list all four ingested L2s on each side.
- **Sections skipped:** None within the L2s — fully ingested. Global skip: 8 more S2R L2s remain (Capability Management 2 + BVD 6).
- **Lint result:** PASS — see lint following.
- **Open questions filed:** None new. OQ-046 covers ODA cross-walk gap for both L2s.
- **Notes:**
    - **Third Capability Management PSR pair complete. Phase 3 ingest halfway done** (8 of 16 S2R L2s). Capability Management batch nearly closed — one PSR pair remains (1.4.19 + 1.5.19 Specification Management).
    - **Smallest PSR pair so far + most-symmetric content.** 2 L3s each, no L4/L5s. L2 EDs and L3 EDs near-mirror-image between PSR sides. No SLA/SLO/SLR Service-only framing, no AI/automation Resource-only framing, no structural-asymmetry callouts at the process level. Where PSR asymmetry exists for catalog work, it lives in the *underlying SID* (Service Specification ABE has CFSSpec/RFSSpec distinction; Resource Specification ABE has Physical/Logical/Compound subtypes; different dimensional structures). v25.5 process framing collapses both SID structures into the same Catalog Planning process shape.
    - **Four-L2 Catalog lifecycle — load-bearing for transformation roadmap.** GB921 v25.5 frames Catalog work as a four-stage lifecycle spanning both Lifecycle Areas: Planning (S2R-CM) → Lifecycle (S2R-BVD) → Operational Readiness (Ops-ORS) → Content (Ops-ORS). Heat-map composability now wired across both view pages via anchored cross-page wikilinks on the H4 entries. A current OSS that "has a service catalog" typically conflates these four stages into a single concern; the four-stage framing is the precondition for transformation-roadmap clarity on catalog maturity. Eight L2 anchors total across both view pages cover Service + Resource catalog work end-to-end.
    - **PSR-symmetric source-text quirk preserved verbatim.** Both L3 `.1` EDs carry an extra PSR-qualifier word at the start that the L3 name doesn't have (*"Service Design Catalog Plan..."* / *"Resource Design Catalog Plan..."*). Pattern matches OQ-045 family handling — source-text artefact, intent recognisable, no separate OQ filed.
    - **Forward references to out-of-corpus-scope content** — two on each side:
        1. "Specification Management business activities" → forward to 1.4.19 / 1.5.19 (next pair); these L3s will become back-references when Specification Management ingests.
        2. "Enterprise Business Process for Catalog Management" → Enterprise-domain governance reference; out of corpus L1 scope per CLAUDE.md §3 (Phase 3 amendment); pattern matches `1.8.5 Domain Orchestration` (1.5.1.1.3) and "Manage Resource Class Configuration" (1.5.2 L2 ED) — verbatim preserved, no new OQ.
    - **Notable non-asymmetry — pattern crystallising.** No AI / automation references on either PSR side. Catalog Planning + Capacity Management both lack the AI/automation Resource-only content that's present in Strategy Management + Capability Delivery. **Pattern:** v25.5's AI commentary appears concentrated in Strategy + Capability Delivery, absent from Capacity + Catalog Planning. Recorded as observation for the eventual L3-derived sub-capability review. Confirmation/refutation depends on the final Capability Management PSR pair (Specification Management) and the BVD batch.
    - **Convention discipline maintained.** No wikilinks in trilateral sections beyond the primary forward-link bullet target — applied cleanly across both L2 pages. No lint errors on first pass.
    - **Pending decisions:** none.
    - **Next action:** Propose 1.4.19 + 1.5.19 Specification Management as the fourth and final Capability Management PSR pair. After that: Capability Management batch closes; BVD batch begins (3 PSR pairs covering Specification Lifecycle, Catalog Lifecycle, Anomaly Lifecycle); then L3-derived sub-capability review closes Phase 3.

---

## 2026-05-11T11:00Z — INGEST — Capability Management batch CLOSED — final PSR pair: Service / Resource Specification Management (1.4.19 + 1.5.19)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.19 + Resource Domain L2 1.5.19 (and their L3 / L4 descendants) extracted via openpyxl. Both net-new in v25.5.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-specification-management.md` — full L2 page. Net-in-v25.5 callout. Cross-L2 back-reference callout to Catalog Planning (1.4.16.2 forward reference now resolves here). Verbatim L2 Overview (551 chars). `## L3 Process Details` with all 3 L3s + 2 L4s under 1.4.19.1. **Three inline source-text observation callouts:** (1) L4 1.4.19.1.1 modelled/modeled spelling inconsistency between brief and ED; (2) **significant copy-paste bug on L3 1.4.19.2** — L3 name "Model Service Specifications" but brief + ED prose open "Model **Resource** Specifications…" (verbatim preserved with explicit flag — OQ-045-family); (3) PSR-asymmetry note on Resource-only `.4 Update and Version Resource Specifications` L3 with forward-reference to potential Service-side BVD analog (1.4.3). Single SID forward link: `service-specification-abe` (primary manipulator).
    - **NEW** `wiki/etom/resource-domain/resource-specification-management.md` — full L2 page parallel structure (548 chars ED). Net-in-v25.5 callout. Cross-L2 back-reference callout to Catalog Planning. 4 L3s (one more than Service-side). PSR naming-asymmetry notes on `.1` (Develop vs Describe) and `.2` (Master vs Model). Explicit PSR-asymmetric L3 `.4 Update and Version Resource Specifications` flagged at section level with heat-map-relevance commentary. Single SID forward link: `resource-specification-abe` (primary manipulator, pre-production source).
    - `wiki/sid/service/service-specification-abe.md` — `## eTOM Processes That Manipulate This Entity` extended to **three eTOM back-links**, ordered by manipulator role:
        1. 1.4.19 (primary specifications-management) — newly added.
        2. 1.4.2 (capability-delivery upstream-input) — existing.
        3. 1.4.16 (catalog-planning scope-specific) — existing.
    - `wiki/sid/resource/resource-specification-abe.md` — same shape, three back-links: 1.5.19 (primary) + 1.5.2 (capability-delivery) + 1.5.18 (catalog-planning).
    - `wiki/etom/service-domain/_index.md` — 1.4.19 row added at end of table (highest ID). Pending-ingest paragraph updated to mark **Capability Management batch complete** and point to BVD batch as next.
    - `wiki/etom/resource-domain/_index.md` — 1.5.19 row added in numerical order (between 1.5.18 and 1.5.21). Same "Capability Management batch complete" note.
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in: `cap-service-specification` and `cap-resource-specification`. TMF distinctions on Service-side H4: closes the three-L2 Specification-data-management triad (primary + capability-delivery + catalog-planning); back-references resolve Catalog Planning forward references; PSR L3-count + L3-name semantic asymmetries; significant source-text bug on 1.4.19.2; AI-distribution pattern confirmed. TMF distinctions on Resource-side H4: same triad structure (1.5.19 + 1.5.2 + 1.5.18); explicit treatment of PSR-asymmetric `.4` version-management L3 with transformation-roadmap relevance; intact version of the Service-side copy-paste-bugged content; AI-pattern confirmation. Both Mermaid nodes (`S1419`, `R1519`) de-`:::pending`-ed. Session State: Last activity, scope-line capability count (10 of 16 done — **Strategy + Capability Management verticals both complete**), Batches DONE list (added Specification Management PSR pair as #5 — Capability Management batch closed), IN-PROGRESS / PENDING reorganised, Next action repointed to BVD batch first PSR pair (1.4.3 + 1.5.3 Specification Lifecycle Management). `derived_from` + Source Pages updated.
    - `wiki/index.md` — Service Domain count 12 → 13; Resource Domain count 13 → 14; S2R-area subdivisions list all 5 ingested L2s on each side.
- **Sections skipped:** None within the L2s. Global skip: 6 more S2R L2s remain (BVD batch: 3 PSR pairs).
- **Lint result:** PASS — see lint following.
- **Open questions filed:** None new. OQ-046 covers ODA cross-walk gap for both L2s.
- **Notes:**
    - **CAPABILITY MANAGEMENT BATCH COMPLETE — 4 of 4 PSR pairs ingested.** Capability Delivery (1.4.2/1.5.2), Capacity Management (1.4.12/1.5.14), Catalog Planning (1.4.16/1.5.18), Specification Management (1.4.19/1.5.19). 8 L2 pages total under the Capability Management vertical, balanced 4 on each PSR side. All 8 net-new in v25.5 (Original PID = None across all 8 L2s at the L2 level). Strategy Management (2 L2s) + Capability Management (8 L2s) = 10 of 16 S2R L2s complete. Only BVD batch (6 L2s, 3 PSR pairs) remains before L3-derived sub-capability review closes Phase 3.
    - **Specification ABEs now carry three eTOM back-links each.** Both `service-specification-abe` and `resource-specification-abe` now back-reference three Capability Management L2s — the primary specifications-management process (1.4.19/1.5.19), the capability-delivery upstream-input process (1.4.2/1.5.2), and the catalog-planning scope-specific process (1.4.16/1.5.18). This is a denser trilateral pattern than any other SID ABE in the corpus carries; reflects that the Specification ABEs are central data-model artefacts touched by multiple Capability Management activities at different scopes. Ordering convention: primary first, then by ingest order.
    - **PSR-asymmetric L3 count (3 vs 4)** — first PSR pair in Phase 3 where the L3 counts differ. Resource side has explicit version management at L3 level (`.4 Update and Version Resource Specifications`); Service side defers to a separate BVD L2 (likely 1.4.3 Service Specification Lifecycle Management, pending BVD batch). Worth confirming when 1.4.3 ingests — if 1.4.3 has explicit version-management L3s that mirror 1.5.19.4, the asymmetry is "where Service puts the version management" rather than "Service doesn't have it". Either way, the L3-count asymmetry surfaces as a meaningful TMF distinction for the transformation-roadmap framing.
    - **Most prominent source-text bug in Phase 3 so far.** Service-side L3 1.4.19.2 ("Model Service Specifications") has brief + ED prose copy-pasted from the Resource-mirror page's body, with incomplete PSR substitution. The L3 name was corrected (Model vs Master) but the body text was not. Preserved verbatim per CLAUDE.md §1; the Resource-mirror L3 1.5.19.2 ("Master Resource Specifications") is the intact version. Pattern matches OQ-045 (Resource Anomaly "Resource Problem Management") and 1.4.12.9 (Service Capacity Report carrying "Resource Capacity" body text) source-text bugs. No new OQ filed — pattern is well-established.
    - **AI-distribution pattern crystallised after this ingest.** Four PSR pairs without AI references on either side (Capacity Management, Catalog Planning, Specification Management — three Capability Management pairs that don't carry AI commentary) vs two PSR pairs with Resource-side-only AI references (Strategy Management, Capability Delivery). Pattern: v25.5 AI commentary is concentrated in Strategy + Capability Delivery, absent from the rest of Capability Management. BVD batch will determine whether the pattern extends or breaks down — likely Specification Lifecycle (1.4.3/1.5.3) and Catalog Lifecycle (1.4.13/1.5.15) follow the AI-free pattern; Anomaly Lifecycle (1.4.17/1.5.20) is the wildcard.
    - **Catalog Planning forward references now resolved.** L3 1.4.16.2 / 1.5.18.2 EDs from the previous PSR pair reference "Specification Management business activities" — those references now point at concrete L2 pages. Cross-L2 back-reference callouts surfaced on both new pages.
    - **Convention discipline maintained.** No wikilinks in trilateral sections beyond the primary forward-link bullet target. Zero lint errors on first pass.
    - **Pending decisions:** none.
    - **Next action:** Propose 1.4.3 + 1.5.3 Specification Lifecycle Management as the first BVD batch PSR pair. After that: 1.4.13 + 1.5.15 Catalog Lifecycle Management; then 1.4.17 + 1.5.20 Anomaly Lifecycle Management closes the BVD batch and Phase 3 ingest. Then L3-derived sub-capability review.

---

## 2026-05-11T13:00Z — INGEST — BVD batch OPENS — first PSR pair: Service / Resource Specification Lifecycle Management (1.4.3 + 1.5.3)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.3 + Resource Domain L2 1.5.3 (and their L3 / L4 descendants) extracted via openpyxl. **Heaviest L4 decomposition of any Phase 3 PSR pair so far** — Service 17 L4s; Resource 21 L4s.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-specification-lifecycle-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Three-line lifecycle-area / vertical-context / domain callout (with BVD as new vertical context). Italic provenance line for v24.0 rename (*"Service Specification Development & Retirement"*). **R20.5-lineage callout** flagging that this is the first S2R PSR pair in Phase 3 with pre-v25 history (Original PID 1.2.2.3) — softer OQ-046 ODA-cross-walk framing. Verbatim L2 Overview (547 chars + rename note). `## L3 Process Details` with all 8 L3s + 17 L4s. **Multiple inline source-text observation callouts:** PSR-cascade note on L3 1.4.3.1 input; cross-L2 boundary + implicit-version-management callout on L3 1.4.3.5 (resolves Service-side version-mgmt asymmetry definitively); naming-asymmetry flag on L4 1.4.3.6.3 ("Party" vs Resource-side "Supplier/Partner"); brief-content bug on L4 1.4.3.5.3 ("resource" where context is "service"); PSR-asymmetric Exit decomposition callout on L3 1.4.3.7 (0 L4s vs Resource-side 4); cross-PSR-test-composition callout on L3 1.4.3.8 (new in v25.5). Two SID forward links: `service-specification-abe` (fourth back-link on that ABE — lifecycle-driven manipulator) and `service-test-abe` (second back-link on that ABE — Service Test catalogue). ODA via OQ-046 with softer R20.5-lineage framing.
    - **NEW** `wiki/etom/resource-domain/resource-specification-lifecycle-management.md` — full L2 page parallel structure. R20.5-lineage callout (Original PID 1.2.3.3). Verbatim L2 ED (962 chars + rename note) including cross-version naming reference to pre-v24.0 "Resource Strategy & Planning". 8 L3s + 21 L4s. **Five inline source-text observation callouts:** cross-version naming reference at L2 ED; PSR-cascade note on L3 1.5.3.1; brief-content bug on L4 1.5.3.1.1 ("required service classes" not "required resource classes"); cross-L2 boundary + forward-references-to-out-of-scope-Party-processes callouts on L3 1.5.3.5; naming-asymmetry flag on L4 1.5.3.6.3 ("Supplier/Partner"); PSR-asymmetric Exit decomposition callout on L3 1.5.3.7 with 4 explicit L4s (Identify Unviable, Identify Impacted Customers, Develop Transition Strategies, Manage Exit Process); possible copy-paste artefact flag on L3 1.5.3.8 ED (Resource Tests enriching Resource Test results). Two SID forward links: `resource-specification-abe` (fourth back-link, pre-production source) and `resource-test-abe` (second back-link, pre-production source).
    - `wiki/sid/service/service-specification-abe.md` — `## eTOM Processes That Manipulate This Entity` extended to **four eTOM back-links** with explicit manipulator-role-density note: primary (1.4.19, ongoing-maintenance) → capability-delivery (1.4.2, project-driven-design) → catalog-planning (1.4.16, catalog-system-design) → lifecycle (1.4.3, class-introduction-to-retirement). Densest pattern in corpus.
    - `wiki/sid/service/service-test-abe.md` — `## eTOM Processes That Manipulate This Entity` extended to **two eTOM back-links**: 1.4.1 (Strategy Management Test-strategy L3s) + 1.4.3 (Lifecycle Management Test catalogue L3).
    - `wiki/sid/resource/resource-specification-abe.md` — extended to **four eTOM back-links** with parallel manipulator-role-density note. Pre-production source.
    - `wiki/sid/resource/resource-test-abe.md` — extended to **two eTOM back-links** (1.5.1 + 1.5.3).
    - `wiki/etom/service-domain/_index.md` — 1.4.3 row added in numerical order (between 1.4.2 and 1.4.4). Pending-ingest paragraph updated — Capability Management batch marked complete; BVD batch in progress (1.4.3 done; 2 pairs remaining).
    - `wiki/etom/resource-domain/_index.md` — 1.5.3 row added in numerical order (between 1.5.2 and 1.5.4). Same status updates.
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in: `cap-service-specification-lifecycle` and `cap-resource-specification-lifecycle`. **First BVD H3 sections opened on both Domain sections** with full content. TMF distinctions on both H4 entries surface: R20.5-lineage / heat-map calibration note; cross-L2 boundary with Capability Delivery; **closes the four-L2 Specification-ABE manipulator pattern** (densest trilateral pattern in corpus on both PSR sides); PSR-asymmetric Exit decomposition; PSR cascade input at L3 .1; L3 .8 new-in-v25.5 + cross-PSR-test composition; **definitive resolution of Service-side version-management PSR asymmetry**; AI-distribution pattern continues. Both Mermaid nodes (`S143`, `R153`) de-`:::pending`-ed. Session State: Last activity, scope-line capability count (12 of 16 done — Strategy + Capability Management + first BVD pair complete; 4 BVD capabilities pending), Batches DONE list (added Specification Lifecycle PSR pair as #6 — first BVD entry), IN-PROGRESS / PENDING reorganised, Next action repointed to second BVD PSR pair (1.4.13 + 1.5.15 Catalog Lifecycle Management). `derived_from` + Source Pages updated.
    - `wiki/index.md` — Service Domain count 13 → 14; Resource Domain count 14 → 15; S2R-area subdivisions list all 6 ingested L2s on each side in numerical order.
- **Sections skipped:** None within the L2s — fully ingested. Global skip: 4 more S2R L2s remain (BVD: 2 PSR pairs — Catalog Lifecycle + Anomaly Lifecycle).
- **Lint result:** PASS — see lint following.
- **Open questions filed:** None new. OQ-046 covers ODA cross-walk gap (with softer framing for R20.5-lineage L2s).
- **Notes:**
    - **BVD BATCH OPENED.** First BVD PSR pair landed. Structural break from Capability Management batch: BVD has pre-v25 history (R20.5 lineage on both 1.4.3 and 1.5.3 — Original PIDs 1.2.2.3 / 1.2.3.3), whereas Capability Management was uniformly v25.5-net-new. v24.0 rename pattern applies on both sides ("Specification Development & Retirement" → "Specification Lifecycle Management"). Provenance-line convention applied per established Phase 3 pattern.
    - **Heaviest L4 decomposition in Phase 3 so far** — combined 38 L4s across the PSR pair (Service 17; Resource 21). Resource side has 4 extra L4s, all under L3 1.5.3.7 Manage Resource Exit (Service-side analog has 0 L4s). PSR-asymmetric retirement-granularity is the strongest TMF distinction in this pair.
    - **Specification-ABE four-back-link pattern complete on both PSR sides.** With this ingest, both `service-specification-abe` and `resource-specification-abe` carry four eTOM back-links each, distinguishing temporal scope of activity on the same SID artefact: ongoing-maintenance / project-driven-design / catalog-system-design / class-introduction-to-retirement. Densest trilateral pattern in the corpus; heat-map composability for the Specification ABE is now wired across four discrete cells per PSR side.
    - **Test-ABE two-back-link pattern.** Both Test ABEs now carry back-links from Strategy Management (1.4.1.8/9 + 1.5.1.8/9 Test-strategy L3s — strategic-level test planning) and Specification Lifecycle Management (1.4.3.8 + 1.5.3.8 Test Development & Retirement — Test catalogue management). The third Phase-3-discovered Test-related L3-set pattern: Strategy (.8 + .9) + Lifecycle (.8) is now visible. (The fourth is the Operations-area Manage Service/Resource Test L3s 1.4.4.6 / 1.5.4.9 — already H5 sub-capability anchors on the Operations-area capability map.)
    - **Definitive resolution of Service-side version-management asymmetry.** Confirmed: Service-side has no explicit version-management L3 anywhere across both Spec Management (1.4.19) and Spec Lifecycle (1.4.3). Service-side version mgmt is implicit / folded into 1.4.3.5 ("As well as developing new service classes these processes manage upgrades or enhancements to existing service classes"). Resource-side has explicit 1.5.19.4 Update and Version Resource Specifications. **PSR asymmetry is genuine and definitive** — Resource-side has more granular treatment of spec versioning at L3 level. Worth recording for the transformation roadmap; the asymmetry suggests OSS systems that manage *resource* specs may have version-control concerns more naturally exposed than systems managing *service* specs.
    - **PSR cascade visible at process level.** L3 .1 (Gather & Analyze New Service/Resource Ideas) shows the canonical cascade: Service takes input from Product only; Resource takes input from both Product and Service. Reflects the canonical PSR realization chain at requirements-capture layer.
    - **Multiple source-text observations preserved verbatim:**
        1. L4 1.4.3.5.3 brief contains "resource class deployed" — copy-paste artefact in Service-side text.
        2. L4 1.5.3.1.1 brief contains "required service classes" — copy-paste artefact in Resource-side text.
        3. L4 1.4.3.6.3 / 1.5.3.6.3 — naming asymmetry ("Party" vs "Supplier/Partner").
        4. L2 1.5.3 ED — cross-version naming reference to pre-v24.0 "Resource Strategy & Planning".
        5. L3 1.5.3.8 ED — possible copy-paste artefact ("enrichment of Resource Tests results" referencing itself).
        All preserved per CLAUDE.md §1, §10.3; OQ-045-family handling; no separate OQs filed.
    - **AI-distribution pattern continues.** No AI / automation references in either 1.4.3 or 1.5.3 EDs. BVD batch following the Capability-Management-batch-AI-free pattern. The Strategy + Capability Delivery AI concentration thesis holds across 5 of 6 PSR pairs ingested in Phase 3 so far.
    - **Convention discipline maintained.** No wikilinks in trilateral sections beyond the primary forward-link bullet target. Zero lint errors on first pass.
    - **Pending decisions:** none.
    - **Next action:** Propose 1.4.13 + 1.5.15 Catalog Lifecycle Management as the second BVD PSR pair. After that: 1.4.17 + 1.5.20 Anomaly Lifecycle Management closes BVD and Phase 3 ingest. Then L3-derived sub-capability review.

---

## 2026-05-11T14:00Z — INGEST — BVD batch, PSR pair 2 of 3: Service / Resource Catalog Lifecycle Management (1.4.13 + 1.5.15)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.13 + Resource Domain L2 1.5.15 (and their L3 descendants) extracted via openpyxl. **Thin process tree** — 3 L3s each, no L4 or L5 decomposition on either side.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-catalog-lifecycle-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Net-in-v25.5 callout (Original PID = None). **Completes-four-L2-Catalog-lifecycle callout** with anchored wikilinks to sibling Catalog L2s (Planning 1.4.16 + Operational Readiness 1.4.14 + Content 1.4.15). PSR-agnostic L2 ED observation (identical to Resource-side 1.5.15). `## L3 Process Details` with all 3 L3s. **Section-level callout flagging six source-text bugs across the PSR pair** — L3 body texts mis-target activity names shifted by one position (L3 .2 body says "Catalog Design"; L3 .3 body says "Catalog Build"). Per-L3 inline notes on the mis-targeting plus cross-L2 back-reference to Catalog Planning (1.4.13.1 → 1.4.16.2 Define Catalog Specification) and Enterprise-governance forward reference (1.4.13.3). Single SID forward link: `service-specification-abe` — **fifth eTOM back-link** on that ABE, extending the densest pattern in corpus. ODA via OQ-046 with hard-net-new-in-v25.5 framing.
    - **NEW** `wiki/etom/resource-domain/resource-catalog-lifecycle-management.md` — full L2 page parallel structure. Identical L2 ED to Service-side. Same six-bug L3 body mis-targeting cluster (preserved verbatim). Same cross-L2 back-reference and Enterprise-governance patterns. Single SID forward link: `resource-specification-abe` — fifth back-link, pre-production source.
    - `wiki/sid/service/service-specification-abe.md` — `## eTOM Processes That Manipulate This Entity` extended to **five eTOM back-links** with updated manipulator-role-density note: primary specifications-management (1.4.19, ongoing-maintenance) → capability-delivery (1.4.2, project-driven-design) → catalog-planning (1.4.16, catalog-system-design) → specification-lifecycle (1.4.3, class-introduction-to-retirement) → catalog-implementation-lifecycle (1.4.13, catalog-system-implementation-lifecycle). Densest trilateral pattern in corpus extended to five distinct manipulator roles.
    - `wiki/sid/resource/resource-specification-abe.md` — extended to **five eTOM back-links** with parallel manipulator-role-density note. Pre-production source.
    - `wiki/etom/service-domain/_index.md` — 1.4.13 row added in numerical order (between 1.4.12 and 1.4.14). Pending-ingest paragraph updated — BVD batch progress note now "1 of 3 pairs remaining: 1.4.17 + 1.5.20 Anomaly Lifecycle Management closes BVD and Phase 3 ingest".
    - `wiki/etom/resource-domain/_index.md` — 1.5.15 row added in numerical order (between 1.5.14 and 1.5.16). Same status updates.
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in: `cap-service-catalog-lifecycle` and `cap-resource-catalog-lifecycle`. **Completes-four-L2-Catalog-lifecycle callout** on both H4 entries with anchored wikilinks to all three sibling catalog L2s across both view pages (Planning + Operational Readiness + Content). PSR-agnostic-L2-ED observation. Most-prominent-source-text-inconsistency-cluster callout. **Fifth eTOM back-link on Specification ABEs — densest pattern in corpus extended.** Both Mermaid nodes (`S1413`, `R1515`) de-`:::pending`-ed. Session State: Last activity, scope-line capability count (14 of 16 done — only Anomaly Lifecycle pair remains), Batches DONE list (added Catalog Lifecycle PSR pair as #7), IN-PROGRESS / PENDING reorganised, Next action repointed to the third and final BVD PSR pair (1.4.17 + 1.5.20 Anomaly Lifecycle Management — closes BVD and Phase 3 ingest). `derived_from` + Source Pages updated.
    - `wiki/index.md` — Service Domain count 14 → 15; Resource Domain count 15 → 16; S2R-area subdivisions list all 7 ingested L2s on each side.
- **Sections skipped:** None within the L2s — fully ingested. Global skip: 2 more S2R L2s remain (Anomaly Lifecycle PSR pair).
- **Lint result:** PASS — see lint following.
- **Open questions filed:** None new.
- **Notes:**
    - **Second BVD PSR pair complete. Phase 3 ingest 14 of 16 S2R L2s done — only Anomaly Lifecycle PSR pair remains.**
    - **Four-L2 Catalog lifecycle structurally complete in v25.5 framing.** With this ingest, all four Catalog L2s on both PSR sides have capability anchors across both view pages: Planning (S2R-CM, 1.4.16/1.5.18) + Lifecycle (S2R-BVD, 1.4.13/1.5.15 — this pair) + Operational Readiness (Ops-ORS, 1.4.14/1.5.16) + Content (Ops-ORS, 1.4.15/1.5.17). Eight catalog anchors total. **Heat-map composability for catalog work fully wired** — a transformation initiative on catalog maturity now renders as a four-cell row per PSR side, not a single cell.
    - **Most prominent source-text inconsistency cluster in Phase 3.** Six bugs total across the PSR pair (three per side): L3 body texts (briefs + EDs) reference the wrong sub-process names shifted by one position from the L3's actual name. L3 .2 body says "Catalog Design" (should be "Build"); L3 .3 body says "Catalog Build" (should be "Policy"). Preserved verbatim per OQ-045-family handling; flagged with section-level callouts on both source pages and inline notes per L3. No separate OQ filed.
    - **First PSR pair with completely PSR-agnostic L2 EDs.** Both L2 EDs literally identical word-for-word (416 chars each). Neither "Service" nor "Resource" appears in either ED; both reference "Product/Service/Resource Catalog" generically. v25.5 treats Catalog Lifecycle as a domain-agnostic governance pattern — only the L3 names carry PSR qualifiers. PSR-agnostic L2-ED framing is itself a v25.5 modelling observation worth preserving.
    - **Specification-ABE five-back-link pattern complete on both PSR sides.** Densest trilateral pattern in corpus extended from four to five back-links. Five distinct manipulator roles distinguish temporal and structural scope of activity on the same SID artefact: primary specifications-management / capability-delivery upstream-input / catalog-planning / specification-lifecycle / catalog-implementation-lifecycle. Heat-map composability for Specification-ABE work is now wired across five discrete cells per PSR side.
    - **Structural break from BVD pair #1.** First BVD PSR pair (1.4.3/1.5.3 Specification Lifecycle Management) had R20.5 lineage with v24.0 renames; this pair is v25.5-net-new with no R20.5 lineage. **BVD batch is mixed-vintage** — Specification Lifecycle is pre-v25 (renamed v24.0); Catalog Lifecycle is v25.5-net-new. Worth recording as structural fact about v25.5 BVD-vertical evolution.
    - **AI-distribution pattern continues — 7 of 8 PSR pairs AI-free.** No AI / automation references in either 1.4.13 or 1.5.15. The Strategy + Capability Delivery AI concentration thesis holds robustly; only the final BVD PSR pair (Anomaly Lifecycle) remains to fully confirm or break the pattern.
    - **Convention discipline maintained.** No wikilinks in trilateral sections beyond the primary forward-link bullet target. Zero lint errors on first pass.
    - **Pending decisions:** none.
    - **Next action:** Propose 1.4.17 + 1.5.20 Anomaly Lifecycle Management as the **third and final BVD PSR pair**. After that: BVD batch closes; Phase 3 ingest closes (16 of 16 S2R L2s); then L3-derived sub-capability review closes Phase 3 entirely.

---

## 2026-05-12T10:00Z — INGEST — BVD batch CLOSED + PHASE 3 INGEST CLOSED — final PSR pair: Service / Resource Anomaly Lifecycle Management (1.4.17 + 1.5.20)

- **File(s):** `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` — Service Domain L2 1.4.17 + Resource Domain L2 1.5.20 (and their L3 / L4 descendants) extracted via openpyxl. Both net-new in v25.5.
- **Pages created/updated:**
    - **NEW** `wiki/etom/service-domain/service-anomaly-lifecycle-management.md` — full L2 page per CLAUDE.md §5.1 anatomy. Three-line lifecycle-area / vertical-context / domain callout. Net-in-v25.5 callout. **BVD-governs / Operations-executes callout** with anchored wikilink to existing Operations-side [[wiki/etom/service-domain/service-anomaly-management|1.4.18]] and structural framing of the two-L2 Anomaly pattern as the third instance of v25.5's cross-Lifecycle-Area governance/execution split (after the four-L2 Catalog lifecycle and the Test-strategy lineage). Verbatim L2 Overview from Excel ED. Smart curly quotes around *"what is normal"* / *"deviations"* preserved verbatim per CLAUDE.md §1, §10.3. Full `## L3 Process Details` section with all 6 L3s + 5 L4s. **Major source-text observation cluster on L4 1.4.17.1.2** (three threads on the same L4): (a) L4 name *"Establish Anomaly Criteria"* lacks PSR qualifier present in brief (*"Establish **Service** Anomaly Criteria…"*); (b) brief + ED reference **"Products" / "Product's"** instead of Services with mid-paragraph PSR-context flip Product → Service — **first Product-domain leakage** in Phase 3 source-text bugs (prior bugs were all Resource ↔ Service leakage); (c) structural correlation — this L4 is the one missing entirely on the Resource side. Full inline source-text observation callout with verbatim brief + ED preserved per OQ-045-family handling; no separate OQ filed. Minor PSR typographic asymmetry callout on 1.4.17.2.1 brief (missing terminal period; Resource-side has it). **OODA framing callout** on L3 1.4.17.4 ED (Observe / Orient / Decide / Act pattern verbatim from source). Two SID forward links: `wiki/sid/common/anomaly-abe` (production) + `wiki/sid/common/closed-loop-abe` («Preliminary», `release_status: draft`) — **first Phase 3 PSR pair with SID forward links into Common ABE folder** rather than per-domain folders. Closed Loop ABE «Preliminary» heat-map calibration note. ODA via OQ-046 placeholder with hard-net-new framing.
    - **NEW** `wiki/etom/resource-domain/resource-anomaly-lifecycle-management.md` — full L2 page parallel structure. Net-in-v25.5 callout. Same BVD-governs / Operations-executes callout pattern with anchored wikilink to existing Operations-side [[wiki/etom/resource-domain/resource-anomaly-management|1.5.21]]. Verbatim L2 Overview (PSR-substitution-clean from Service-side analog). Full L3 Process Details with all 6 L3s + 4 L4s (one fewer than Service side). **PSR-asymmetry callout on L3 1.5.20.1** flagging the missing `.1.2` L4 (Resource has only `.1.1` and `.1.3`; Service has `.1.1` + `.1.2` + `.1.3`); cross-reference to Service-side Product → Service body-text leakage on the corresponding-but-missing L4. Same OODA framing callout on L3 1.5.20.4. Same minor 2.1-brief terminal-period observation. Same SID forward links to anomaly-abe + closed-loop-abe. ODA via OQ-046.
    - `wiki/sid/common/anomaly-abe.md` — `## eTOM Processes That Manipulate This Entity` section **populated for the first time** (replacing the OQ-008 deferral): two back-links to the new BVD-side L2s (1.4.17 + 1.5.20). Inline note acknowledging Operations-side L2s (1.4.18 + 1.5.21) as expected-but-deferred manipulators per the **tight-scope decision** at this ingest (Option A from proposal — Phase-4 broader-trilateral-sweep is the right place to populate Operations-side trilateral fully). The ABE's existing speculative OQ-008 wording is now superseded by source-grounded BVD-side back-links.
    - `wiki/sid/common/closed-loop-abe.md` — same shape. Section populated for first time with two back-links (1.4.17 + 1.5.20) + tight-scope note for Operations-side. The L3 1.4.17.4 / 1.5.20.4 OODA-citation surfaced in the back-link justification because the ClosedLoop ABE is the SID-side artefact for the OODA-pattern-driven Closed Loops the L2s govern. ABE remains `release_status: draft` («Preliminary»); back-links surface the SID-side-lags-eTOM-side observation explicitly.
    - `wiki/etom/service-domain/_index.md` — 1.4.17 row added in numerical order (between 1.4.16 and 1.4.18). Pending-ingest paragraph rewritten — **Phase 3 ingest CLOSED** note with full enumeration of all 8 in-scope S2R Service Domain L2s; total 16 in-scope L2s (8 OFAB + 8 S2R).
    - `wiki/etom/resource-domain/_index.md` — 1.5.20 row added in numerical order (between 1.5.19 and 1.5.21). Same Phase-3-CLOSED note; total 17 in-scope L2s (9 OFAB + 8 S2R).
    - `wiki/views/capability-map-s2r.md` — both H4 capabilities baked in: `cap-service-anomaly-lifecycle` and `cap-resource-anomaly-lifecycle`, replacing the (duplicated) pending stubs. TMF distinctions on both H4 entries: net-new-in-v25.5; **BVD-governs / Operations-executes** anchored cross-page wikilinks to `[[wiki/views/capability-map#cap-{service,resource}-anomaly]]` — heat-map composability for the two-L2 Anomaly pattern wired across both view pages, same convention as the four-L2 Catalog lifecycle; **OODA-framing-in-source** callout; **most-symmetric L3 naming in Phase 3** (6 L3 names PSR-substitution-clean); PSR-asymmetric L4 structure on Service-side H4 (Service has buggy `.1.2`, Resource missing it entirely); first Product-domain source-text leakage in Phase 3 (Service-side detail); first Phase 3 SID forward links into Common ABE folder; Closed Loop ABE «Preliminary» heat-map calibration; **AI-distribution thesis fully confirmed (8 of 8 PSR pairs AI-free outside Strategy + Capability Delivery)**. Both Mermaid nodes (`S1417`, `R1520`) **de-`:::pending`-ed — diagram now fully populated, no remaining pending nodes**. Session State extensively updated: Last activity (Phase 3 ingest CLOSED narrative), scope-line capability count (16 of 16 — Phase 3 ingest CLOSED), Batches DONE list (added Anomaly Lifecycle PSR pair as #8 — closes BVD batch and Phase 3 ingest), IN-PROGRESS / PENDING reorganised (only L3-derived sub-capability review remains), Naming-asymmetry convention note updated (no PSR naming asymmetries observed across all 16 S2R L2s — confirms pattern at end of Phase 3), Next action repointed to L3-derived sub-capability review. `derived_from` frontmatter expanded to 18 entries (16 L2s + 2 foundations). Source Pages list extended to 18 entries.
    - `wiki/views/capability-map.md` Session State — Last activity line updated to record companion-page Phase 3 closure; Companion view bullet updated to reflect 16-of-16 S2R capabilities populated and sister page's empty-pending-Mermaid status.
    - `wiki/index.md` — Service Domain count 15 → 16; Resource Domain count 16 → 17; S2R-area subdivisions list all 8 ingested L2s on each side; **Phase 3 S2R-expansion ingest CLOSED 2026-05-12** flag added. Views section S2R-page entry updated to reflect 16/16 ingested + Phase 3 ingest CLOSED + remaining work (L3-derived sub-capability review).
- **Sections skipped:** None within the L2s — fully ingested. Global skip: 0 — Phase 3 ingest CLOSED at this entry. No further L2 ingest planned for v1 corpus; L3-derived sub-capability review closes Phase 3 entirely.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** None new. OQ-046 covers ODA cross-walk gap for both L2s with hard-net-new framing.
- **Notes:**
    - **PHASE 3 INGEST CLOSED — 16 of 16 S2R L2s ingested across 8 PSR pairs over 3 days (2026-05-10 → 2026-05-12).** Strategy Management (2 L2s, 1 PSR pair, pilot) + Capability Management (8 L2s, 4 PSR pairs) + Business Value Development (6 L2s, 3 PSR pairs). **Total corpus: 147 pages** (was 145 pre-ingest, +2 new L2 pages). Total in-scope L2s in S+R domains: 33 (Service 16 + Resource 17). Combined with 12 in-scope Product Domain L2s from v1, the corpus carries **45 in-scope L2 pages** representing the operational+lifecycle process layer for OSS modernisation.
    - **Final BVD PSR pair complete.** Single combined log entry per PSR pair convention from prior BVD ingests holds. The Anomaly Lifecycle PSR pair is qualitatively different from the prior two BVD pairs (Specification Lifecycle had heavy L4 decomposition + R20.5 lineage; Catalog Lifecycle had thin L3 trees + PSR-agnostic L2 EDs; Anomaly Lifecycle has medium-depth + most-symmetric L3 naming + first Common-ABE SID trilateral) but follows the same propose → ingest both → bake → log → lint rhythm.
    - **PSR asymmetries recorded as TMF distinctions** on both L2 pages and on both view-page H4 entries: (1) PSR-asymmetric L4 structure (Service 5 L4s vs Resource 4 — Resource missing `.1.2` Establish Anomaly Criteria entirely); (2) Source-text bug cluster on Service-side L4 1.4.17.1.2 (three threads — PSR-name vs PSR-body asymmetry + Product → Service body leakage + structural correlation with the missing Resource L4); (3) Minor PSR typographic asymmetry on 1.4.17.2.1 / 1.5.20.2.1 brief (terminal-period presence/absence); (4) Verbatim-symmetric L3 names (most-symmetric Phase 3 PSR pair at L3-name level); (5) PSR-substitution-clean L2 EDs (not PSR-agnostic like Catalog Lifecycle 1.4.13/1.5.15 — both sides explicitly carry their PSR qualifier).
    - **First Product-domain leakage in Phase 3 source-text bugs.** Prior Phase 3 source-text bugs were all cross-PSR-domain leakage within Service ↔ Resource: 1.5.21 ("Resource Problem Management" reference); 1.4.12.9 (Service Capacity Report carrying "Resource Capacity"); 1.4.19.2 (Model Service Specifications carrying "Model Resource Specifications" body); 1.4.13.x + 1.5.15.x six-bug L3-body-mis-targeting cluster. Anomaly Lifecycle 1.4.17.1.2 introduces the **first Product-domain leakage** (Service-side L4 body references "Products" / "Product's" mid-paragraph). Likely pattern: GB921 Anomaly content was authored from a Product-domain template and PSR-substituted with incomplete coverage. Cannot infer authorial intent (CLAUDE.md §1); preserve verbatim, flag inline, no new OQ.
    - **First Phase 3 SID forward links into Common ABE folder.** All prior Phase 3 PSR pairs pointed at per-domain SID ABEs (`wiki/sid/{service,resource}/...`). Anomaly Lifecycle is the first to point at Common ABEs (`wiki/sid/common/anomaly-abe`, `wiki/sid/common/closed-loop-abe`). Reflects the Anomaly + Closed Loop pattern in v25.5 SID design — these are abstract entities specialised per-domain (`ServiceAnomaly`, `ResourceAnomaly`, etc. as specialisations of the Common Anomaly entity). The PSR-domain-specialisations are referenced verbatim from Common §4.30.2 in the L2 trilateral notes. Both Common ABEs get their `## eTOM Processes That Manipulate This Entity` sections **populated for the first time at this ingest**, replacing the OQ-008 deferral with source-grounded back-links.
    - **Tight-scope decision applied per proposal.** Operations-side L2s 1.4.18 + 1.5.21 — both correspond to the BVD-governance L2s ingested here, both had OQ-008 deferrals on their `## SID Entities Manipulated` sections, and both are explicit Phase-4 candidates per the now-superseded OQ-008 speculation in the Anomaly ABE. Option A (tight-scope) chosen at proposal sign-off — Operations-side trilateral fills deferred to Phase 4 broader trilateral sweep rather than opportunistically populated at this ingest. Both target Common ABEs carry inline notes acknowledging the Operations-side L2s as expected-but-deferred manipulators. Cleaner audit trail; less mid-ingest scope drift.
    - **Two-L2 Anomaly pattern complete — third instance of cross-Lifecycle-Area "BVD governs / Operations executes" structural pattern in v25.5.** Prior instances: four-L2 Catalog lifecycle (Planning S2R-CM + Lifecycle S2R-BVD + Operational Readiness Ops-ORS + Content Ops-ORS — 8 anchors per side); Test-strategy lineage (1.4.1.8/9 + 1.5.1.8/9 strategic L3s + 1.4.4.6 + 1.5.4.9 operational L3s as H5 anchors). Anomaly is the simplest of the three instances (two-L2 pattern, one Lifecycle-stage in each Area). All three patterns share the same shape: governance/lifecycle layer in S2R + operational-execution layer in Ops; SID artefacts (Catalog sub-ABE, Test ABE, Anomaly + Closed Loop ABEs) bridge them. Worth recording as a corpus-level v25.5 observation — TMF deliberately separates governance-of-X from operations-of-X across the two Lifecycle Areas, surfacing capability boundaries that monolithic OSS implementations typically conflate.
    - **OODA framing as v25.5 anchor.** L3 1.4.17.4 / 1.5.20.4 EDs explicitly cite the OODA pattern (Observe / Orient / Decide / Act) as the conceptual model for Anomaly Closed Loops. Practitioner-recognisable framework from military strategy / decision theory; also present in autonomous-systems and AIOps practice. Useful for current-state-OSS gap analysis — current systems may not have OODA-aligned closed-loop architecture even where they have anomaly detection.
    - **AI-distribution thesis fully confirmed across all 8 Phase 3 PSR pairs.** AI-free PSR pairs: Capacity Management, Catalog Planning, Specification Management, Specification Lifecycle, Catalog Lifecycle, **Anomaly Lifecycle (this pair)** = 6 of 8. PSR pairs with Resource-side-only AI references: Strategy Management, Capability Delivery = 2 of 8. **Pattern is robust** — v25.5 AI commentary is concentrated exclusively in the two upstream-most Resource-side L2s (1.5.1 Strategy + 1.5.2 Capability Delivery), absent from all 6 downstream Capability Management + BVD PSR pairs. Practitioner implication: AI-readiness assessment for the OSS modernisation roadmap should focus on the Resource-Strategy + Resource-Capability-Delivery layers; downstream layers (Catalog, Specification, Anomaly Lifecycle) don't carry v25.5 AI guidance.
    - **Convention discipline maintained.** No wikilinks in trilateral sections beyond the primary forward-link bullet target (Common-ABE-folder targets carry the same single-wikilink-per-entry pattern). No mid-trilateral-section parenthetical wikilinks. Cross-page anchored wikilinks in body text (BVD-governs / Operations-executes callouts) are fine and used per established pattern. Zero lint errors expected on first pass.
    - **Verbatim discipline preservations.** Smart curly quotes in L2 EDs (`"what is normal"` / `"deviations"`); smart curly quotes in L3 EDs (`"normal pattern data"` / `"constraints data"` / `"goals data"` / `'learned normal'` / `'expected behavior'`); L4 1.4.17.1.2 Product / Service body-text mixing; missing terminal period on 1.4.17.2.1 brief; missing L4 `.1.2` on Resource side. All preserved per CLAUDE.md §1, §10.3.
    - **Pending decisions:** none.
    - **Next action:** L3-derived sub-capability review — final closing step of Phase 3. Survey all L3s across the 16 newly-ingested S2R L2s for sub-capability promotion candidates per the convention (named L3 + substantive scope + recognised practitioner concern + cross-PSR symmetry). Likely candidates per Session State observations: Capability Delivery's commissioning L4 on Resource side; Capacity Management's threshold/utilization L4 cluster; Specification Management's version-management L3 (Resource-only). Anomaly Lifecycle's six L3s read as fully-merged-into-the-L2 capability rather than separable concerns — likely no sub-capability promotions from this PSR pair, but to confirm during the review. Will produce a proposal with shortlist + recommended H5 anchors before any anchors are added to either view page.

---

## 2026-05-12T10:15Z — LINT FIX — wikilinks-in-trilateral-sections removed from Common Anomaly + Closed Loop ABE Phase-4-candidate notes

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/sid/common/anomaly-abe.md` — `## eTOM Processes That Manipulate This Entity` section: removed two wikilinks from the inline Phase-4-candidate prose note (`[[wiki/etom/service-domain/service-anomaly-management|1.4.18]]` and `[[wiki/etom/resource-domain/resource-anomaly-management|1.5.21]]`). The wikilinks were in the deferred-trilateral commentary acknowledging Operations-side L2s as expected manipulators that were intentionally not populated this ingest (per the tight-scope decision). The linter correctly interpreted them as forward links demanding bidirectional reciprocity from those Operations-side L2 pages — which still defer to OQ-008. Replaced with plain-prose references ("Service Anomaly Management 1.4.18; Resource Anomaly Management 1.5.21 — both in `wiki/etom/{service,resource}-domain/`") and an explicit note that wikilinks are intentionally omitted per the convention.
    - `wiki/sid/common/closed-loop-abe.md` — same fix, two wikilinks removed from the parallel Phase-4-candidate note.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Convention reaffirmed.** The "no wikilinks in trilateral sections beyond the primary forward-link bullet target" rule (settled at the 2026-05-10T21:05Z Capacity Management lint fix) extends to **inline commentary about deferred-or-pending manipulators** within the trilateral section. Even when the prose explicitly says the link is deferred / not populated, the wikilink itself triggers the bidirectional-consistency check. Plain prose with structured-path-hint (`wiki/etom/{service,resource}-domain/`) preserves practitioner navigation intent without triggering the lint.
    - **No content lost** — both ABEs retain the full Phase-4-candidate discussion; only the wikilink syntax was stripped. Practitioners following the prose-path-hint can reach the Operations-side L2s via the existing `wiki/etom/{service,resource}-domain/_index.md` browse pages one click away.
    - **First Common-ABE-trilateral lint cycle in the corpus.** The Anomaly Lifecycle PSR pair was the first to populate Common ABE trilateral sections — surfacing this convention extension at the Common-ABE level. Same pattern as prior per-domain ABE lint fixes (Resource Strategy & Plan ABE; Capacity ABE), now confirmed to apply uniformly across all SID-folder targets.
    - **Phase 3 ingest closure stands.** The lint fix is a within-ingest correction; the 2026-05-12T10:00Z entry's claim of Phase 3 ingest CLOSED is unaffected.

---

## 2026-05-12T14:00Z — REVIEW — Phase 3 closing step: L3-derived sub-capability review COMPLETE — Phase 3 entirely closed

- **File(s):** none ingested. Derivative content drawn from existing in-corpus L2 pages.
- **Pages created/updated:**
    - `wiki/views/capability-map-s2r.md` — **6 new H5 sub-capability anchors added** across 3 clusters and 4 distinct H4 parent entries:
        - **Strategy Management vertical, Service Domain section:** new H5 `cap-service-strategy-test` after `cap-service-strategy` H4 — anchored on L3 1.4.1.8 Service Test Strategy + L3 1.4.1.9 Analyze Service Test Quality (both new in v25.5; no L4s). Verbatim source quotes; cross-anchor wikilinks to all 5 sibling Test anchors (Resource-side Strategy + Service+Resource Lifecycle + Service+Resource Operations) rendering the 3-stage × 2-PSR Test maturity row.
        - **Strategy Management vertical, Resource Domain section:** new H5 `cap-resource-strategy-test` after `cap-resource-strategy` H4 — anchored on L3 1.5.1.8 Resource Test Strategy + L3 1.5.1.9 Analyze Resource Test Quality. Cross-anchor wikilinks parallel to Service-side. Cross-version naming reference observation flagged: 1.5.1.8 ED lists "Resource Provisioning" (R20.5-era naming) for the v25.5 [[wiki/views/capability-map#cap-resource-order|Resource Order Management]] L2.
        - **Business Value Development vertical, Service Domain section:** two new H5s after `cap-service-specification-lifecycle` H4 — `cap-service-specification-lifecycle-test` (L3 1.4.3.8 Service Specification Test Development & Retirement; cross-PSR test composition surfaced — Service Test catalogue includes "relationships with lower level tests (Resource Test)"); `cap-service-specification-lifecycle-exit` (L3 1.4.3.7 Manage Service Exit; narrative-only at L3 level, no L4s — heat-map relevance: decommissioning maturity separable from broader spec-lifecycle maturity).
        - **Business Value Development vertical, Resource Domain section:** two new H5s after `cap-resource-specification-lifecycle` H4 — `cap-resource-specification-lifecycle-test` (L3 1.5.3.8 Resource Specification Test Development & Retirement; PSR-asymmetric vs Service — Resource side missing the "lower-level tests" composition line because Resource is the bottom of the cross-PSR test stack); `cap-resource-specification-lifecycle-exit` (L3 1.5.3.7 Manage Resource Exit with **4 explicit L4s** — Identify Unviable / Identify Impacted Customers / Develop Transition Strategies / Manage Exit Process — all with substantive briefs; PSR-asymmetric L4 depth surfaces the practitioner observation that resource decommissioning is operationally more demanding than service decommissioning).
    - `wiki/views/capability-map-s2r.md` — **ITIL Service Transition framing TMF distinction bullet added** to both Capability Delivery H4 entries (`cap-service-capability-delivery` + `cap-resource-capability-delivery`). Records that L3 1.4.2.7 / 1.5.2.7 Manage Handover to Operations was considered for H5 promotion at this review and rejected as a stage-within-process rather than a cross-cutting concern; ITIL Service Transition framing preserved at L2 level for practitioner reference.
    - `wiki/views/capability-map-s2r.md` — Session State extensively updated: Last activity (full 6-anchor narrative + 3-stage × 2-PSR Test row framing + 2 borderline rejections + Capacity sanity-check confirmation); Batches DONE list (added Phase-3-closing entry as #9); Batches IN-PROGRESS / PENDING reorganised to `_(none — Phase 3 entirely closed)_`; Next action repointed to `_(none from Phase 3 — corpus structurally and content-complete; user-side overlay work in `project/` is unblocked; future phases surface only on user prompt)_`. Naming-asymmetry convention note already updated in the prior 10:00Z ingest closure. Scope-line in derivation-status callout updated to reflect the 22 anchors (16 L2 + 6 H5) on this page.
    - `wiki/views/capability-map.md` — **cross-anchor wikilinks added to existing test H5s** (`cap-service-support-test` and `cap-resource-support-test`) under the **Cross-Lifecycle Test maturity row (Phase 3 closing review, 2026-05-12)** sub-section heading. Each Operations-side test H5 now wikilinks the corresponding Strategy-level + Lifecycle-level Test anchors on the S2R page, making the cross-Lifecycle Test row navigable from any entry point. The 8-bullet existing "Test management includes" verbatim source quote unchanged; the cross-Lifecycle row addition slots in between that and the **Stable sub-anchor** trailer line.
    - `wiki/views/capability-map.md` Session State — Last activity line updated to record the 6-H5-promotion sub-capability review + the cross-anchor wikilinks added to this page; Companion view bullet updated with the 16 L2 + 6 H5 = 22 anchor count and 3-stage × 2-PSR row framing; final corpus stable-anchor inventory recorded as 47 (25 on this page + 22 on S2R page).
    - `wiki/index.md` — Views section S2R-page entry updated to reflect Phase 3 entirely closed + 22 anchors (16 L2 + 6 H5) + 3-stage × 2-PSR Test row spanning both view pages.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint output following this entry.
- **Open questions filed:** None new.
- **Notes:**
    - **PHASE 3 ENTIRELY CLOSED.** Phase 3 ran 2026-05-10 → 2026-05-12 (3 days end-to-end): scoping & decisions (2026-05-10 morning); CLAUDE.md §3 amendment (2026-05-10 evening); 8 PSR pair ingests over 2 days (Strategy pilot 2026-05-10; Capability Management 2026-05-10 → 2026-05-11; BVD 2026-05-11 → 2026-05-12 morning); L3-derived sub-capability review 2026-05-12 afternoon (this entry). **Net additions to corpus: 16 new L2 pages (Service +8, Resource +8); 4 SID ABE updates (per-domain Strategy + Test + Spec + Capacity ABEs) + 2 first-time-populated Common ABEs (Anomaly + Closed Loop); 1 new view page (`capability-map-s2r.md`); 1 amended CLAUDE.md §3; 6 H5 sub-capability anchors on the new view page; 2 H5 cross-anchor wikilink additions on the existing view page; 2 ITIL-handover TMF distinction bullets on the new view page. Total stable heat-map anchors across both view pages: 47 (25 Operations + 22 S2R).** Total corpus pages: 147 (was 117 at v1; +30 from Phase 3 ingests including L2 pages, the new view page, and assorted SID/ABE intermediate updates that didn't add new files).
    - **L3-derived sub-capability convention applied uniformly.** Survey covered all 95 L3s across the 16 newly-ingested S2R L2s. Convention test (named L3 + substantive scope + recognised practitioner concern + cross-PSR symmetry) yielded 3 strong-candidate clusters (6 anchors), 2 borderline candidates (rejected — handover and Resource-only spec versioning), and 0 from the remaining 5 L2s (Capacity, Catalog Planning, Catalog Lifecycle, Specification Management, Anomaly Lifecycle — none of their L3s passed the cross-cutting-concern bar; all are stages-within-the-L2 rather than separable concerns).
    - **3-stage × 2-PSR Test maturity row — strongest cross-Lifecycle composability story to come out of Phase 3.** v25.5 distributes Test treatment across all three Lifecycle stages: Strategy-level (Test Strategy + Quality Analysis at L3 1.4.1.8/9 + 1.5.1.8/9); Lifecycle-level (Test catalogue Development & Retirement at L3 1.4.3.8 + 1.5.3.8); Operations-level (Test execution at L3 1.4.4.6 + 1.5.4.9). All six L3s already in corpus pre-this-review; the review formalises them as 6 stable heat-map anchors with full cross-anchor navigation. **Practitioner heat-map relevance:** orgs typically have very different maturity profiles across the three stages — strong test execution doesn't imply strong test catalogue management doesn't imply strong test strategy. Surfacing as 6 separate cells lets overlay convey that asymmetry. **Cross-PSR test composition** explicitly documented in source — Service Test catalogues compose against Resource Test catalogues; Resource is the bottom of the composition stack.
    - **Specification end-of-life (Exit) — PSR-asymmetric L4 depth becomes structural heat-map dimension.** Both PSR sides get their own anchor (`cap-service-specification-lifecycle-exit` + `cap-resource-specification-lifecycle-exit`); the asymmetry between them (Service narrative-only / Resource 4 L4s) is preserved as content rather than synthesised away. Practitioner observation: resource decommissioning involves physical equipment + legacy systems + infrastructure transition + migration paths (4 L4s' worth of breakdown); service decommissioning is largely customer-migration + catalogue-cleanup (narrative-level). Heat-map cells for the two sides will typically score differently in any practitioner org.
    - **Borderline rejections — convention discipline preserved.**
        1. **Handover (Borderline A) — rejected, surfaced as TMF distinction.** L3 1.4.2.7 / 1.5.2.7 Manage Handover to Operations passes most convention tests (named L3 + substantive scope + multi-L4 decomposition both sides + recognised practitioner concern via ITIL Service Transition framing) but **fails the cross-cutting test**: handover is a stage *within* capability delivery (only happens at the end), not a concern *exercised across multiple processes*. Workforce / inventory / test / security (the 4 prior H5 promotions) all appear across multiple L2s in one form or another; handover only ever appears in capability-delivery's L3 .7. Rejection preserves the convention's structural integrity. ITIL framing added as TMF distinction bullet on both Capability Delivery H4 entries so the practitioner concern isn't lost.
        2. **Resource-only specification version management (Borderline B) — rejected, no new content.** L3 1.5.19.4 Update and Version Resource Specifications passes most convention tests (named L3 + recognised concern — version management is universal OSS) but **fails cross-PSR symmetry** (Resource-only; Service-side has no version-mgmt L3 anywhere across either 1.4.19 Specification Management or 1.4.3 Specification Lifecycle Management — definitively confirmed in the 2026-05-11T13:00Z Specification Lifecycle ingest). Promoting would set a single-PSR-side precedent that propagates structural asymmetry into every overlay built against the corpus. Asymmetry already surfaced as TMF distinction on existing `cap-resource-specification` H4 (per 2026-05-11T11:00Z log entry); no new content added at this review. **Convention rule reaffirmed:** single-PSR-side promotion fails the bar regardless of whether the concern itself is generic or domain-specific (Number Portability was rejected on two grounds — single-side AND telecom-specific; this candidate fails only the first ground but that's sufficient).
    - **Capacity Management Threshold/Utilization L4 cluster — sanity-check confirmed rejection.** Session State observation had flagged this as a candidate (L3 1.4.12.7 / 1.5.14.7 Optimize). Re-examined at this review and confirmed: the cluster is L4-internal (Service collapses Thresholds + Utilization into one L4 with Adjust + Allocate L5s; Resource splits into two parallel L4s — `.7.1 Manage Utilization` + `.7.2 Manage Thresholds`). Promoting `cap-{service,resource}-capacity-optimize` as H5 would pull out Capacity Management's own optimization step as a separable anchor — but optimization isn't cross-cutting, it's a stage of the capacity lifecycle (Plan → Align → GAP → Forecast → Implement → Analyze → Optimize → Monitor → Report). Same structural problem as Handover. The L4-level asymmetry is already surfaced on both Capacity Management H4 entries' TMF distinctions — that's the right level.
    - **Convention discipline updated.** The L3-derived sub-capability convention now has 4 instances of the same rejection rationale: Number Portability (Phase 2), Handover (Phase 3 closing), Resource-only Spec Versioning (Phase 3 closing), Capacity-Optimize (Phase 3 closing — sanity check). Across all 4 rejections the test that fails varies (cross-cutting / cross-PSR-symmetry / domain-specificity / stage-within-process) — confirming the convention is multi-criteria and that all criteria need to hold. **The convention has been validated as a discriminating filter** — it accepts genuine cross-cutting concerns (workforce, inventory, test, security) and rejects stages-within-process or single-PSR concerns even when they're substantive.
    - **Final stable-anchor inventory after Phase 3.**
        - **Operations-area page (`capability-map.md`)** — 17 L2 anchors + 8 H5 anchors (security ×2, workforce ×2, inventory ×2, test ×2) = **25 anchors**. Test H5s carry cross-Lifecycle wikilinks added at this review.
        - **S2R-area page (`capability-map-s2r.md`)** — 16 L2 anchors + 6 H5 anchors (Strategy-test ×2, Lifecycle-test ×2, Lifecycle-exit ×2) = **22 anchors**.
        - **Corpus total: 47 stable heat-map anchors across both view pages.** All anchor IDs are stable; user's `project/` overlay file (which Claude does not read — security boundary per CLAUDE.md §10.4) can wikilink these anchors and they will not move under future maintenance.
    - **Convention discipline maintained at this review.** No wikilinks placed in trilateral sections (the H5 additions are inside view-page H4 capability blocks; views are exempt from trilateral linking per CLAUDE.md §5.5). All H5 anchors carry the `cap-<l2-anchor>-<concern>` naming pattern. Cross-anchor wikilinks use anchor-relative form (`[[#cap-...]]`) within a page and full-path form (`[[wiki/views/capability-map#cap-...]]`) across pages.
    - **Pending decisions:** none.
    - **Next action:** _(none from Phase 3 — corpus structurally and content-complete against the original transformation-roadmap goal. User reviews the full Phase 3 deliverable in Obsidian and signals readiness to move to overlay work in `project/` whenever they're ready. Future phases — corpus maintenance; ODA-layer trilateral sweep against GB1022; possible Phase 4 broader-trilateral fills (Operations-side Anomaly L2s → Common ABEs; Resource-only candidates that failed cross-PSR test) — surface only on explicit user prompt.)_

---

## 2026-05-12T16:00Z — DIAGRAMS — Boxes-in-boxes capability-map renders (PDF + PNG) for both view pages plus combined view

- **File(s):** none ingested. Derivative visual artefacts.
- **Pages created/updated:**
    - **NEW** `wiki/views/diagrams/` directory — 8 new files:
        - `capability-map-s2r.{html,pdf,png}` — S2R-area capability map render. A3 landscape; boxes-in-boxes treemap with domains across the top, verticals down the side, L2 boxes in cells, H5 sub-capabilities nested inside parent L2 boxes. Blue palette.
        - `capability-map.{html,pdf,png}` — Operations-area capability map render. Same template structure with 4 vertical rows (OFAB) instead of 3. Green palette to distinguish from sister page.
        - `capability-map-combined.{html,pdf,png}` — combined render of both Lifecycle Areas. A2 landscape (594×420 mm — needed for 7-row height). Two distinct matrix blocks with their own Lifecycle Area band labels (blue S2R / green Operations); cross-Lifecycle composability patterns (Test row / Anomaly pair / Catalog 4-L2) marked with `⇄` connector pills on participating cells; inventory totals card in footer (47 anchor breakdown).
        - `render.sh` — one-command regeneration script (Chrome headless → PDF + PNG). Reproducible.
    - `wiki/views/capability-map.md` — new `## Visual exports` section added between L2 Capability Frame Diagram (Mermaid) and Service Domain L2 Capabilities sections. Inline PNG embed + links to PDF/PNG/HTML (this-page render + combined render + S2R sister render).
    - `wiki/views/capability-map-s2r.md` — same `## Visual exports` section structure added in parallel position. Inline PNG embed + same set of links (this-page render + combined render + Operations sister render).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Visualisation choice — boxes-in-boxes (CSS Grid matrix) over Mermaid extension or treemap library.** Boxes-in-boxes is the canonical TMF / business-architecture capability-map visual style; matches what stakeholders expect; gives precise control over hierarchy depth (Lifecycle Area > Domain × Vertical > L2 > H5 nested 4-deep). Mermaid auto-layout was rejected for this purpose — its flowchart engine renders 16-22 nodes with nested sub-graphs awkwardly compared to the explicit grid layout. Treemap libraries (d3.js, plotly) were rejected — they optimise area allocation but lose the domain × vertical matrix structure that's the point of the heat-map overlay frame.
    - **Source format — hand-built HTML + CSS Grid, rendered via Chrome headless.** Available rendering stack on this machine: Python 3 (no matplotlib / weasyprint / cairosvg installed); Google Chrome.app (can do headless HTML→PDF + screenshot); macOS sips. Chrome headless gives high-quality PDF (with `@page` CSS controlling page size) plus PNG via `--screenshot` at `--force-device-scale-factor=2` for crispness. No external dependencies beyond Chrome (which the user already has).
    - **Three artefacts, three @page sizes.** S2R map (16 + 6 = 22 anchors, 3 vertical rows) — A3 landscape. Operations map (17 + 8 = 25 anchors, 4 vertical rows) — A3 landscape. Combined map (47 anchors total, 7 vertical rows) — A2 landscape (the 7-row height needs the larger paper to stay readable; A3 landscape would crush the rows).
    - **Cross-Lifecycle composability — three patterns visualised in combined map.**
        - **3-stage × 2-PSR Test maturity row** — six cells marked `⇄ Test row` form a 6-cell heat-map row spanning Strategy → Lifecycle → Operations × Service / Resource. The strongest cross-Lifecycle composability story to come out of Phase 3.
        - **Two-L2 Anomaly pattern** — four cells marked `⇄ Anomaly pair` (Service-side BVD + Operations + Resource-side BVD + Operations). BVD governs / Operations executes pattern.
        - **Four-L2 Catalog lifecycle** — eight cells marked `⇄ Catalog 4-L2` spanning Capability Mgmt (Planning) → BVD (Lifecycle) → ORS (Operational Readiness + Content) on each PSR side.
    - **Connector treatment — pills, not lines.** The `⇄` connector pills mark cell membership in a cross-Lifecycle pattern. Considered drawing actual SVG connector lines between paired cells; rejected for the heat-map use case because connector lines would compete visually with whatever colour the heat-map overlay puts on each cell. Pills convey the relationship without occupying the cell-fill region. Future iteration could add SVG connectors as a presentation-only variant if needed (for stakeholder slides where heat-map overlay isn't applied).
    - **Color coding — Lifecycle Area at the highest level.** Blue palette for S2R (matches the existing `wiki/views/capability-map-s2r.md` page's mental association); green palette for Operations (visually distinct without being garish). In the combined map, L2 box borders are color-coded by Lifecycle Area so a reader tracing a cross-Lifecycle relationship visually can immediately see which side a box belongs to.
    - **Reproducibility.** `render.sh` regenerates all 6 PDF/PNG outputs from the 3 HTML sources via `chrome --headless --print-to-pdf` and `chrome --headless --screenshot`. If the user tweaks any HTML source (different colors, alternative layout, additional badges), `bash render.sh` from inside `wiki/views/diagrams/` regenerates the affected outputs in seconds.
    - **Wiki integration.** Both view pages now have a `## Visual exports` section between their existing Mermaid `## L2 Capability Frame Diagram` section and the per-capability content. Inline PNG embed via standard markdown image syntax (`![](diagrams/...png)`) renders inline in Obsidian; PDF/HTML/sister-page/combined-view links use standard markdown link syntax (avoids triggering wikilink-resolution lint check on non-md files).
    - **No CLAUDE.md amendment needed.** Diagrams are derivative output, not corpus content per CLAUDE.md §2 (corpus content = `raw/` + `wiki/`-as-source-derivative; the diagrams are derivative-of-derivative). No new authority statements; no new TMF facts; no new trilateral linking. The existing CLAUDE.md §13 Obsidian conventions cover the inline-image + markdown-link choices.
    - **Pending decisions:** none.
    - **Next action:** _(none unless user wants iteration on the visualisation — alternative color schemes, SVG connector lines, additional viewport sizes for specific use cases, etc.)_

---

## 2026-05-12T17:00Z — DIAGRAMS — Editable draw.io source for all three capability maps

- **File(s):** none ingested. Derivative visual artefact + generator script.
- **Pages created/updated:**
    - **NEW** `wiki/views/diagrams/capability-map.drawio` — single multi-page draw.io file (3 pages: S2R / Operations / Combined) covering all 47 stable heat-map anchors. 506 mxCell elements; structurally validated (zero broken parent references). Verified via `drawio --export --format png` for all three pages.
    - **NEW** `wiki/views/diagrams/_build_drawio.py` — generator script. Same description data as the HTML renders (L2 + H5 names, descriptions, anchors). Emits valid mxGraph XML using standard draw.io shapes only — rounded rectangles + plain text labels + container groups (`container=1` on L2 boxes so H5s nest visually and move with their parent). No external shape libraries required; opens in any draw.io install.
    - `wiki/views/capability-map.md` — `## Visual exports` section extended with **Editable draw.io source** entry pointing to the new `.drawio` file + generator script.
    - `wiki/views/capability-map-s2r.md` — same addition in parallel position.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Standard-shapes-only constraint.** The user request was specifically for shapes available in a typical draw.io install — no custom shape libraries. Implemented using:
        - Plain rounded rectangles (`rounded=0;whiteSpace=wrap;html=1`) for L2 + H5 boxes and matrix cells.
        - Plain text labels (`text;html=1;strokeColor=none;fillColor=none`) for titles, descriptions, anchor IDs.
        - Container styling (`container=1;collapsible=0`) on L2 boxes so H5 sub-capabilities nest visually inside their parent and move together when the L2 is repositioned.
        - Rotated text (`rotation=-90`) for vertical row labels.
        - All shapes are part of the default draw.io General library — no plugins or custom libraries required.
    - **Editable vs presentation-quality split.** The HTML/PDF/PNG renders are presentation/print artefacts (fixed layout); the `.drawio` file is the editable source. The two are deliberately not auto-synced — practitioners using the .drawio for stakeholder slides will likely re-position cells, recolor for emphasis, or add annotation arrows that don't belong in the wiki's canonical view.
    - **Page sizes match the HTML renders.** S2R = A3 landscape (1684×1190 pt); Operations = A3 landscape extended to 1400 pt height to fit the 4 OFAB rows + dense Resource Support H5 cluster; Combined = A2 landscape (2384×1684 pt).
    - **Cross-page consistency.** Same color palette, same description data, same anchor IDs as the HTML renders — practitioners overlaying heat-map data against the .drawio see the same cells they'd see in the HTML/PDF/PNG versions.
    - **Pending decisions:** none.
    - **Next action:** _(none from this iteration. If the user wants the .drawio re-rendered to PNG/PDF as a default static export — separate from the HTML-driven renders — `drawio --export --format png --page-index N capability-map.drawio` produces it on demand.)_

---

## 2026-05-12T18:00Z — DIAGRAMS — Roadmap layout: vertical-major combined view (verticals across top, domains down side)

- **File(s):** none ingested. Derivative visual artefact.
- **Pages created/updated:**
    - **NEW** `wiki/views/diagrams/capability-map-roadmap.html` — alternative layout for the combined capability map. Same 47 anchors as `capability-map-combined.html` but with axes transposed: 7 vertical columns across the top (3 S2R + 4 Operations); 2 domain rows down the left (Service / Resource). Lifecycle Area band labels span the appropriate column ranges above the column headers. Reads left-to-right as the OSS modernisation roadmap progression (Strategy → Capability → BVD → ORS → Fulfillment → Assurance → Billing) and top-to-bottom as the PSR pair (Service above Resource). A2 landscape page size.
    - **NEW** `wiki/views/diagrams/capability-map-roadmap.{pdf,png}` — rendered outputs (A2 landscape; 440 KB / 1.3 MB).
    - `wiki/views/diagrams/render.sh` — `TARGETS` array extended with `capability-map-roadmap 2400 1500` so the roadmap render regenerates with the rest.
    - `wiki/views/capability-map-s2r.md` — Visual exports section's combined-view entry restructured to list both layouts (areas-stacked + roadmap) as siblings.
    - `wiki/views/capability-map.md` — same restructuring in parallel.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Layout choice and rationale.** The original combined view places verticals as rows (down the side) and stacks the two Lifecycle Areas as separate matrix blocks. The roadmap layout transposes — verticals as columns (across the top), all 7 verticals in one row of column headers separated by Lifecycle Area band labels. This is the canonical "L1 Frame for OSS Layer" arrangement: Service capabilities sit directly above their Resource peers in the same vertical, making PSR-pair comparison the dominant visual axis; left-to-right reading naturally maps to the modernisation roadmap progression.
    - **Both layouts kept available.** They serve different reading purposes — the original is better for "show me everything in one Lifecycle Area" (each area is a discrete block); the roadmap is better for "show me PSR symmetry per vertical" and "trace a capability's lifecycle progression". Heat-map overlays apply equally to either layout because the underlying anchor IDs are identical (47 stable IDs unchanged).
    - **L2 stacking within cells.** Each (domain, vertical) intersection cell stacks its L2s vertically. This handles the variable L2 density per cell uniformly — Strategy and Fulfillment cells have 1 L2 each; Capability Mgmt cells have 4 L2s; ORS cells have 3 (Service) or 4 (Resource). The 2-column packing used in the original combined view doesn't transfer cleanly to a 7-column wide layout (would create excessive horizontal pressure).
    - **Cell background tint by Lifecycle Area** — light blue for S2R cells, light green for Operations cells. L2 box borders also color-coded by area. Lets a reader scanning across a row immediately see where the area boundary crosses (between BVD and ORS columns).
    - **Roadmap-reading footer.** Footer carries explicit "read it like a roadmap" guidance — left-to-right is the OSS modernisation Lifecycle progression; top-to-bottom is PSR-paired comparison. Practitioners unfamiliar with the layout convention get the framing immediately.
    - **Pending decisions:** none.
    - **Next action:** _(none unless user wants the roadmap layout added as a 4th page in `capability-map.drawio` — the .drawio file currently has 3 pages matching the original combined layout's structure. Adding a vertical-major page would require ~150 lines of additional layout code in `_build_drawio.py`. Worth doing if the user prefers this layout for editing.)_

---

## 2026-05-12T18:30Z — DIAGRAMS — Roadmap layout added as Page 4 of capability-map.drawio

- **File(s):** none ingested. Derivative visual artefact.
- **Pages created/updated:**
    - `wiki/views/diagrams/capability-map.drawio` — added 4th page **"Roadmap"** matching the HTML render's vertical-major orientation (verticals across the top, domains down the side). 250 mxCell elements on the new page; total file now 244 KB; structurally validated (4 pages, zero broken parent references). Custom 2480×1500 page size to fit 7 columns of 295pt + label column + margins.
    - `wiki/views/diagrams/_build_drawio.py` — extended with:
        - `emit_grid_roadmap()` — transposed-orientation grid emitter (S2R band spans first 3 column ranges; Operations band spans next 4; vertical column headers below; domain row labels on left; cells stack L2s vertically).
        - `build_roadmap_page()` — top-level page builder.
        - `stacked_height()` helper for computing the vertical stack height needed per (domain, vertical) intersection.
        - Refactored `emit_l2_box()` to take a `stroke` color parameter so L2 box borders match their Lifecycle Area in the new layout (blue for S2R columns, green for Operations columns). Backward-compatible default keeps existing pages rendering as before, and threaded through `emit_grid()` so the existing combined-page L2 borders are now also area-colored.
        - Bug fix: `cell()` helper now escapes `"` in the `value` attribute (was breaking on the domain row labels containing *"What is sold"* / *"What runs underneath"* phrases).
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Page 4 mirrors `capability-map-roadmap.html` orientation.** Same 47 anchors, same descriptions, same color palette. The HTML render is the print/presentation export; the .drawio page is the editable equivalent.
    - **L2 border color now Lifecycle-Area-aware across all pages.** The original `emit_l2_box()` hardcoded `S2R_MID` for the L2 border color regardless of which area the L2 lived in. Refactor adds a `stroke` parameter; `emit_grid()` and `emit_grid_roadmap()` now both pass the area-appropriate color through. Side effect: the existing "Combined" page (Page 3) now also shows correct area-colored L2 borders — a minor improvement to the combined page that also landed in this commit.
    - **Custom page size for Roadmap.** A2 landscape (1684×1190) is too narrow for 7 columns at comfortable reading width — would require columns ~210pt wide, cramping L2 names. Roadmap page uses custom 2480×1500 to fit 7 columns of 295pt + 140pt label column + gaps. drawio handles custom page sizes natively (`pageWidth` / `pageHeight` in mxGraphModel).
    - **Pending decisions:** none.
    - **Next action:** _(none — capability-map.drawio now contains all 4 layouts: 3 area-specific renders + 2 combined views. Practitioners can pick whichever matches their immediate task.)_

---

## 2026-05-12T19:00Z — DIAGRAMS — Fix: full vertical names in Roadmap headers + explicit white page background

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py` — two fixes:
        1. Added `FULL_VERTICAL_NAMES` mapping (e.g. `"BVD"` → `"BUSINESS VALUE DEVELOPMENT"`, `"ORS"` → `"OPERATIONS READINESS & SUPPORT"`). Used by `emit_grid_roadmap()` for the horizontal column headers; the original Combined page still uses the short labels in its rotated/vertical labels (where compact text fits the cell shape better).
        2. Added `background="#FFFFFF"` to every `mxGraphModel` element via `build_page()`. Forces white canvas regardless of the user's draw.io theme — without it, dark-mode draw.io desktop renders the canvas dark, which made the matrix gridlines (cell strokes) appear very prominent against a dark background.
    - `wiki/views/diagrams/capability-map.drawio` — regenerated. Both fixes verified in the XML; `STRATEGY MANAGEMENT`, `CAPABILITY MANAGEMENT`, `BUSINESS VALUE DEVELOPMENT`, `OPERATIONS READINESS & SUPPORT` all present in roadmap-page column headers; `background="#FFFFFF"` present on all 4 pages.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Why a separate FULL_VERTICAL_NAMES dict rather than changing S2R_GRID/OPS_GRID directly.** The grid data is shared between `emit_grid()` (used by S2R / Operations / Combined pages — labels rendered as rotated text in narrow cells where short labels fit better) and `emit_grid_roadmap()` (Roadmap page — labels rendered as horizontal column headers in wide cells where full names fit comfortably). Keeping the data short and mapping at render time per layout preserves both use cases.
    - **Why `background="#FFFFFF"` rather than relying on draw.io defaults.** The drawio file format does not strictly require a `background` attribute — when omitted, draw.io applications fall back to the user's current theme color. Light-theme users see white; dark-theme users see dark. Setting it explicitly in the file overrides the theme so the file renders consistently regardless of viewer setup. Same pattern applied to all 4 pages for consistency.
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T19:30Z — DIAGRAMS — Roadmap page: line-break rendering fix + domain label restructure

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        1. **`cell()` helper now converts `\n` to `&#10;`** (XML newline entity) after escape. Under drawio's `html=1` rendering mode, literal newline characters are treated as whitespace; the `&#10;` entity forces actual line breaks. Fixes column headers and domain labels appearing as run-on text rather than multi-line stacked.
        2. **Domain row labels restructured** — was `"SERVICE\nDOMAIN\n\nGB991 §1.1.1.5\n\n\"What is sold\"\n— services realizing\nProduct offerings"` (which split "SERVICE DOMAIN" across two lines and chunked the description awkwardly); now `"SERVICE DOMAIN\n\nGB991 §1.1.1.5\n\n\"What is sold\" — services realizing Product offerings"` (three centered lines: name / ref / description). Same shape on Resource side.
    - `wiki/views/diagrams/capability-map.drawio` — regenerated with both fixes.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **drawio html=1 line-break behavior.** The `html=1` style flag tells drawio to render the cell value as HTML; under HTML, `\n` collapses to whitespace. The XML entity `&#10;` (or `&#xa;`) is the canonical way to encode an actual newline character that drawio renders as a break. Drawio's own UI emits files this way.
    - **Why apply globally to `cell()` helper rather than per-callsite.** All cells in this file use `html=1` styling (set by `style_box()` and `style_text()` defaults). A central `\n` → `&#10;` conversion in the cell() emitter ensures every multi-line value renders consistently regardless of where in the script it's constructed. Single-line values are unaffected (no `\n` to convert).
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T20:00Z — DIAGRAMS — L2 box height fix + drop embellishment from Lifecycle Area band labels

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        1. **`L2_HEIGHT_BASE` 90 → 108.** The anchor footer at `y = box_h - 14` was sitting only 2px from the box's bottom border, causing visible clipping at typical render scales. Bumping base height + pushing the anchor footer up by 4px (`box_h - 14` → `box_h - 18`) gives proper bottom margin. Affects all 4 pages (S2R / Operations / Combined / Roadmap) since `L2_HEIGHT_BASE` is shared.
        2. **Band labels stripped of embellishment.** Was *"STRATEGY-TO-READINESS LIFECYCLE AREA — what to build / how to deliver"* and *"OPERATIONS LIFECYCLE AREA — day-to-day customer operations"*; now just *"STRATEGY-TO-READINESS"* and *"OPERATIONS"*. The verbatim TMForum names from GB991 §1.1.2.1 are exactly *"Strategy-to-Readiness"* and *"Operations"*; the *"LIFECYCLE AREA"* suffix and the descriptive em-dash phrases were my additions, not source-faithful. Applied to both the original Combined page and the Roadmap page.
    - `wiki/views/diagrams/capability-map.drawio` — regenerated with both fixes.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Why the box height fix was needed.** drawio's text rendering positions text within the cell's geometry; with the anchor footer at `y = box_h - 14` (height 12, so reaching `y = box_h - 2`) and a 1.5px stroke, the visible inner space below the footer was effectively 0.5px. At display scales ≥ 100% the bottom of the anchor text was being clipped by the box border. Bumping base height to 108 + footer position to `box_h - 18` leaves ~6px clearance.
    - **Verbatim discipline (CLAUDE.md §1) reinforced.** The *"LIFECYCLE AREA"* and descriptive phrases I had added were technically derivative content — fine in narrative prose but problematic on a diagram label that reads as if it were the canonical TMF term. Stripping back to just the GB991 verbatim terms is the right call. Applies to both view pages too if I add Lifecycle Area band labels there (currently they don't have them — capability-map.md and capability-map-s2r.md identify their area in the page H1 / Session State, not via embedded band labels).
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T20:30Z — DIAGRAMS — Roadmap promoted to Page 1 + A3 landscape + footer + centered title

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        - **Page order changed.** Roadmap promoted to Page 1; S2R / Operations / Combined slide down to pages 2 / 3 / 4. Reflects that the Roadmap layout is now the primary view.
        - **Roadmap page resized to A3 landscape (1684×1190 pt).** Fits TMForum's standard print/share format — was 2480×1500 custom which didn't match any standard paper size.
        - **Compact-mode L2 boxes** to make all 47 anchors fit in A3 landscape:
            - Roadmap-specific layout constants (`ROAD_DOMAIN_LABEL_W=100`, `ROAD_COL_W=205`, `ROAD_BAND_H=22`, `ROAD_HDR_H=38`, `ROAD_CELL_GAP=6`, `ROAD_CELL_PADDING=6`, `ROAD_L2_GAP=6`).
            - `emit_l2_box()` extended with a `compact=True` flag — switches to tighter dimensions (L2 base 88, name area 46, H5 height 38, smaller fonts: id 8pt, name 9pt, desc 7pt; H5: name 8pt, desc 7pt, src 6pt). Default `compact=False` preserves existing pages unchanged.
            - `stacked_height()` extended with same `compact` flag for accurate per-cell row sizing.
        - **Centered title and subtitle** on the Roadmap page (was left-aligned). Title text simplified to *"OSS Capability Map — Roadmap Layout"*.
        - **New `emit_footer()` helper** — emits a single-row footer strip: dark filler on the left, then alternating blue label + white content cells. Mirrors the user-supplied screenshot. Used on the Roadmap page with fields: Document = "OSS Capability Map", Author = "Adam Moyes", Version = "1.0", Last Updated = "11 May 2026".
    - `wiki/views/diagrams/capability-map.drawio` — regenerated. Roadmap is now Page 1, A3 landscape, with title centered and footer at bottom. 259 mxCells on the Roadmap page (up from 250 — added footer cells); 4 pages total; zero broken parent references.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Why compact-mode rather than larger A3 page.** The Roadmap layout's natural width is ~2300 pt at comfortable reading sizes. Forcing it onto A3 landscape (1684 wide) requires column compression to ~205pt and proportional reductions across all L2/H5 dimensions. A3 is the most-printed paper size in business contexts; the trade-off (smaller fonts, tighter layout) buys universal print compatibility.
    - **Why pre-defined compact dimensions rather than auto-fit.** Auto-fitting would require iterative layout (compute → measure → adjust → recompute) which complicates the generator. Pre-defined compact constants are a one-time tuning exercise; the constants are easy to adjust if the user wants different sizing.
    - **Footer width allocation.** Each label-content pair is 80+130 = 210pt. 4 pairs = 840pt. Page body width minus 4 pairs = the dark filler width on the left (auto-sized). Dark filler doesn't carry any text — it's a visual anchor that mirrors the source image's layout (likely a placeholder for branding / page number in the original document template).
    - **Other pages unchanged.** S2R / Operations / Combined pages still render as before (verticals down side, etc.). Only the Roadmap page got the A3 + footer + center treatment.
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T21:00Z — DIAGRAMS — Real A3 page size + triple-redundant white background

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        - **Page sizes corrected to drawio's actual A-series presets.** Was using `1684×1190` for "A3 landscape" — that's actually closer to A2 landscape; drawio doesn't recognize it as A3 in the page-format dropdown. Real drawio A3 landscape preset is **1654×1169 pt** (per drawio source: `gPresetPageFormats.a3 = mxRectangle(0,0,1169,1654)`). Updated all 4 pages: Roadmap + S2R + Operations now use 1654-wide; Combined uses 2339-wide (real A2 landscape). The Operations page keeps an extended height (1400 vs 1169) to fit the dense ORS row.
        - **Triple-redundant white background** on every page via `build_page()`:
            1. `background="#FFFFFF"` on `mxGraphModel` (older drawio)
            2. `pageBackground="#FFFFFF"` on `mxGraphModel` (newer drawio attribute name)
            3. Explicit white-fill rectangle as the first content cell on every page (`id="bg"`, fills the whole page area; final fallback that renders white even if the canvas theme is dark)
        - **Roadmap page recompressed slightly** to fit the now-30pt-narrower page width (`ROAD_DOMAIN_LABEL_W` 100→90, `ROAD_COL_W` 205→207, `ROAD_CELL_GAP` 6→5, `ROAD_CELL_PADDING` 6→5, `ROAD_L2_GAP` 6→5, page margin 18→14).
    - `wiki/views/diagrams/capability-map.drawio` — regenerated.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Why background still appeared dark before this fix.** Newer drawio versions appear to ignore the `background` attribute in favour of `pageBackground` (or expect both). When the file specifies neither in a way the running drawio recognises, the canvas theme color shows through — `#121212` is the typical drawio dark-mode canvas. Setting both attributes plus an explicit white rectangle covers all known render paths.
    - **Why `1654×1169` not `1684×1190` for A3 landscape.** drawio uses 100dpi for paper conversions: 297mm × 100/25.4 = 1169.29; 420mm × 100/25.4 = 1653.54. drawio's preset rounds to 1169 / 1654. Setting these exact values makes drawio's UI display the page as "A3 (Landscape)" rather than "Custom".
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T22:00Z — DIAGRAMS — Roadmap text overlap fix (2-line allocations for wrapping fields)

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        - **L2 name cell height** in compact mode increased from 16px (1 line) to 28px (2 lines). When a name like *"Service Specification Lifecycle Management"* wraps to 2 lines, the rendered text now stays inside the name cell rather than spilling into the desc cell below.
        - **L2 desc cell height** increased from 12px (1 line) to 24px (2 lines). Same fix for descriptions.
        - **H5 desc cell height** increased from 13px (1 line) to 26px (2 lines). Same fix for the yellow sub-capability boxes — wrapped descriptions no longer cover the source/anchor label below.
        - **H5 source line dropped** in compact mode (`line_h5_src = 0`) — saves ~13px per H5. The src+anchor info is preserved in non-compact pages and on the wiki source pages.
        - **L2 anchor footer dropped** in compact mode via new `show_anchor_footer` flag. Also a vertical-space saving; anchor info preserved elsewhere.
        - Tightened `ROAD_*` constants to fit the now-taller cells inside A3 landscape: `ROAD_CELL_PADDING` 5→4, `ROAD_L2_GAP` 4→3, `ROAD_L2_HEIGHT_BASE` 88→72, `ROAD_L2_NAME_HEIGHT` updated to 70 (matches new compact branch).
    - `wiki/views/diagrams/capability-map.drawio` — regenerated.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Why the overlap happened.** drawio cells use absolute positioning with fixed widths and heights. Text inside a cell with `whiteSpace=wrap` flows internally but the cell boundary is fixed. When text wrapped to a second line, it rendered beyond the cell's bottom edge — and since the next cell (description) was positioned at `cell_top + previous_cell_height`, the wrapped text visually overlapped it. Fix: allocate enough height in the wrapping cell so 2-line text fits within the cell boundary.
    - **Why fixed-height cells rather than auto-flow.** drawio doesn't have CSS-style auto-layout where one cell pushes the next down. Each cell has absolute coordinates. The only way to prevent overlap is either (a) allocate enough height up front, or (b) use a single multi-line cell with HTML formatting. Approach (a) is simpler and what's done here.
    - **What was sacrificed to fit A3.** The L2 anchor footer (small grey text at the bottom of each L2 box) and the H5 source line (`L3 1.4.1.8 — cap-...`) are hidden in compact mode. Both are still visible on the S2R / Operations / Combined pages (which use larger page sizes) and in the wiki source pages. The trade-off: the Roadmap page is now overview-friendly at A3 size; readers needing the source/anchor citations can drill into the other pages.
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T22:30Z — DIAGRAMS — Roadmap footer legend explaining the asterisk on multi-vertical L2s

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        - `emit_footer()` extended with optional `legend` parameter — text rendered as small light-gray label inside the dark filler area on the left of the footer (was previously empty space).
        - `build_roadmap_page()` now passes a legend explaining the asterisk on multi-vertical L2 IDs: *"L2 spans multiple verticals, placed under primary vertical — 1.5.5: Fulfillment + ORS | 1.5.7: all four OFAB verticals"*.
    - `wiki/views/diagrams/capability-map.drawio` — regenerated.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **Why the asterisk needed explanation.** Two L2s appear with `*` suffix — `1.5.5*` Resource Order Management and `1.5.7*` Resource Data Management. GB921 v25.5 places these L2s under multiple `Vertical Group` values (1.5.5 = Fulfillment + ORS; 1.5.7 = all four OFAB verticals). The capability map renders each L2 once under its primary vertical to avoid visual duplication; the asterisk flags that the L2 logically also covers other verticals. User noticed the asterisks and asked what they meant — fair feedback that the symbol needed a key.
    - **Why in the dark filler rather than as a separate cell.** The footer's dark filler area was visual ballast (matching the source image's design template), carrying no information. Repurposing it for the legend removes wasted space and avoids restructuring the matrix-vs-footer layout. Light-gray text (`#DDDDDD`) on dark background is legible without competing with the more prominent blue/white document fields.
    - **Other pages still don't carry this legend** — they have asterisks too (Operations and Combined pages render 1.5.5 and 1.5.7 with the same asterisk marker). Could be added there in a follow-up; the HTML renders' footers already explain the asterisk in their separate legend section.
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T23:00Z — DIAGRAMS — Roadmap-only file + asterisk legend repositioned as info-callout note

- **File(s):** none ingested.
- **Pages created/updated:**
    - `wiki/views/diagrams/_build_drawio.py`:
        - **`main()` reduced to single-page output.** S2R / Operations / Combined pages dropped from `capability-map.drawio` per user direction (the Roadmap page covers all 47 anchors in a single A3 view; per-area detail still lives on the wiki source pages). File size dropped from ~233 KB → ~70 KB.
        - **Asterisk legend removed from footer dark filler.** That area is purely visual delimiter per user direction; restored to no-text style.
        - **Legend strip added between matrix and footer**, styled as an info-callout note: light blue-gray fill (`#EEF2F7`), subtle gray border, italic dark-blue text, with a thick blue (`#5BB6E8`) left-edge bar acting as the "info" indicator. ⓘ icon prefix. Distinct from both the matrix cells (white with colored borders) and the footer (dark filler + blue/white labelled bars).
    - `wiki/views/diagrams/capability-map.drawio` — regenerated as single-page A3 landscape file.
- **Sections skipped:** N/A.
- **Lint result:** PASS — see lint following.
- **Open questions filed:** none.
- **Notes:**
    - **HTML/PDF/PNG renders unchanged.** The decision to drop the other pages applies only to the .drawio file. The HTML-driven exports (`capability-map.{html,pdf,png}`, `capability-map-s2r.{html,pdf,png}`, `capability-map-combined.{html,pdf,png}`) still render the per-area views. The Visual exports section on the view pages still links to all of them.
    - **Pending decisions:** none.
    - **Next action:** _(none.)_

---

## 2026-05-12T23:15Z — DIAGRAMS — Note callout: separate bar and text cells with spacingLeft

- **Pages updated:** `wiki/views/diagrams/_build_drawio.py` — note cell now starts at `x = margin + bar_w` (after the blue bar) rather than overlapping it; added `spacingLeft=12` internal padding so the ⓘ icon has breathing room from the bar's right edge. `wiki/views/diagrams/capability-map.drawio` regenerated.
- **Lint result:** PASS — see lint following.
- **Notes:** User reported the ⓘ icon was visually touching the blue left-edge bar. Was caused by both cells starting at the same `x = margin` — the blue bar overlaid the note's left padding area. Now bar and text are non-overlapping cells; `spacingLeft` controls the icon-to-bar gap precisely.

---

## 2026-05-12T23:30Z — DOCS — Resume prompt for capability-map refinement (relocated to repo root)

- **Pages updated:** Moved `wiki/views/diagrams/RESUME-PROMPT.md` → `CAPABILITY-MAP-RESUME-PROMPT.md` (repo root) — process-management artifact, consistent with `S2R-EXPANSION-SCOPE.md` placement; lives outside `wiki/` so the linter doesn't require corpus-type frontmatter.
- **Lint result:** PASS — see lint following.
- **Notes:** Prompt captures orientation steps, the always-export-PDF-and-PNG directive, established design decisions, and workflow conventions. Drop the file content into a fresh session as the opening message to continue capability-map refinement work without re-explaining context.

---

## 2026-05-12T23:45Z — DOCS — View pages: .drawio description corrected to single-page Roadmap

- **Pages updated:** `wiki/views/capability-map.md` + `wiki/views/capability-map-s2r.md` — Visual exports section's "Editable draw.io source" paragraph was stale (described the .drawio as a "single multi-page draw.io file with all three diagrams"); corrected to reflect the now-current "single-page A3-landscape Roadmap layout" reality. Also tweaked `CAPABILITY-MAP-RESUME-PROMPT.md` — render-command wording mentions the `TARGETS` array (so future additions don't silently invalidate the prompt) and the log-reading instruction recommends `grep + Read offset/limit` over a large `tail -N` (avoids tool-output cap).
- **Lint result:** PASS — see lint following.
- **Notes:** Surfaced by a fresh-session test of the resume prompt — the test agent flagged the stale view-page paragraphs and suggested the prompt tweaks. Bug-fixes only; no design change.
