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
