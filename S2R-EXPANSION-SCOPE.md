# S2R-Vertical Scope Expansion — Planning Document

**Status:** Scoping in progress (Phase 3 of capability map work).
**Initiated:** 2026-05-10 per user direction *"promote it then scope the S2R work."*
**Trigger:** User Phase 1 review question — *"Why is there no 'strategy' and 'capability' verticals?"*
**Source-grounded answer:** They're excluded today by CLAUDE.md §3 ("Strategy / Infrastructure / Product Lifecycle Management (SIP) vertical — strategic, not operational"). v25.5 calls this the **Strategy-to-Readiness (S2R)** Lifecycle Area per GB991 §1.1.2.

This document scopes what it would take to expand the corpus and the capability map to include S2R-area verticals. **Scoping complete — Phase 3 active per 2026-05-10 user sign-off on all five decisions in §10.**

---

## Session State

> _Authoritative resume context for this S2R expansion work. Updated on every state
> transition. A fresh Claude session reads this callout end-to-end before doing anything
> else. Once the new view page `wiki/views/capability-map-s2r.md` exists, Session State
> moves to the top of that page and this document becomes the historical scoping
> artifact only._

- **Last activity:** 2026-05-11 — **BVD batch — second PSR pair landed: 1.4.13 + 1.5.15 Catalog Lifecycle Management.** Both net-new in v25.5 (Original PID = None) — **structural break from BVD pair #1** (1.4.3/1.5.3 had R20.5 lineage); BVD batch is mixed-vintage. Smallest L4 footprint in BVD (3 L3s each, no L4s/L5s). **First PSR pair with completely PSR-agnostic L2 EDs** — both L2 EDs literally identical word-for-word; neither "Service" nor "Resource" appears; v25.5 treats Catalog Lifecycle as a domain-agnostic governance pattern. **Most prominent source-text inconsistency cluster in Phase 3** — six bugs total (three per side): L3 body texts mis-target activity names shifted by one position. **Completes the four-L2 Catalog lifecycle** structurally — all eight catalog anchors (Planning + Lifecycle + Operational Readiness + Content × Service + Resource) now resolve across both view pages; heat-map composability for catalog work fully wired. Both Spec ABEs extended to **five eTOM back-links** each — densest trilateral pattern in corpus extended (primary + capability-delivery + catalog-planning + spec-lifecycle + catalog-implementation-lifecycle). AI-free pattern continues — 7 of 8 PSR pairs AI-free. 14 of 16 S2R L2s now complete. Only Anomaly Lifecycle PSR pair (1.4.17 + 1.5.20) remains to close BVD batch and Phase 3 ingest. Lint: PASS — 145 pages, 0 findings, first try.
- **Refined goal (2026-05-10):** Capability map for **current → target transformation
  roadmap** — monolithic, code-driven BSS/OSS → PSR-driven TMF/eTOM target architecture
  (Nokia OSS). Service + Resource focus, **all vertical groups including S2R**. BVD's
  Specification Lifecycle and Catalog Lifecycle L2s are central to the "build services
  in code → service spec / catalog" transition story; their inclusion is what makes the
  map a transformation artifact rather than an operational gap-only view.
