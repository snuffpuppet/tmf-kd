# Open Questions

Ambiguities, missing cross-references, version mismatches, and source defects that require
user input. Filed by the agent during ingest. Closed only by user direction. Format defined
in [[CLAUDE]] §8.

---

## OQ-001 — GB991 §1.1.1.2 source heading typo: "Sles" vs "Sales"

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/domains.md
- **Question:** GB991 v25.5 §1.1.1.2 has the heading "Sles Domain" while the body text
  uses "Sales domain". The body text content is consistent with the canonical
  understanding of a Sales Domain. Treated as a typo in the source heading; the wiki
  uses "Sales Domain" as the section heading and notes the source typo verbatim.
- **Blocking:** None — wiki content can proceed. Flagging for user awareness in case
  the typo is corrected in a future GB991 version, or in case "Sles" is in fact
  intentional TMF terminology (very unlikely).

---

## OQ-002 — Business vs Non-Business domain assignment depends on Figure 1-1

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/domains.md
- **Question:** GB991 §1.1.1 distinguishes "Business Domains (shown in color in the
  diagram below)" from "Non-Business Domains". Figure 1-1 is the colour-coded diagram;
  it cannot be reconstructed from PDF text extraction. From the textual descriptions
  alone, §1.1.1.9–§1.1.1.11 explicitly classify Shared, Patterns, and Integration as
  "specialized" or "business-agnostic" — implying these three are Non-Business — and
  the other eight (Market, Sales, Product, Customer, Service, Resource, Business
  Partner, Enterprise) are Business. This inference is not directly confirmed by source
  text.
- **Blocking:** None for v1. The wiki currently lists all 11 domains in a single
  section without business/non-business categorisation. If categorisation matters for
  later use, confirm against Figure 1-1 directly (open the PDF) and update the wiki.

---

## OQ-003 — GB991 INF principle numbering gap

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/principles.md
- **Question:** GB991 v25.5 §2.2.3 (Information Framework principles) lists #INF-01,
  then jumps to #INF-05, #INF-06, #INF-07, #INF-08, #INF-09, #INF-10. Numbers
  #INF-02, #INF-03, #INF-04 do not appear. Possible explanations: (a) source typo;
  (b) deprecated principles removed without renumbering; (c) extraction artifact (the
  pdftotext extraction for §2.2.3 spans pages 28–29 and showed no missing content).
  Visual inspection of the PDF confirms the gap is in the source itself.
- **Blocking:** None. Wiki preserves verbatim numbering with this gap noted.

---

## OQ-004 — GB991 Functional Framework principles flagged for revision

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/principles.md
- **Question:** GB991 §2.2.4 prefaces the Functional Framework principles with: "We
  are currently in the process of redefining the principles of the Functional
  Framework. This is an iterative process and we plan to remove the current principles
  and add new one as they are identified discussed and approved to be included.
  Previous List of Principles, will be curated in next version." Additionally, #FUF-02
  carries the editorial annotation "[TO BE EDITED BY KAJ / DONE]". The current FUF
  principles are therefore explicitly transitional content.
- **Blocking:** None — wiki ingests the verbatim "previous list" and notes the source
  caveat. When the next GB991 version is released with curated principles, re-ingest
  and resolve.

---

## OQ-005 — GB991 §1.2 (Business Capability Map) is FUTURE WORK

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/_index.md (no page created)
- **Question:** §1.2 is marked "(FUTURE WORK)" in v25.5 — empty placeholder. No content
  to ingest. Watch for content in future versions.
- **Blocking:** None.

---

## OQ-006 — GB991 §1.6 (Metrics) and §2.2.5 (Metrics principles) are FUTURE WORK

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/_index.md (no page created)
- **Question:** §1.6 (Metrics concept) and §2.2.5 (Metrics principles) are both marked
  "(FUTURE WORK)" in GB991 v25.5 — empty placeholders. No content to ingest. Watch
  for content in future versions.
- **Blocking:** None.

---

## OQ-007 — GB991 §1.2.1 Business Capability principles is FUTURE WORK

- **Raised:** 2026-05-08
- **Source page:** wiki/foundations/principles.md
- **Question:** §2.2.1 (Business Capability principles) is marked "(FUTURE WORK)" in
  v25.5 — empty placeholder. No content to ingest. Watch for content in future
  versions.
- **Blocking:** None.

---

## OQ-008 — SID Product entity trilateral links pending eTOM/ODA ingest

- **Raised:** 2026-05-08
- **Source page:** all 12 pages in `wiki/sid/product/` (shared)
- **Question:** Each SID Product ABE page has two trilateral sections — "ODA
  Components That Own This Entity" and "eTOM Processes That Manipulate This Entity" —
  that cannot be populated until the ODA component layer (GB1022, IG1167) and the eTOM
  process layer (GB921) are ingested. This is the structural gap from ingest order:
  SID is being ingested before eTOM and ODA per the agreed sequencing, so trilateral
  references on SID pages necessarily await those later ingests.
- **Blocking:** None for ingest of SID; trilateral pages will be revisited and
  populated as eTOM L2 and ODA component pages are added. This single open question
  serves as the placeholder reference from all SID Product ABE pages.

---

## OQ-009 — BE-level attribute and relationship detail deferred

- **Raised:** 2026-05-08
- **Source page:** all 12 pages in `wiki/sid/product/`
- **Question:** v1 GB922 Product ingest captures ABE-level overviews and headline
  Business Entity definitions but does not exhaustively reproduce attribute tables,
  every BE definition, or the figure-by-figure relationship detail. Per CLAUDE.md §5.2
  (v1 granularity decision), this is a deliberate scope choice. Detailed
  attribute/relationship work is available directly in GB922 Product v25.5 PDF until a
  follow-up ingest deepens the wiki content.
- **Blocking:** None. Surface for awareness; inform follow-up ingest planning.

---

## OQ-010 — `plannedOrActutalCapacity` typo in source

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/product/product-capacity-abe.md
- **Question:** GB922 Product v25.5 §4.10 references attribute `plannedOrActutalCapacity`
  on the Capacity entity. Almost certainly a typo for `plannedOrActualCapacity`.
  Preserved verbatim per CLAUDE.md §1, with a note. The Common Domain Capacity ABE may
  resolve this when ingested; until then the wiki preserves the source spelling.
