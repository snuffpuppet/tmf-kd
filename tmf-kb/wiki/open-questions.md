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

_(more open questions will accumulate as further ingestion proceeds)_