- **Decisions locked (do not relitigate):**
    1. **BVD: INCLUDE.** Full S2R coverage = Strategy Management + Capability Management
       + Business Value Development = **16 new L2s**. Verified against
       `GB921_…_v25.5.xlsx eTOM25,5` sheet (2026-05-10 read): Service Domain has 16
       unique v25.5 L2s (8 already in corpus + 1 Strategy + 4 Capability + 3 BVD = 16
       ✓); Resource Domain has 17 unique v25.5 L2s (9 already in corpus + 1 + 4 + 3 =
       17 ✓; gaps at 1.5.6/11/12/13 captured in the `eTOM Deleted` sheet, not missed).
       L2 inventory in §2 of this document is complete.
    2. **Capability map structure: Option 2C — two view pages.** Existing
       `wiki/views/capability-map.md` stays Operations-area only (17 OFAB L2s, 8 H5
       sub-capabilities, anchors stable, `project/` overlay already wired). New
       `wiki/views/capability-map-s2r.md` carries the 16 S2R L2s with matching anchor
       conventions (`cap-<layer>-<kebab-name>`). Cross-link via top-of-page navigation.
       Composable for the transformation-roadmap story; `project/` overlay can wikilink
       both anchor sets.
    3. **Mermaid: Option 3b — two diagrams, one per Lifecycle Area.** S2R diagram lives
       in the new view page using the same `flowchart TB` template + greying convention
       as the Operations diagram.
    4. **Phasing: Option P1 — pilot first.** Pilot scope: 1.4.1 Service Strategy
       Management + 1.5.1 Resource Strategy Management (paired-PSR; Strategy is the
       simplest of the three new verticals). Review checkpoint after pilot. Then
       Capability Management (8 L2s — heaviest batch); then BVD (6 L2s); then
       L3-derived H5 sub-capability review; then a second `capability-map-s2r.md`
       skeleton/integration pass once content is in place.
    5. **Trilateral verification: incremental.** Per-L2 OQ filing during ingest, same
       pattern as v1 and OFAB L2 ingests. Expect 5–10 new OQs from R20.5 → v25.5 ID
       cross-walks on the ODA side (Original PIDs in v25.5 Excel show the new S2R L2s
       carry R20.5 SIP-vertical numbering — e.g. 1.4.1 was 1.2.2.1).
- **CLAUDE.md §3 amendment:** **APPLIED 2026-05-10T20:00Z.** Surgical rewrite of §3
  → eTOM subsection: two-axis framing (Domain × Lifecycle-Area) anchored to GB991
  §1.1.2; per-Domain × per-Lifecycle-Area in-scope statements (Service + Resource
  both areas; Product Operations-area only); SIP exclusion lifted for S+R, preserved
  as historical note; stale L2-name examples replaced with wikilinks to live
  `_index.md` files; explicit Product-S2R out-of-scope (Phase 4 candidate);
  catch-all out-of-scope for unenumerated branches. SID + ODA subsections
  unchanged. See `wiki/log.md` 2026-05-10T20:00Z entry for full diff and rationale.
- **Conventions inherited from capability-map work (apply forward to S2R ingest):**
    - Verbatim discipline (CLAUDE.md §1, §10.3) — canonical names, IDs, attributes
      copied exactly, including Excel encoding artefacts (`&;` → flag, do not silently
      smooth).
    - Provenance-line convention (Batch 3) — italic line above Scope for documented
      version-renames. *1.4.1 has a rename: v24.0 "Service Strategy & Planning" → v25.5
      "Service Strategy Management". Apply.*
    - Naming-asymmetry convention (Batch 4) — preserve TMF's PSR-asymmetric labels.
      Spot check during S2R: 1.4.1 Service Strategy Management vs 1.5.1 Resource
      Strategy Management — symmetric here, but watch for asymmetry elsewhere
      (especially in BVD: e.g. Anomaly Lifecycle Management).
    - Security-H5 convention (Batch 5) — H5 sub-capability with stable anchor for
      multi-bullet responsibility blocks within an L2.
    - TMF-pure mental-category convention (Batch 5) — organisation-specific groupings
      stay in `project/`, not the wiki.
    - L3-derived sub-capability convention (Phase 2) — H5 sub-capability for named L3
      processes with substantive scope, recognised practitioner concern, cross-PSR
      symmetry. Review scheduled at end of S2R ingest (post-16-L2). Capability
      Management L2s likely candidates given the transformation-roadmap framing.
- **Pilot status:** **COMPLETE 2026-05-10.** Pilot deliverable per Phase 3 phasing
  decision = both pilot L2s + the new view page skeleton + Strategy Management
  vertical populated. All three components landed. Last filed OQ: **OQ-046**
  (S2R-vertical eTOM L2 ODA cross-walk — applies forward to all 16 S2R L2 pages).
- **Conventions recorded during pilot (apply forward to S2R batches):**
    - Cross-PSR navigational wikilinks in trilateral sections (`## SID Entities
      Manipulated`, `## eTOM Processes That Manipulate This Entity`, `## ODA
      Components That…`) trigger bidirectional consistency lint errors per-entity,
      not per-PSR-pair. Use plain prose for cross-PSR navigation in those sections;
      wikilinks elsewhere (L3 anchored, body text outside trilateral sections) are
      unaffected.
    - Lifecycle-area italic line on view-page H4 capabilities — three dimensions
      (eTOM L2 — Vertical — Lifecycle Area) on S2R-area capabilities; the Operations
      sister page elides Lifecycle Area because all its capabilities are in the same
      one.
    - Mermaid `pending` style class for view-page diagrams introduced at pilot —
      `classDef pending fill:#f4f4f4,stroke:#888,color:#666,stroke-dasharray:4 3`.
      All 16 S2R L2 nodes appear in the diagram from day one; `:::pending` is
      removed per node as the L2 ingests.