- **Blocking:** None.

---

## OQ-011 — Product Performance ABE «notFullyDeveloped» per source

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/product/product-performance-abe.md
- **Question:** GB922 Product v25.5 §4.11 explicitly tags this ABE as «notFullyDeveloped»
  with only an overview paragraph. Re-ingest when the source matures.
- **Blocking:** None.

---

## OQ-012 — Strategic Product Portfolio Plan ABE «notFullyDeveloped» per source

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/product/strategic-product-portfolio-plan-abe.md
- **Question:** GB922 Product v25.5 §4.12 explicitly tags this ABE as «notFullyDeveloped».
  Re-ingest when source matures.
- **Blocking:** None.

---

## OQ-013 — Strategy-to-Readiness ABEs in operational corpus

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/product/strategic-product-portfolio-plan-abe.md
- **Question:** §4.12 (Strategic Product Portfolio Plan) sits in the Strategy-to-Readiness
  lifecycle area (per [[wiki/foundations/lifecycle]]), which is generally less directly
  relevant to operational current-state mapping. Two of the eTOM verticals
  (Strategy/Infrastructure/Product Lifecycle Management) are out of scope per CLAUDE.md
  §3 — but at the SID level we have the Strategic Portfolio ABE. Confirm whether this
  ABE should remain in the corpus, be retained but flagged out of mapping scope, or be
  removed.
- **Blocking:** None for ingest. Affects how the user uses this ABE in mapping work.

---

## OQ-014 — GB922 Common spans Common/Pattern/Shared sub-domains; v1 wiki does not formalise

- **Raised:** 2026-05-08
- **Source page:** all 19 pages in `wiki/sid/common/` (shared)
- **Question:** GB922 Common §4.1, §4.2, §4.3 reference Level 1 organisational figures
  for three distinct sub-domains: Common, Pattern, and Shared (per
  [[wiki/foundations/domains]] §1.1.1.9–§1.1.1.11). Some ABEs are explicitly placed in
  Shared (e.g. §4.7 Communication Interaction states "located in «Shared Business
  Entities Domain»"). Others are in Pattern (containing abstract templates). The v1
  wiki uses a single `abe_category: common` for all 19. Each page records its
  source-stated sub-domain in text; the schema does not distinguish.
- **Blocking:** None for ingest. If sub-domain navigation matters for mapping work,
  CLAUDE.md §6 abe_category options could be extended to `product | service | resource
  | common | pattern | shared`. This would mean re-categorising existing pages. Defer
  until use shows the need.

---

## OQ-015 — Source spelling "authentification" preserved verbatim

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/digital-identity-abe.md
- **Question:** GB922 Common §4.8 uses "authentification" (a French-influenced
  English variant of "authentication") several times. Preserved verbatim per
  CLAUDE.md §1.
- **Blocking:** None.

---

## OQ-016 — Calendar ABE content thin in v1 ingest

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/calendar-abe.md
- **Question:** §4.9 Calendar ABE spans 22 pages with detailed scheduling and time
  conflict modelling. v1 ingest captured the chapter overview only — the actual BE
  inventory (Calendar, ScheduleEntry, TimeConflict, etc.) and their attributes are not
  yet in the wiki. Deepen on follow-up if scheduling work becomes important.
- **Blocking:** None.

---

## OQ-017 — Location ABE BE inventory deferred

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/location-abe.md
- **Question:** §4.10 Location ABE spans 79 pages covering coordinates, addresses,
  areas, and country-specific subtleties. v1 ingest covers conceptual structure and
  major BEs only; the full address-pattern detail (which is genuinely complex per the
  source's own disclaimer) is deferred.
- **Blocking:** None.

---

## OQ-018 — Root Business Entities ABE BE inventory deferred (131 pages)

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/root-business-entities-abe.md
- **Question:** §4.12 is the largest single ABE chapter (131 pages). v1 ingest captures
  the top-of-hierarchy concepts (RootEntity, EntitySpec/Entity, ManagedEntity,
  Collection, Attachment, CharSpec/CharValue patterns) at the conceptual level. Many
  pattern entities and their detailed structures are in the source.
- **Blocking:** None for ingest. Deepening recommended given how foundational this
  ABE is — almost every other SID entity inherits from RootEntity or its patterns.

---

## OQ-019 — Metric ABE content depth deferred (110 pages)

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/metric-abe.md
- **Question:** §4.19 Metric ABE spans 110 pages including Best Practices for design
  and application. v1 ingest covers conceptual content only.
- **Blocking:** None.

---

## OQ-020 — Project ABE content depth deferred (170 pages)

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/project-abe.md
- **Question:** §4.22 Project ABE is the largest single chapter (170 pages). v1
  ingest is conceptual; WBS, Activity, scheduling detail not extracted.
- **Blocking:** None.

---

## OQ-021 — Project ABE relevance to operational mapping

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/project-abe.md
- **Question:** The Project ABE is a generic project management model that the source
  intends organisations to extend ("by SID blades"). Its relevance to current-state
  monolithic-OSS-to-PSR mapping is uncertain. Confirm whether it should remain in the
  corpus, be flagged as out of mapping scope, or be deferred for v2.
- **Blocking:** None.

---

## OQ-022 — Network Service Spec / Usage Volume Service Spec sub-ABEs «Preliminary»

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/service/service-specification-abe.md, wiki/sid/service/service-abe.md
- **Question:** GB922 Service §4.3.1.3, §4.3.1.5, §4.4.1.3, §4.4.1.4 are
  source-tagged «Preliminary». Content may evolve. Re-ingest when source matures.
- **Blocking:** None.

---

## OQ-023 — Service Performance ABE marked work-in-progress

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/service/service-performance-abe.md
- **Question:** GB922 Service §4.9 source notes "this section is still a work in
  progress, and is subject to change." SLS/SLA/KPI structure may evolve.
- **Blocking:** None.

---

## OQ-024 — Service Problem ABE «NotFullyDeveloped»

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/service/service-problem-abe.md
- **Question:** GB922 Service §4.11 source-tagged «NotFullyDeveloped». Service
  Problem Management is operationally important (in-scope eTOM L2 per CLAUDE.md §3),
  yet the SID-side data model is incomplete. May limit mapping work in this area
  until the source matures or until eTOM-side ingestion fills the gap from the
  process angle.
- **Blocking:** Partial — production-side fault/alarm/outage mapping has reduced
  data-layer reference until SID Service Problem matures.

---

## OQ-025 — Service Strategy & Plan ABE «notFullyDeveloped» + scope question

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/service/service-strategy-and-plan-abe.md
- **Question:** GB922 Service §4.12 source-tagged «notFullyDeveloped». Additionally,
  this ABE sits in the Strategy-to-Readiness lifecycle area, which is partially out
  of scope per CLAUDE.md §3 (the SIP vertical is excluded; this is a Strategy-area
  ABE). Confirm whether to keep in corpus or flag/remove.
- **Blocking:** None.

---

## OQ-026 — TIP Service Management ABE «likelyToBeDepreciated»

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/service/tip-service-management-abe.md
- **Question:** GB922 Service §4.13 source explicitly states "This ABE is likely to
  be removed in Release 25.5". Source-tagged «likelyToBeDepreciated» (sic; "deprecated"
  is the standard spelling — preserved verbatim). The TIP (TMF Interface Program /
  MTOSI 2.0) machinery is legacy; replaced by the TMF Open API Program. When v25.5
  Service is published this ABE may disappear; the wiki page should be removed at
  that point.
- **Blocking:** None.

---

## OQ-027 — GB922 Resource v25.5 is Pre-production / Team Approved

- **Raised:** 2026-05-08
- **Source page:** all 13 pages in `wiki/sid/resource/`
- **Question:** GB922 Resource v25.5 PDF metadata reports "Release Status:
  Pre-production" and "Approval Status: Team Approved" — distinct from standard
  Production / TM Forum Approved status. Ingested with explicit user authorisation
  per the workflow established at the SID Resource pre-flight check
  (see log entry 2026-05-08T13:30Z and prior). All Resource ABE pages carry
  `release_status: pre-production` in frontmatter (CLAUDE.md §6 field added during
  this ingest).
- **Blocking:** None for ingest. Surfaces caution for downstream readers; re-ingest
  when v25.5 reaches Production status (or v26 supersedes).

---

## OQ-028 — `«doNotImplement»` example sub-ABEs preserved

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/resource-specification-abe.md, wiki/sid/resource/resource-abe.md
- **Question:** GB922 Resource §4.2.3.3 (LogicalResource Spec Examples) and §4.3.3.4
  (LogicalResource Examples) are source-tagged «doNotImplement». The wiki preserves
  these as sub-section references for completeness but flags the source's
  implementation guidance.
- **Blocking:** None.

---

## OQ-029 — §4.3 Computing and Software Addendum content depth

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/resource-abe.md
- **Question:** GB922 Resource §4.3 contains a substantial Computing and Software
  Addendum (§4.3.2, pp. 240–273) with detailed scenarios, plus §4.3.3.3 Computing
  and Software ABE. v1 ingest covers the structural placement at the chapter
  overview level; deepening recommended if Computing/Software resource mapping
  becomes important for the user's monolith decomposition (highly likely for an OSS
  context).
