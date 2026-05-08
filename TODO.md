# TODO — TMF Knowledge Base outstanding work

The v1 corpus is complete. This file tracks remaining work.

**Before picking up any task here:**

1. Read `AGENTS.md` for orientation (current state, working style, ingest workflow)
2. Read `CLAUDE.md` for binding discipline rules
3. Read `wiki/log.md` for ingest worked examples
4. Run `python3 lint/lint.py` — must pass before any new work

The user picks priorities. The order below is recommended, not strict.

---

## 1. Full eTOM ↔ SID ↔ ODA trilateral sweep

**Why:** GB1022 §4.3.3, §4.4.3, §4.5.2, §4.6.2 contain mapping tables that connect
the 6 ODA Functional Blocks to many eTOM L2 processes and SID ABEs. Most of those
mappings are not yet wikilinked because they reference R20.5 IDs (see OQ-037),
and resolving them to v25.x equivalents requires careful per-mapping judgement.
The 16 already-linked reciprocals show the pattern.

**Approach:**

- Read each ODA block's GB1022 mapping tables (`raw/extracted/tmf/oda/GB1022_..._v1.1.0.md`)
- Resolve where unambiguous (e.g. R20.5 "Customer Order Processing Management" → v25.5
  ID 1.3.3 in our corpus — verify against `raw/extracted/tmf/etom/_in_scope_l2_digest.md`
  and the full Excel extract)
- File an open question where uncertain (e.g. R20.5 process moved to a different
  domain in v25.5)
- Don't infer; cite the source mapping in the wikilink context
- Each forward link from an ODA block needs a reciprocal back-link on the target
  SID/eTOM page — the linter enforces bidirectional consistency

**Acceptance:** lint passes; relevant OQ-037 references in ODA pages get reduced or
replaced by concrete wikilinks; the SID and eTOM target pages have reciprocal
ODA Component back-links.

**Estimated scope:** 50–100 reciprocal links across ~30 pages; can be done in
focused batches per ODA block.

---

## 2. GB921 Decomposition PDFs (eTOM narrative depth)

**Why:** Three PDFs in `raw/tmf/etom/` cover Service (217 pp), Resource
(305 pp), Product (304 pp). Current eTOM L2 pages are overview-level from the
Excel master — verbatim IDs, names, Extended Descriptions, and L3 listings. The
PDFs add narrative prose, diagrams, and inter-process relationships. **OQ-035** is
the placeholder for this.

**Approach:**

- One ingest event per PDF (3 events total)
- For each in-scope L2, append a `## Detailed Description` (or similar) section to
  the existing L2 page with verbatim prose from the PDF
- Don't restructure the existing page anatomy; add depth alongside
- Cite source pages: `— GB921F Service Process Decompositions §X, p. NN`

**Acceptance:** the in-scope L2 pages gain narrative content; lint still passes;
log entries record each ingest with sections-skipped notes for any non-in-scope
content in the PDFs.

**Estimated scope:** 8 + 9 + 12 = 29 L2 pages get a new section each; per ingest
event, ~3–4 hours of careful reading and verbatim extraction.

---

## 3. SID BE-level attribute detail (depth per ABE)

**Why:** v1 ingest captured ABE-level overviews (per CLAUDE.md §5.2 v1 granularity
decision). Many ABEs have rich attribute tables and BE definitions in source not yet
in the wiki.

**Specific OQs flagging the largest gaps:**

- **OQ-016** — Calendar ABE (22 pp)
- **OQ-017** — Location ABE (79 pp; complex, with country-specific subtleties)
- **OQ-018** — Root Business Entities ABE (131 pp; foundational, every other SID
  entity inherits from these patterns — high value to deepen)
- **OQ-019** — Metric ABE (110 pp; includes Best Practices for design and
  application)
- **OQ-020** — Project ABE (170 pp; the largest single chapter)
- **OQ-029** — Resource Computing & Software Addendum (~33 pp; high relevance for
  OSS-monolith mapping)

**Approach:**

- Deepen specific ABEs as the user's mapping work demands them — not all at once
- For each, append BE-level detail under the existing `## Business Entities` H2:
  expand the H3 sub-sections with attributes, relationships, figures' content where
  extractable
- Verbatim discipline — copy attribute names exactly, never paraphrase

**Acceptance:** target ABE page has BE-level detail; corresponding OQ can be marked
(by the user) as resolved; lint passes.

---

## 4. User-decision OQs to revisit

These are open questions where the user's input is needed; don't resolve
autonomously. Surface them when relevant to current work or when the user has
bandwidth to review.

- **OQ-013** — `Strategic Product Portfolio Plan` ABE: keep, flag, or remove?
  (sits in Strategy-to-Readiness lifecycle area; partially out of scope per
  CLAUDE.md §3 which excludes the SIP vertical)
- **OQ-021** — `Project` ABE relevance to OSS mapping (170 pp generic project
  management model; intended for organisation-specific extension; uncertain fit
  for OSS-monolith decomposition)
- **OQ-024 + OQ-031** — `Service Problem` and `Resource Trouble` both
  «notFullyDeveloped» in source. Partial blocker for production-side fault
  mapping work; may need supplementation from other TMF documents
- **OQ-030** — `Stock Item` ABE (148 pp, supply chain modelling) relevance to
  typical OSS monolith mapping

**Approach:** when one of these comes up during other work (e.g. doing the
trilateral sweep and hitting the Strategic Portfolio Plan ABE), surface it
concisely with a recommendation. Don't bundle them all into one big "let's resolve
OQs" session unless the user asks.

---

## How to mark something done

- File any new OQs raised during the work
- Append a log entry in `wiki/log.md` per the format defined in
  CLAUDE.md §9
- Run `python3 lint/lint.py` — must pass
- Commit with a descriptive message; end with the standard
  `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>` line per
  the session's git convention
- Update this file: strike through or remove the completed task, or add a "Done"
  note

When a TODO item is fully addressed across all aspects, remove it from this file
(history is in git). When new work emerges, add it here.