- **Capability Management batch progress:**
    - ✅ Pair 1: 1.4.2 + 1.5.2 Capability Delivery — done 2026-05-10.
    - ✅ Pair 2: 1.4.12 + 1.5.14 Capacity Management — done 2026-05-10.
    - ✅ Pair 3: 1.4.16 + 1.5.18 Catalog Planning Management — done 2026-05-11.
    - ✅ Pair 4: 1.4.19 + 1.5.19 Specification Management — done 2026-05-11.
    - **BATCH COMPLETE.**
- **BVD batch progress:**
    - ✅ Pair 1: 1.4.3 + 1.5.3 Specification Lifecycle Management — done 2026-05-11.
    - ✅ Pair 2: 1.4.13 + 1.5.15 Catalog Lifecycle Management — done 2026-05-11.
    - ⏳ Pair 3: 1.4.17 + 1.5.20 Anomaly Lifecycle Management — next, closes BVD +
      Phase 3 ingest entirely.
- **AI-distribution pattern crystallised after Capability Management closes.** 4 PSR
  pairs without AI references on either side (Capacity Management, Catalog Planning,
  Specification Management — 3 of 4 Capability Management pairs) vs 2 PSR pairs with
  Resource-side AI (Strategy Management, Capability Delivery). Pattern: v25.5 AI
  commentary is concentrated in Strategy + Capability Delivery, absent from the rest
  of Capability Management. **BVD batch test:** likely Specification Lifecycle
  (1.4.3/1.5.3) and Catalog Lifecycle (1.4.13/1.5.15) follow the AI-free pattern;
  Anomaly Lifecycle (1.4.17/1.5.20) is the wildcard.
- **Cross-L2 linkages established within Capability Management:**
    - Capability Delivery → Capacity (capability-shortfalls input flow) on both PSR
      sides; both ABEs carry two back-links (primary capacity-mgmt + upstream-input
      capability-delivery).
    - Capability Delivery + Catalog Planning + Specification Management → Specification
      ABE (three-back-link triad on both PSR sides, densest pattern in corpus).
    - Catalog Planning → Specification Management (back-reference resolution within
      same SID ABE — Catalog Planning leverages Specification Management activities).
    - Cross-domain handoff: Service Capability Delivery (1.4.2.1) → Resource Capability
      Delivery (1.5.2.1) for resource-requirements pass-through.
- **Four-L2 Catalog lifecycle visible across both view pages.** Planning (S2R-CM) +
  Lifecycle (S2R-BVD, pending) + Operational Readiness (Ops-ORS) + Content (Ops-ORS).
  Heat-map composability wired via anchored cross-page wikilinks. Load-bearing
  transformation-roadmap callout.
- **Specification-ABE three-back-link triad** on both PSR sides. Densest trilateral
  pattern in the corpus, reflecting that Specification ABEs are central data-model
  artefacts touched by multiple Capability Management activities at different scopes.
- **Next action:** Propose **1.4.17 + 1.5.20 Anomaly Lifecycle Management** — third
  and final BVD PSR pair; closes BVD batch and Phase 3 ingest. After ingest: L3-
  derived sub-capability review closes Phase 3 entirely. The Anomaly pair pairs
  with the Operations-area Anomaly Management H4s already in the sister capability
  map — both pages will then carry full Anomaly story (Lifecycle S2R-BVD + the
  pre-existing 1.4.18/1.5.21 Operations-area assurance Anomaly L2s).
- **No pending decisions.** Phase 3 ingest at 14 of 16 S2R L2s (88% complete); BVD
  has 2 of 3 PSR pairs done. Four-stage Catalog lifecycle now structurally complete
  (Planning + Lifecycle + Operational Readiness + Content all wired). Five-back-
  link densest-pattern extended on both Spec ABEs.