- **Blocking:** None.

---

## OQ-030 — Stock Item ABE relevance to OSS mapping

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/stock-item-abe.md
- **Question:** §4.9 Stock Item ABE is large (148 pages) and covers supply chain
  modelling (warehouse stock, shipments). Its relevance to typical OSS-monolith
  decomposition is uncertain — most OSS monoliths don't include warehouse/supply
  chain. Confirm scope: (a) keep in corpus as reference for completeness, (b) flag
  as out of typical mapping scope, or (c) defer.
- **Blocking:** None.

---

## OQ-031 — Resource Trouble ABE «notFullyDeveloped»

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/resource-trouble-abe.md
- **Question:** GB922 Resource §4.11 source-tagged «notFullyDeveloped». Combined
  with the parallel Service Problem ABE incompleteness
  (see [[wiki/open-questions#OQ-024]]), this is a meaningful gap for production-side
  fault-management mapping work. eTOM Resource Trouble Management L2 is in scope per
  CLAUDE.md §3 — when that ingests, the SID side may need supplementation from other
  TMF documents or deferred entirely.
- **Blocking:** Partial — production-side fault/alarm/repair data-layer reference is
  thin until SID Resource Trouble matures. Continues OQ-024 from Service domain.

---

## OQ-032 — Source verbatim "resoluiton" (sic)

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/resource-trouble-abe.md
- **Question:** GB922 Resource §4.11 uses "resoluiton" (sic — typo for "resolution").
  Preserved verbatim per CLAUDE.md §1.
- **Blocking:** None.

---

## OQ-033 — Resource Topology ABE «notFullyDeveloped»

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/resource-topology-abe.md
- **Question:** GB922 Resource §4.12 source-tagged «notFullyDeveloped»; content
  is overview only.
- **Blocking:** None.

---

## OQ-034 — Resource Strategy & Plan ABE «notFullyDeveloped» + scope

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/resource/resource-strategy-and-plan-abe.md
- **Question:** §4.13 source-tagged «notFullyDeveloped». Sits in the
  Strategy-to-Readiness lifecycle area, which is partially out of scope per CLAUDE.md
  §3. Confirm whether to keep, flag, or remove.
- **Blocking:** None.

---

## OQ-035 — eTOM L2 narrative prose deferred to follow-up

- **Raised:** 2026-05-08
- **Source page:** all 8 pages in `wiki/etom/service-domain/`
- **Question:** GB921 v25.5 ships as both Excel master (the canonical process
  catalogue with IDs/names/Extended Descriptions) and the three Process Decomposition
  PDFs (Service, Resource, Product) which contain richer narrative prose, figures,
  and inter-process relationships. The current Service Domain L2 ingest uses Excel
  data only — it has all the verbatim IDs, names, and Extended Descriptions, but
  the additional narrative depth from GB921_Service_Process_Decompositions_v24.0.pdf
  (217 pages) is not yet layered in. To be added in a follow-up ingest event keyed
  to that PDF.
- **Blocking:** None. The L2 pages are usable as-is; PDF prose adds depth.

---

## OQ-036 — HANDOFF.md L2 scope cross-walk to GB921 v25.5

- **Raised:** 2026-05-08
- **Source page:** wiki/etom/service-domain/_index.md (and equivalent index pages
  for Resource and Product when those ingest)
- **Question:** HANDOFF.md listed in-scope L2s by names from an older eTOM version
  (e.g. "Service Configuration & Activation", "Service Quality Management",
  "Resource Provisioning", "Resource Data Collection & Distribution"). GB921 v25.5
  has restructured: many L2s have new names, splits, or replacements:
    - "Service Configuration & Activation" → likely Service Activation Management
      (1.4.5) plus parts of Service Support Management (1.4.4)
    - "Service Quality Management" → Service Performance Management (1.4.7)
    - "Service Problem Management" — name unchanged (1.4.6)
    - "Service Guiding & Mediation" — name unchanged (1.4.8)
    - "Resource Provisioning" → likely Resource Order Management (1.5.5)
    - "Resource Trouble Management" — unchanged (1.5.8)
    - "Resource Performance Management" — unchanged (1.5.9)
    - "Resource Mediation & Reporting" — unchanged (1.5.10)
    - "Resource Data Collection & Distribution" → likely Resource Data Management
      (1.5.7)
  Per CLAUDE.md §1 (verbatim discipline), the corpus uses v25.5 names. The HANDOFF
  scope is preserved in spirit: operational (OFAB) L2s in Service/Resource/Product.
- **Blocking:** None. Surface for awareness — readers consulting the HANDOFF should
  be aware names have evolved.

---

## OQ-037 — GB1022 ODA mappings reference GB921/GB922 R20.5

- **Raised:** 2026-05-08
- **Source page:** all 6 pages in `wiki/oda/functional-blocks/`
- **Question:** GB1022 ODA Functional Architecture Guidebook v1.1.0 (2021) provides
  rich mapping tables in §4.3.2/3, §4.4.2/3, §4.5/§4.5.2, §4.6.1/2 referencing eTOM
  Process Identifiers and SID ABE names sourced from **GB921 R20.5** and **GB922
  R20.5**. Our corpus uses v25.5/v25.0/v23.0 (eTOM and SID). Many process IDs and
  ABE names have evolved between R20.5 and v25.x (some renamed, some restructured,
  some moved across domains). Per CLAUDE.md §7, version mismatches are recorded
  honestly: each ODA Functional Block page references the source mapping tables
  verbatim and notes the version mismatch; explicit cross-version resolution is
  deferred to the trilateral sweep.
- **Blocking:** None for ODA ingest. The trilateral sweep (OQ-008) is the moment to
  resolve and populate cross-references with v25.x targets where unambiguous, and
  file new OQs where uncertain.

---

## OQ-038 — Non-business ODA blocks have structural trilateral exemption

- **Raised:** 2026-05-08
- **Source page:** wiki/oda/functional-blocks/decoupling-and-integration.md,
  wiki/oda/functional-blocks/engagement-management.md
- **Question:** GB1022 §4.2.2 explicitly states Engagement Management "Holds no
  business process (eTOM), no functions (functional Framework) and no operational
  data (SID)". Decoupling & Integration is similarly framed as a non-business block
  (§4.1.1: "non-business functions"). The corpus's `oda-component` page anatomy
  (CLAUDE.md §5.3) requires SID Entities Owned and eTOM Processes Realised
  trilateral sections. For these two blocks, the sections explicitly note the
  structural exemption per source. The linter's TRI-EMPTY check is satisfied via
  reference to OQ-008 and this OQ.
- **Blocking:** None. Exemption is honoured in pages; lint passes.

---

## OQ-039 — IG1167 ingested as reference summary, not per-block extensions

- **Raised:** 2026-05-08
- **Source page:** wiki/oda/_index.md (IG1167 Proposed Extensions section)
- **Question:** IG1167 ODA Exploratory Report v6.0.0 was previously assessed and held
  pending GB1022 ingest (see log entry 2026-05-08T12:40Z). With GB1022 now in place
  as the canonical baseline, IG1167 has been ingested as a **summary section in
  `wiki/oda/_index.md`** rather than as separate ODA Functional Block extension
  pages. Reasoning:
    - IG1167 §7 sub-sections largely align with GB1022's 6 Functional Blocks (same
      conceptual blocks).
    - Many IG1167 §7 entries are explicitly marked "TBD" or "Ongoing Study" — the
      document is a working report, not a settled standard.
    - Concrete proposals (e.g. §7.5 SID mapping tables) reference GB922 R20.5 — the
      same version mismatch noted in OQ-037.
    - A summary page captures IG1167's role and content map; the source extract
      remains in `raw/extracted/` for detailed lookups.
  When IG1167 proposals are formally incorporated into GB1022 (or a successor
  document), re-ingest as canonical content via the existing ODA Functional Block
  pages.
- **Blocking:** None. IG1167 content is accessible; treated honestly as exploratory.

---

## OQ-040 — Production block trilateral sweep: R20.5→v25.x cross-walk decisions

- **Raised:** 2026-05-08
- **Source page:** wiki/oda/functional-blocks/production.md
- **Question:** GB1022 §4.5 Table 4-9 (eTOM mapping) and Table 4-10 (SID mapping) are
  sourced from GB921 R20.5 and GB922 R20.5. Resolving these to the v25.5 / v25.0 /
  v23.0 corpus required per-row decisions. Decisions taken in this sweep (recorded
  here for audit; reversible if the user disagrees):

  **eTOM L2 — resolved to v25.5 (linked):**
    - R20.5 1.4.4 SM&O Support & Readiness → v25.5 1.4.4 Service Support Management
      (same ID; renamed)
    - R20.5 1.4.5 Service Configuration & Activation → v25.5 1.4.5 Service Activation
      Management (same ID; renamed; v25.5 Extended Description explicitly references
      the legacy "Service Configuration & Activation" name)
    - R20.5 1.4.6 Service Problem Management → v25.5 1.4.6 (same ID, same name)
    - R20.5 1.4.8 Service Guiding & Mediation → v25.5 1.4.8 (same ID, same name)
    - R20.5 1.5.4 RM&O Support & Readiness → v25.5 1.5.4 Resource Support Management
      (same ID; renamed)
    - R20.5 1.5.7 Resource Data Collection & Distribution → v25.5 1.5.7 Resource Data
      Management (same ID; renamed)
    - R20.5 1.5.8 Resource Trouble Management → v25.5 1.5.8 (same ID, same name)
    - R20.5 1.5.10 Resource Mediation & Reporting → v25.5 1.5.10 (same ID, same name)

  **eTOM L2 — absorbed/restructured in v25.5 (NOT linked at L2; L3 evidence noted):**
    - R20.5 1.4.10 Service Test Management → demoted in v25.5 to L3 1.4.4.6 "Manage
      Service Test" under 1.4.4 Service Support Management
    - R20.5 1.5.5 Workforce Management → restructured in v25.5; L4 Workforce
      activities now live under 1.5.4 Resource Support Management (e.g. 1.5.4.8.x).
      v25.5 ID 1.5.5 is now Resource Order Management (different process)
    - R20.5 1.5.6 Resource Provisioning → distributed in v25.5; "Enable Resource
      Provisioning" lives at L3 1.5.4.1 under 1.5.4 Resource Support Management;
      provisioning lifecycle activities also under 1.5.5 Resource Order Management
    - R20.5 1.5.12 Resource Test Management → demoted in v25.5 to L3 1.5.4.9 "Manage
      Resource Test" under 1.5.4 Resource Support Management

    These four R20.5 L2s are not linked individually because the v25.5 reorganisation
    is not a clean rename — the source content was demoted, distributed, or merged.
    The absorbing v25.5 L2s (1.4.4, 1.5.4, 1.5.5) are already linked from the
    "resolved" list above.

  **eTOM — out of scope:**
    - R20.5 1.4.1, 1.4.2, 1.4.3 (Service Strategy/Capability/Specification) — SIP
      vertical, out of corpus scope per CLAUDE.md §3
    - R20.5 1.5.2, 1.5.3 (Resource Capability/Specification) — same
    - R20.5 1.X.Y Service Balance Management — flagged "to be discussed" in source

  **SID ABEs — resolved (linked):**
    - All 8 Service ABEs in Table 4-10 → wiki/sid/service/* (Service, Service Order,
      Service Specification, Service Strategy & Plan, Service Configuration, Service
      Usage, Service Problem, Service Test)
    - All 9 Resource ABEs in Table 4-10 → wiki/sid/resource/* (Resource, Resource
      Order, Resource Specification, Resource Topology, Resource Configuration,
      Resource Usage, Resource Strategy & Plan, Resource Trouble, Resource Test)
    - Common Location ABE → wiki/sid/common/location-abe

  **SID ABEs — gap:**
    - Common Topology ABE listed in Table 4-10 has **no corresponding entity in our
      GB922 Common v23.0 corpus** (the v23.0 Common ingest covered §4.4–§4.22 with
      19 ABEs; no Topology ABE). Resource Topology ABE exists separately in our
      Resource corpus and is the one linked. Whether v23.0 dropped Common Topology,
      renamed it, or whether it was never a top-level Common ABE in v23.0 is
      uncertain. Not linked. May warrant a focused look at GB922 Common v23.0 §4
      structure to verify.

  **SID — Enterprise Workforce ABE:** out of corpus scope (Enterprise Domain not in
    v1 corpus per CLAUDE.md §3).

- **Blocking:** None. Sweep complete for Production; remaining gaps are documented
  here. The cross-walk pattern set here is the template for the other 5 ODA blocks
  (Core Commerce Management, Engagement Management, Party Management, Intelligence
  Management, Decoupling & Integration).

---

## OQ-041 — v1 Common ingest stopped at §4.22; 12 ABEs missed

- **Raised:** 2026-05-08
- **Source page:** wiki/sid/common/_index.md
- **Question:** GB922 Common v23.0 contains ABE chapters §4.4 through §4.30 plus
  four ABEs declared in the §4.1 [ComD-01] Common ABEs Level 1 diagram with brief
  descriptions but no dedicated chapter. The v1 Common ingest (2026-05-08T15:00Z)
  covered §4.4–§4.22 only — 19 ABE pages — leaving 12 Common ABEs absent from the
  corpus. Discovered during the Production block trilateral sweep, where GB1022
  §4.5 Table 4-10 references Common Topology ABE (one of the missing entries).

  **Missed per-chapter ABEs (8):**
    - §4.23 Test ABE — canonical Test pattern; Product Test, Service Test, Resource
      Test all specialise from it
    - §4.24 Usage ABE — canonical Usage pattern; Product Usage, Service Usage,
      Resource Usage all specialise from it
    - §4.25 Segmentation ABE — entity-grouping criteria
    - §4.26 Intent ABE — Intent and IntentReport
    - §4.27 Closed Loop ABE «Preliminary»
    - §4.28 Goal ABE «Preliminary»
    - §4.29 Workflow ABE «Preliminary»
    - §4.30 Anomaly ABE — ties to v25.5 eTOM Anomaly Management L2s

  **Missed diagram-only ABEs (4)** — listed as top-level Common ABEs in §4.1 with
  one-paragraph definitions, no dedicated chapter:
    - Topology ABE — referenced by GB1022 §4.5 Table 4-10 (Production owner)
    - Event ABE («not fully developed»)
    - Trouble Ticket ABE («not fully developed»)
    - Trouble or Problem ABE

  **Resolution:** filling the gap with 12 new pages in the same ingest event that
  raises this OQ. Per-chapter pages get full anatomy from §4.x content. Diagram-only
  pages are honest about thinness — overview from §4.1 brief description, no
  chapter content available. «Preliminary» pages set `release_status: draft` per
  CLAUDE.md §6.

- **Blocking:** None now (resolved in same ingest event). Logged for audit so the
  v1 truncation is not silent.

---

## OQ-042 — Core Commerce Management trilateral sweep: R20.5→v25.x cross-walk decisions

- **Raised:** 2026-05-08
- **Source page:** wiki/oda/functional-blocks/core-commerce-management.md
- **Question:** GB1022 §4.4.2 Table 4-6 (eTOM mapping) and §4.4.3 Table 4-7 (SID
  mapping) are sourced from GB921 R20.5 and GB922 R20.5. Resolving these to the
  v25.5 / v25.0 / v23.0 corpus produced the following per-row decisions; logged
  for audit (reversible if user disagrees).

  **Table 4-6 (eTOM L2) — out of corpus scope:**
    - R20.5 1.1.5 Sales Development, 1.1.9 Selling, 1.1.19 Loyalty Program
      Management — Market & Sales Domain, not in v1 corpus per CLAUDE.md §3
    - R20.5 1.2.1 Product & Offer Portfolio Planning, 1.2.2 Product & Offer
      Capability Delivery — Strategy/Capability lifecycle (S-T-R), out per §3
    - R20.5 1.2.7 Product Specification & Offering Development & Retirement —
      v25.5 retains 1.2.7 but in "Business Value Development" vertical (out of
      OFAB scope per §3)
    - R20.5 1.2.8 Product Capacity Management — not in v25.5 OFAB in-scope set
    - R20.5 1.3.x Customer Order/Problem/QoS Handling — Customer Domain, not in
      v1 corpus per §3
    - R20.5 1.6.x Party (Offering / Agreement / Order / Problem / Special Event /
      Revenue) — Business Partner Domain, not in v1 corpus per §3

  **Table 4-6 (eTOM L2) — resolved to v25.5 (linked):**
    - R20.5 1.2.5 Product Configuration Management → v25.5 1.2.5 (same ID, same
      name)
    - R20.5 1.2.11 Product Inventory Management → v25.5 1.2.11 (same ID, same
      name)
    - R20.5 1.2.16 Product Usage Management → v25.5 1.2.16 (same ID, same name)
    - R20.5 1.2.17 Product Rating & Rate Assignment → v25.5 1.2.17 (same ID,
      same name)
    - R20.5 1.2.18 Product Balance Management → v25.5 1.2.18 (same ID, same
      name)
    - R20.5 1.2.9 Product Offering Purchasing + R20.5 1.2.15 Product Test
      Management → both demoted/restructured in v25.5; activities live under
      v25.5 1.2.4 Product Support Management (L3 1.2.4.4 "Support Product
      Offering Purchasing"; L3 1.2.4.9 "Manage Product Test"). Linking 1.2.4 as
      the absorbing L2 — same precedent as Production block (OQ-040) where
      1.4.4/1.5.4 absorbed equivalent R20.5 L2s.

  **Table 4-6 — NOT linked despite being in v25.5 in-scope Product Domain:**
    - 1.2.27 Product Order Management, 1.2.21/1.2.22 Product Catalog L2s,
      1.2.25/1.2.26 Product Anomaly/Problem Management, 1.2.6 Product
      Performance Management — none of these v25.5 L2s appear in GB1022 §4.4.2
      Table 4-6. The earlier Core Commerce page asserted these mappings by
      inference; per CLAUDE.md §1 they are removed pending source backing (e.g.
      an updated GB1022 or a future TMF mapping document). Note: 1.2.27
      Product Order Management is a strong candidate by content (its Extended
      Description matches R20.5 1.3.3 Customer Order Handling, which is in
      Table 4-6 but in the out-of-scope Customer Domain). Reasonable hypothesis
      that the v25.5 reorg moved Customer Order Handling responsibilities into
      the Product Domain; not in our corpus until a source confirms.

  **Table 4-7 (SID ABE) — out of corpus scope:**
    - Customer Domain entries 01–04 (Customer Product Order, Customer Problem,
      Customer SLA, Applied Customer Billing Rate) — Customer Domain not in v1
      corpus per §3
    - Business Partner Domain entries 01–06 (Party Problem, Business Partner
      Product Order, Party Product Specification & Offering, Party Revenue
      Settlement, Party Service Level Agreement, Applied Party Billing Rate
      «Preliminary - Ongoing study») — Business Partner Domain not in v1 corpus
      per §3

  **Table 4-7 (SID ABE) — resolved (linked):**
    - Product 01 Product ABE → v25.5
      `wiki/sid/product/product-and-offering-instance-abe` (R20.5 "Product ABE"
      definition focused on product instance; v25.5 split into separate
      Specification and Instance ABEs, with both Product and Offering instances
      living in product-and-offering-instance-abe)
    - Product 02 Product Specification ABE → v25.5
      `wiki/sid/product/product-specification-abe` (clean rename)
    - Product 03 Strategic Product Portfolio Plan ABE →
      `wiki/sid/product/strategic-product-portfolio-plan-abe` (clean)
    - Product 04 Product Offering ABE → v25.5
      `wiki/sid/product/product-offering-specification-abe` (R20.5 "Product
      Offering ABE" focused on offering definitions; v25.5 separates the spec
      side here; offering instance side lives in
      product-and-offering-instance-abe — which is also linked from #01)
    - Product 05 Product Usage ABE → `wiki/sid/product/product-usage-abe`
    - Product 06 Product Configuration ABE →
      `wiki/sid/product/product-configuration-abe`
    - Product 07 Loyalty ABE → `wiki/sid/product/loyalty-abe`
    - Product 08 Product Test ABE → `wiki/sid/product/product-test-abe`
    - Common 01 Agreement ABE → `wiki/sid/common/agreement-abe`
    - Common 02 Capacity ABE → `wiki/sid/common/capacity-abe`

  **Pre-existing legacy back-links — preserved with flag, source unknown:**

    Three Common ABE pages have CCM back-links added during the v1 partial sweep
    (referenced in AGENTS.md "Initial trilateral sweep done — 16 eTOM/SID pages
    have reciprocal ODA back-links") with no recorded rationale. They are not in
    GB1022 §4.4.3 Table 4-7. The inferences are plausible:
      - `wiki/sid/common/account-abe` — likely on the basis that Account is
        canonical parent of CustomerBillingAccount, and CCM handles billing
      - `wiki/sid/common/business-interaction-abe` — likely on the basis that
        BusinessInteraction is canonical parent of ProductOrder, and CCM handles
        Order Capture
      - `wiki/sid/common/catalog-abe` — likely on the basis that Catalog is
        canonical parent of Product Catalog, which is core to CCM
    Preserved as forward links from `wiki/oda/functional-blocks/core-commerce-management`
    in an "Additional Common Domain ABEs from v1 partial sweep" sub-section to
    maintain bidirectional consistency. Flagged here for review when a source
    mapping table for these specific links surfaces — until then, treat as
    legacy / inferential rather than Table 4-7-supported.

- **Blocking:** None. Sweep complete for Core Commerce Management; remaining
  v25.5 Product Domain L2s (1.2.27, 1.2.21, 1.2.22, 1.2.25, 1.2.26, 1.2.6, 1.2.4
  for the parts not derived from R20.5 1.2.9/1.2.15) await a source mapping
  document before linking. Pattern continues from OQ-040 / Production block.

---

## OQ-043 — Party Management trilateral sweep: R20.5→v23.0 cross-walk decisions

- **Raised:** 2026-05-08
- **Source page:** wiki/oda/functional-blocks/party-management.md
- **Question:** GB1022 §4.3.2 Table 4-3 (eTOM mapping) and §4.3.3 Table 4-4 (SID
  mapping) are sourced from GB921 R20.5 and GB922 R20.5. Cross-walk to our
  corpus; decisions logged for audit.

  **Table 4-3 (eTOM L2) — out of corpus scope (entire table):**
    - All 32 R20.5 entries in Table 4-3 fall in Market (1.1.x), Customer (1.3.x),
      or Business Partner (1.6.x) domains. None are in Service / Resource /
      Product domains. Per CLAUDE.md §3, all 32 entries are out of corpus
      scope — Party Management produces **zero eTOM L2 wikilinks**. The 1.X.Y
      "Party Identification & Authentication" placeholder is also out of scope
      and source-flagged "to be discussed for next versions".
    - Note: Party Management is fundamentally a cross-cutting block over
      Market/Sales/Customer/Business-Partner domains (per its name). The corpus's
      operational PSR scope intentionally excludes those domains, so an empty
      eTOM trilateral for PM is the source-supported correct outcome (similar
      to Engagement Management's structural exemption per OQ-038, but for a
      different reason — scope exclusion rather than structural absence).

  **Table 4-4 (SID ABE) — domain reorganization R20.5 → v23.0:**
    - GB1022 Table 4-4 places "Party" (#02) and "Party Privacy" (#08) under
      Business Partner Domain. Our v23.0 GB922 Common places them under Common
      Domain. This is a R20.5 → v23.0 reorganization (Party concepts moved to
      Common because they are truly cross-cutting). The CONCEPT is the same;
      the domain placement differs. The v23.0 Common Party / Party Privacy ABEs
      are linked here as the v23.0 successors of the R20.5 entries Table 4-4
      points at.

  **Table 4-4 (SID ABE) — resolved (linked):**
    - R20.5 Common #01 Communication Interaction → v23.0
      `wiki/sid/common/communication-interaction-abe`
    - R20.5 Business Partner #02 Party → v23.0 `wiki/sid/common/party-abe`
      (domain reorg per above)
    - R20.5 Business Partner #03 Business Partner Account → v23.0
      `wiki/sid/common/account-abe` (v23.0 Common Account ABE explicitly
      includes BusinessPartnerAccount per its overview)
    - R20.5 Business Partner #08 Party Privacy → v23.0
      `wiki/sid/common/party-privacy-abe` (domain reorg per above)
    - R20.5 Product #01 Product Party Roles → v25.5
      `wiki/sid/product/product-party-roles-abe`
    - R20.5 Service #01 Service Party Roles → v25.0
      `wiki/sid/service/service-party-roles-abe`
    - R20.5 Resource #01 Resource Party Roles → v25.5
      `wiki/sid/resource/resource-party-roles-abe`

  **Table 4-4 (SID ABE) — out of corpus scope:**
    - Market/Sales Domain entries 01–07 (Strategy and Plan, Market Segment,
      Competitor, Contact/Lead/Prospect, Sales Channel, Market Sales Forecast,
      Market Sales Party Roles) — Market/Sales Domain not in v1 corpus per §3
    - Customer Domain entries 01–05 (Customer Party Roles, Customer
      Interaction, Customer Bill, Customer Bill Collection, Customer Bill
      Inquiry) — Customer Domain not in v1 corpus per §3
    - Business Partner Domain entries 01 Party Strategy & Plan, 04 Party Bill
      «preliminary», 05 Party Bill Collection (about Dunning — uncertain
      v23.0 mapping; Common Party Payment ABE covers payment methods/plans
      not Dunning specifically), 06 Business Partner Party Roles, 07 Party
      Interaction (overlaps R20.5 Common #01 Communication Interaction
      already linked) — Business Partner Domain not in v1 corpus per §3
    - Common #02 Users and Roles — no clean v23.0 successor; closest match
      would be PartyRole within Party ABE but that's already linked. Skip.
    - Enterprise #01 Enterprise Party Roles — Enterprise Domain not in v1
      corpus per §3

  **Pre-existing legacy back-links — preserved with flag:**

    Two Common ABE pages had v1-partial-sweep PM back-links not directly
    supported by Table 4-4:
      - `wiki/sid/common/agreement-abe` — NOT in Table 4-4. The inference is
        plausible (Party Agreement Management is mentioned in §4.3.1 as a PM
        responsibility; v23.0 Agreement ABE is the canonical Agreement model).
        Preserved on PM page in an "Additional Common ABEs from v1 partial
        sweep" sub-section, flagged for source-supported review.
      - `wiki/sid/common/party-payment-abe` — partial support via R20.5 BP
        #05 Party Bill Collection (which mentions "all what is related to
        PartyPayment"). The v23.0 Party Payment ABE covers PaymentMethod,
        PaymentPlan, Bank — broader than Bill Collection / Dunning. Preserved
        with the same flag.

- **Blocking:** None. Sweep complete for Party Management. Note PM is the
  block where corpus scope (operational PSR) most diverges from the source's
  organizational placement — most of GB1022 §4.3 references Customer / Business
  Partner / Market-Sales domain content that is intentionally out of v1 scope.

---

## OQ-044 — Intelligence Management trilateral sweep: R20.5→v25.x cross-walk decisions

- **Raised:** 2026-05-08
- **Source page:** wiki/oda/functional-blocks/intelligence-management.md
- **Question:** GB1022 §4.6.1 Table 4-12 (eTOM mapping) and §4.6.2 Table 4-13
  (SID mapping) are sourced from GB921 R20.5 and GB922 R20.5. Cross-walk
  decisions logged for audit.

  **Table 4-12 (eTOM L2) — out of corpus scope:**
    - R20.5 1.1.7, 1.1.12, 1.1.13, 1.1.15 (Market Sales Support & Readiness,
      Market Performance, Sales Performance, Marketing Campaign) — Market/Sales
      Domain not in v1 corpus per CLAUDE.md §3
    - R20.5 1.3.1, 1.3.2 (Customer Support, Customer Experience Management) —
      Customer Domain not in v1 corpus per §3
    - R20.5 1.6.6, 1.6.11 (Party Support, Party Performance Management) —
      Business Partner Domain not in v1 corpus per §3
    - R20.5 1.2.13 Product Test Quality Analysis → v25.5 L3 1.2.1.6 "Analyze
      Product Test Quality" but in **Strategy Management vertical**, out of
      OFAB scope per §3
    - R20.5 1.4.11 Service Test Quality Analysis → v25.5 L3 1.4.1.9 "Analyze
      Service Test Quality", Strategy Management vertical, OOS
    - R20.5 1.5.13 Resource Test Quality Analysis → v25.5 L3 1.5.1.9 "Analyze
      Resource Test Quality", Strategy Management vertical, OOS

  **Table 4-12 (eTOM L2) — resolved to v25.5 (linked):**
    - R20.5 1.2.4 Product Support → v25.5 1.2.4 Product Support Management
      (same ID; slight rename)
    - R20.5 1.2.6 Product Performance Management → v25.5 1.2.6 (same ID, same
      name)
    - R20.5 1.4.4 SM&O Support and Readiness → v25.5 1.4.4 Service Support
      Management (same ID; renamed; same as Production OQ-040 cross-walk)
    - R20.5 1.4.7 Service Quality Management → v25.5 1.4.7 Service Performance
      Management (same ID; renamed Quality→Performance — v25.5 Extended
      Description explicitly references "Service Quality" as a performance
      objective, confirming the lineage)
    - R20.5 1.5.4 RM&O Support and Readiness → v25.5 1.5.4 Resource Support
      Management (same ID; renamed; same as Production OQ-040)
    - R20.5 1.5.9 Resource Performance Management → v25.5 1.5.9 (same ID,
      same name)

  **Note on Support Management L2s.** v25.5 1.2.4 / 1.4.4 / 1.5.4 each appear
  in TWO ODA blocks' mapping tables — Production (Table 4-9 for 1.4.4/1.5.4)
  and Intelligence Management (Table 4-12 for 1.2.4/1.4.4/1.5.4). This is
  consistent with the source-stated "split into 2" guidance in §4.6.1: an L2
  can be realised by multiple ODA blocks where it manages SID ABEs that are
  themselves mapped to different blocks. The reciprocal back-links on the
  Support Management L2 pages will list both Production and Intelligence
  Management.

  **Table 4-13 (SID ABE) — out of corpus scope:**
    - Market/Sales 01 Marketing Campaign, 02 Market Sales Statistics — out of
      scope
    - Customer 01 Customer Statistic — out of scope
    - Business Partner 01 Party Statistic — out of scope
    - Common 01 Party / Party Profile (L2) — no clean v23.0 Common ABE
      successor for the marketing-targeting flavour of "Party Profile" Table
      4-13 references (the v23.0 Party ABE contains PartyRole and Party
      profile concepts, but the source's "Party Profile (L2)" is specifically
      about marketing-segment characteristics; out of scope by content even
      though Party concept itself is in our v23.0 Common). Not linked.

  **Table 4-13 (SID ABE) — resolved (linked):**
    - Product 01 Product Performance ABE → v25.5
      `wiki/sid/product/product-performance-abe` (notFullyDeveloped per OQ-011)
    - Service 01 Service Performance ABE → v25.0
      `wiki/sid/service/service-performance-abe`
    - Resource 01 Resource Performance ABE → v25.5
      `wiki/sid/resource/resource-performance-abe`

  **Pre-existing legacy back-links — preserved with flag:**

    Two Common ABE pages had v1-partial-sweep IM back-links not in Table 4-13:
      - `wiki/sid/common/performance-abe` — NOT in Table 4-13. The inference is
        plausible (Common Performance ABE is the canonical pattern that the
        domain Performance ABEs specialise from; if IM owns the domain
        Performance ABEs, the canonical parent is reasonably IM-related). Not
        directly source-supported. Preserved with flag.
      - `wiki/sid/common/metric-abe` — NOT in Table 4-13. The inference is
        plausible (Metric ABE provides standards of measurement, thresholds,
        metrics — central to performance analytics and Insight Management per
        Table 4-14 #04 "Analytic Models"). Not directly source-supported.
        Preserved with flag.

- **Blocking:** None. Sweep complete for Intelligence Management. Pattern
  consistent with OQ-040/042/043 (R20.5→v25.x cross-walk for both clean
  renames and out-of-scope reorganization, plus legacy v1 back-link
  preservation).

---

_(more open questions will accumulate as further ingestion proceeds)_