- **Pending decisions:** _(none — the five primary decisions are locked. The CLAUDE.md
  §3 amendment text is a derived artefact awaiting drafting and sign-off, not a separate
  scope decision.)_

---

## 1. Goal

Add the **Strategy Management** and **Capability Management** verticals (and optionally **Business Value Development** — see Decision 1 below) to the Service and Resource Domain coverage in the corpus and capability map, enabling heat-map / roadmap analysis of strategic-planning and capability-delivery maturity alongside the current operational-only view.

The user's stated goal remains operational OSS-mapping, but Phase 1 surfaced practitioner curiosity about strategic / capability layers — this scope expansion serves stakeholders who need a fuller process-maturity view (e.g. roadmap planning, capability-investment decisions) rather than just the operational gap analysis.

---

## 2. L2 inventory — source-grounded

Direct read from `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` (2026-05-10 survey). Service Domain (1.4.x) and Resource Domain (1.5.x) only.

### Strategy Management vertical — 2 L2s

| ID | Name | Domain |
|---|---|---|
| 1.4.1 | Service Strategy Management | Service |
| 1.5.1 | Resource Strategy Management | Resource |

### Capability Management vertical — 8 L2s

| ID | Name | Domain |
|---|---|---|
| 1.4.2 | Service Capability Delivery | Service |
| 1.4.12 | Service Capacity Management | Service |
| 1.4.16 | Service Catalog Planning Management | Service |
| 1.4.19 | Service Specification Management | Service |
| 1.5.2 | Resource Capability Delivery | Resource |
| 1.5.14 | Resource Capacity Management | Resource |
| 1.5.18 | Resource Catalog Planning Management | Resource |
| 1.5.19 | Resource Specification Management | Resource |

### Business Value Development vertical — 6 unique L2s

GB991 §1.1.2 groups Business Value Development under the same S2R Lifecycle Area as Strategy and Capability Management. Decision 1 below: include or defer.

| ID | Name | Domain |
|---|---|---|
| 1.4.3 | Service Specification Lifecycle Management | Service |
| 1.4.13 | Service Catalog Lifecycle Management | Service |
| 1.4.17 | Service Anomaly Lifecycle Management | Service |
| 1.5.3 | Resource Specification Lifecycle Management | Resource |
| 1.5.15 | Resource Catalog Lifecycle Management | Resource |
| 1.5.20 | Resource Anomaly Lifecycle Management | Resource |

(Note: 1.5.5 Resource Order is also flagged BVD by GB921 v25.5 alongside Fulfillment + ORS — already in corpus scope.)

### Totals

| Scope option | Verticals | New L2 pages |
|---|---|---|
| Minimal (Strategy + Capability) | 2 | 10 |
| Full S2R (Strategy + Capability + BVD) | 3 | 16 |

---

## 3. SID ABE situation — already largely in corpus

Survey (2026-05-10) of existing `wiki/sid/{service,resource,product,common}/` ABE pages against keywords *Strategy*, *Capability*, *Specification*, *Capacity*, *Plan*:

| ABE | Status | Path |
|---|---|---|
| Service Strategy and Plan | **Already ingested** | `wiki/sid/service/service-strategy-and-plan-abe.md` |
| Resource Strategy and Plan | **Already ingested** | `wiki/sid/resource/resource-strategy-and-plan-abe.md` |
| Service Specification | **Already ingested** | `wiki/sid/service/service-specification-abe.md` |
| Resource Specification | **Already ingested** | `wiki/sid/resource/resource-specification-abe.md` |
| Product Specification | **Already ingested** | `wiki/sid/product/product-specification-abe.md` |
| Product Offering Specification | **Already ingested** | `wiki/sid/product/product-offering-specification-abe.md` |
| Service Capacity | **Already ingested** | `wiki/sid/service/service-capacity-abe.md` |
| Resource Capacity | **Already ingested** | `wiki/sid/resource/resource-capacity-abe.md` |
| Product Capacity | **Already ingested** | `wiki/sid/product/product-capacity-abe.md` |
| Common Capacity | **Already ingested** | `wiki/sid/common/capacity-abe.md` |
| Strategic Product Portfolio Plan | **Already ingested** | `wiki/sid/common/strategic-product-portfolio-plan-abe.md` |

**Reason:** SID coverage in CLAUDE.md §3 is by ABE category (Product / Service / Resource / Common), not by vertical alignment. The Strategy/Capability ABEs were ingested at v1 because they're Service/Resource Domain ABEs.

**Likely missing:** Capability-specific ABEs (e.g. *Service Capability Plan*, *Resource Capability Plan* — these may exist in GB922 v25.5 but may not have been called out in the v1 ingest). Verification needed; estimated 0–4 new ABE pages.

**Net SID ingest burden: low** — most of the data-layer support already exists.

---

## 4. CLAUDE.md amendments needed

### §3 — In Scope / Out of Scope

Current text (eTOM section):
> Out of scope:
> - The **Strategy / Infrastructure / Product Lifecycle Management (SIP) vertical** — this is strategic, not operational. The goal is mapping operational processes.

Proposed amendment options:

**Option A — Scoped expansion (recommended for Strategy + Capability):**
> In scope (Phase 3 expansion 2026-05-10):
> - **Strategy Management** lifecycle stage of S2R: provides strategic planning view aligned with operational mapping.
> - **Capability Management** lifecycle stage of S2R: bridges strategic planning to operational readiness via capability delivery, capacity management, and specification management.
>
> Out of scope (still excluded):
> - **Business Value Development** lifecycle stage of S2R — lifecycle/version-management of catalog and specification artifacts; defer pending stakeholder need.

**Option B — Full S2R inclusion (if BVD included):**
> In scope (Phase 3 expansion 2026-05-10):
> - **Strategy-to-Readiness (S2R) Lifecycle Area** — Strategy Management, Capability Management, and Business Value Development lifecycle stages.
>
> Out of scope: _(no remaining S2R-area exclusions for Service and Resource Domains.)_

### §3 — Vertical naming nomenclature

Current text references "OFAB verticals." After expansion this becomes ambiguous (OFAB is Operations area; new verticals are S2R area). Add a clarifying note:
> **OFAB** = Operations Readiness & Support, Fulfillment, Assurance, Billing — the four lifecycle stages of the **Operations** area (per GB991 §1.1.2). The Phase 3 expansion adds lifecycle stages from the **Strategy-to-Readiness (S2R)** area. "Vertical" is the GB991 term for a lifecycle stage; "Lifecycle Area" is the higher-level grouping (S2R or Operations).

### §1.1.2 reference

Update §3 to reference the GB991 §1.1.2 lifecycle structure (already documented in `wiki/foundations/lifecycle.md`) so the scope decision is anchored in the source's own framework.

---

## 5. Capability map integration — structural choices

### Decision 2 — How to organize the capability map after expansion

The current capability map structure:
```
## Service Domain — L2 Capabilities (in scope)
### Operations Readiness & Support
### Fulfillment
### Assurance
### Billing

## Resource Domain — L2 Capabilities (in scope)
### Operations Readiness & Support
### Fulfillment
### Assurance
### Billing
```

Three options for the expanded structure:

**Option 2A — Flat verticals (preserve current pattern):**
Add new H3 sections under each L1 Domain. Service Domain gets 6–7 H3s (Strategy Management, Capability Management, optional BVD, ORS, Fulfillment, Assurance, Billing). Resource same.
- Pros: minimal restructure; consistent with current organization.
- Cons: visual clutter; no Lifecycle-Area distinction; reader doesn't see the S2R/Operations split that GB991 establishes.

**Option 2B — Lifecycle-Area subgrouping (recommended):**
Introduce H2-level Lifecycle-Area split or H3 lifecycle headers.
```
## Service Domain — L2 Capabilities (in scope)

### Strategy-to-Readiness Lifecycle Area
#### Strategy Management
[L2s as H4 capabilities]
#### Capability Management
[...]
#### Business Value Development (if Decision 1 = include)
[...]

### Operations Lifecycle Area
#### Operations Readiness & Support
[...]
#### Fulfillment
[...]
#### Assurance
[...]
#### Billing
[...]
```
But this pushes capabilities to **H5**, sub-capabilities (security, workforce, inventory, test) to **H6**. Obsidian outline gets deep; may break heat-map readability.

**Option 2C — Two view pages (capability map split):**
Keep `capability-map.md` as Operations-only (current state). Create new `capability-map-s2r.md` for the Strategy + Capability + (BVD) verticals. Cross-link both. Heat map can be built on each independently or combined externally.
- Pros: keeps current capability map clean for the operational-OSS use case; isolates the new content; simpler structure per page.
- Cons: practitioner has two pages to navigate; cross-PSR comparisons within Capability Management require cross-page reading; Mermaid diagram doesn't show full picture in one place.

### Decision 3 — Mermaid diagram strategy

Current diagram: 3 top-level subgraphs (Out of scope greyed; Service Domain in scope; Resource Domain in scope), each containing OFAB-vertical sub-subgraphs.

For Option 2A or 2B: subgraphs grow significantly. With 16 added L2s + the 17 existing, Mermaid `flowchart TB` may render unmanageably wide or tall. Consider:
- **3a:** Add new subgraphs but accept visual size growth.
- **3b:** Two diagrams (Operations + S2R), one per Lifecycle Area.
- **3c:** Replace flowchart with a more compact representation (e.g. Mermaid `gantt`-style swim lanes, or table-based).

---

## 6. Capability sub-capability (H5) review

The L3-derived sub-capability convention (settled at capability-map Phase 2) requires fresh L3 review for the new L2s. Likely candidates worth surveying:

- **Capability Delivery (1.4.2 / 1.5.2)** L3s — may carry sub-processes worth heat-map separation (e.g. capability planning vs capability deployment).
- **Capacity Management (1.4.12 / 1.5.14)** L3s — capacity planning is a distinct practitioner concern.
- **Specification Management (1.4.19 / 1.5.19)** L3s — specification design vs specification publishing may merit separate cells.

Effort: similar to Phase 2 — survey all L3s in the new L2s, apply the L3-derived sub-capability criteria (named L3, substantive scope, recognised practitioner concern, cross-PSR symmetry).

---

## 7. Trilateral linking — ODA Functional Block ownership

The existing capability map deliberately omits trilateral inline (framing decision #5). But the new L2 ingest still needs trilateral linking on each L2 page (eTOM-l2 type carries required `## SID Entities Manipulated` and `## ODA Components That Realise This Process` sections).

Likely ODA-block ownership for the new L2s (verification needed against GB1022):
- **Engagement Management** — likely owns Strategy Management L2s (engagement is upstream of strategy).
- **Core Commerce Management** — possibly owns some Capability Management L2s related to product/service portfolio.
- **Production** — possibly owns Capability Delivery / Capacity Management given operational-readiness adjacency.
- **Intelligence Management** — possibly owns Strategy Management's analytics / forecasting functions.

OQ-038 / OQ-040 / OQ-042 / OQ-043 / OQ-044 cross-walk decisions from the v1 trilateral sweep apply: GB1022 may reference R20.5 IDs that need translation to v25.5. Expect 5–10 new OQs filed during ingest.

---

## 8. Effort estimate

Broken down by sub-task. Conservative estimates assuming careful verbatim source extraction and bidirectional trilateral linking.

| Sub-task | Strategy + Capability (10 L2s) | Full S2R (16 L2s) |
|---|---|---|
| **CLAUDE.md amendment** | 1–2 hr | 1–2 hr |
| **L2 page ingest** (verbatim source extraction, full anatomy) | 6–8 hr | 9–12 hr |
| **L3 detail / Extended Description deepening** (per TODO #2 pattern) | 3–4 hr | 5–6 hr |
| **SID ABE verification + any missing ingest** | 1–3 hr | 1–3 hr |
| **Trilateral sweep** (forward links from new L2s + reciprocal ODA back-links) | 2–4 hr | 3–6 hr |
| **Capability map integration** (10–16 new H4 entries, structural decisions, Mermaid update) | 2–3 hr | 3–5 hr |
| **L3-derived sub-capability review** (Phase 2 pattern) | 1–2 hr | 2–3 hr |
| **Lint cleanup throughout** | 1 hr | 1–2 hr |
| **Total** | **17–27 hr** | **25–39 hr** |

For comparison: capability-map Phases 1–2 (Batches 1–6 + L3 review) took ~6 conversation iterations of ~2–3 hours each = ~12–18 hours of iterative collaboration.

---

## 9. Phasing options

### Option P1 — Pilot first (recommended)

Start with the 2 Strategy Management L2s (1.4.1 + 1.5.1) only:
- Smallest scope to validate the workflow.
- Surfaces L1 frame and Mermaid restructure decisions early.
- Produces a small but complete artifact for stakeholder review.
- ~6–8 hours of work.
- If pilot lands cleanly, expand to Capability Management (8 L2s); then optionally BVD.

### Option P2 — Full Strategy + Capability in one pass

10 L2s, 17–27 hours. Produces a complete S2R-pair view (excluding BVD). Recommended if the user has stakeholder pressure for the full picture.

### Option P3 — Full S2R in one pass (Strategy + Capability + BVD)

16 L2s, 25–39 hours. Most comprehensive. Recommended if BVD is genuinely needed for stakeholder use cases.

---

## 10. Decisions needed from user

1. **Include Business Value Development (BVD) vertical?**
   - Yes → 16 L2s, full S2R coverage.
   - No → 10 L2s, Strategy + Capability only.
   - Defer (scope BVD as Phase 4 later) → 10 L2s now, BVD a future TODO.

2. **Capability map structural choice (see §5):**
   - 2A flat verticals (simple, may be cluttered).
   - 2B Lifecycle-Area subgrouping (clean structure, deeper heading levels — capabilities at H5).
   - 2C two view pages (clean separation, two artifacts to navigate).

3. **Mermaid diagram strategy (see §5):**
   - 3a single growing diagram.
   - 3b two diagrams per Lifecycle Area.
   - 3c restructure to compact representation.

4. **Phasing (see §9):**
   - P1 pilot (2 L2s) → expand on success.
   - P2 full Strategy + Capability in one pass (10 L2s).
   - P3 full S2R (16 L2s).

5. **ODA trilateral verification approach.** Expect 5–10 new OQs from R20.5→v25.5 cross-walk. OK with that, or want a clean trilateral sweep first to baseline?

---

## 11. Recommendation

**Decision 1: Include BVD** (full S2R coverage). Reasoning: GB991 §1.1.2 groups all three under S2R Lifecycle Area; partial inclusion creates an awkward gap in the lifecycle view; BVD's scope (Specification Lifecycle, Catalog Lifecycle, Anomaly Lifecycle) is conceptually paired with Capability Management's specification/catalog work — splitting them feels artificial.

**Decision 2: Option 2C — two view pages.** Reasoning: keeps the current `capability-map.md` clean for the user's primary OSS-operational use case (heat-map overlay against the Operations area). New `capability-map-s2r.md` carries the Strategy-to-Readiness content with its own frame, anchors, and (likely simpler) Mermaid diagram. Cross-link the two via top-of-page navigation. Avoids deepening heading levels in the existing capability map; avoids visual diagram bloat.

**Decision 3: Option 3b — two Mermaid diagrams.** Reasoning: matches the two-page split. Each page's diagram stays compact and focused.

**Decision 4: Option P1 — pilot first.** Reasoning: 16 L2s in one pass is a long-running effort; pilot validates the structural choices (Decisions 2 & 3) early. Pilot scope: 2 Strategy Management L2s (1.4.1 Service Strategy Management + 1.5.1 Resource Strategy Management). 6–8 hours. After pilot lands and is reviewed, expand to Capability Management, then BVD.

**Decision 5: Trilateral verification incremental.** File OQs as they arise during ingest; treat the trilateral sweep as part of the ingest (per the v1 pattern), not a precondition.

---

## 12. Next step (after user review of this document)

If the user approves the recommendations above:
1. Amend CLAUDE.md §3 per Option A.
2. Begin the pilot — ingest 1.4.1 Service Strategy Management as the first new L2 page. This single ingest exercises the full workflow (verbatim source extraction → L2 page → frontmatter → Source Pages → trilateral sections → SID/ODA back-references → lint).
3. Pause for user review.
4. If pilot lands clean, ingest 1.5.1 Resource Strategy Management.
5. Pause again.
6. Begin capability-map-s2r.md skeleton with the 2 Strategy Management capabilities.
7. Pause again — review the structural choices in practice, refine if needed.
8. Then expand to Capability Management (8 more L2 ingests).
9. Then BVD (6 more).
10. Throughout: capability-map-s2r.md fills in batch by batch like the original capability map; final L3-derived sub-capability review at the end.

---

## Document state

Prepared 2026-05-10 during capability-map Phase 3 scoping. Status: awaiting user review of decisions in §10. No corpus content modified yet — scoping only.
