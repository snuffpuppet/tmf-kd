# Lint Rules

This document lists every rule the linter (`lint/lint.py`) checks, with severity and rationale.
For governance see [[../CLAUDE]] §4.3, §5, §6, §7.

## Conventions

- **Severity** is either `error` (blocks ingest completion) or `warning` (visible but
  non-blocking).
- **Page types** are `etom-l2`, `sid-abe`, `oda-component`, `foundation`, `view`.
- **Exempt files** are not subject to frontmatter or anatomy checks. They are: top-level
  `wiki/index.md`, `wiki/log.md`, `wiki/open-questions.md`; the four SID category landing
  pages (`wiki/sid/{product,service,resource,common}-abe.md`); and any `_index.md` file.
- The linter requires PyYAML. Install with `pip install pyyaml`.

## Frontmatter rules

### `FM-MISSING` [error]
**Rule.** Non-exempt wiki pages must begin with a YAML frontmatter block delimited by `---`.
**Why.** Frontmatter declares page type and source provenance; without it, no other check applies.
**Fix.** Add a frontmatter block at the top of the file per [[../CLAUDE]] §6.

### `FM-PARSE` [error]
**Rule.** Frontmatter must be valid YAML parseable by `yaml.safe_load`.
**Why.** Invalid YAML breaks tooling and downstream lint.
**Fix.** Quote strings containing special characters; use `- ` for list entries; check indentation.

### `FM-TYPE` [error]
**Rule.** Frontmatter `type` must be one of: `etom-l2`, `sid-abe`, `oda-component`, `foundation`, `view`.
**Why.** The page type drives every other anatomy and link check.
**Fix.** Set `type:` to a valid value matching the page's intent.

### `FM-FIELD` [error]
**Rule.** All fields required for the page's `type` (per [[../CLAUDE]] §6) must be present.
**Why.** Required fields are the citation contract — a page without them cannot be audited.
**Fix.** Add the missing field. See the relevant template in `templates/`.

### `FM-EMPTY` [error]
**Rule.** Required fields must have a non-empty value.
**Why.** A field with `""` or `null` is the same as no field for the agent's purposes.
**Fix.** Populate the field. If the value is genuinely unknown, file an open question
and note the blocker.

### `FM-LIST` [error]
**Rule.** `source_paths`, `source_extract_paths`, and `derived_from` must be YAML lists,
even if there is only one entry.
**Why.** Consistency simplifies tooling and makes multi-source pages the same shape as
single-source pages.
**Fix.** Use `- ` list syntax; never bare strings.

## Anatomy rules

### `ANAT-SECTION` [error]
**Rule.** Required H2 headings (per [[../CLAUDE]] §5) must be present and in the specified
order. Heading text is matched verbatim.

Required sections per type:

| Type           | Required H2 sections (in order)                                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| etom-l2        | Overview, L3 Processes, SID Entities Manipulated, ODA Components That Realise This Process, Open Questions                                       |
| sid-abe        | Overview, Key Attributes, Relationships, ODA Components That Own This Entity, eTOM Processes That Manipulate This Entity, Open Questions         |
| oda-component  | Overview, Responsibilities, SID Entities Owned, eTOM Processes Realised, Component Dependencies, Open Questions                                  |
| foundation     | Overview, Cross-Framework Application, Open Questions (arbitrary body H2s allowed between Overview and Cross-Framework Application)              |
| view           | Purpose, Source Pages                                                                                                                            |

**Why.** Anatomy is the structural contract that makes pages mechanically auditable.
**Fix.** Restore the missing section, or rename a renamed section back to the canonical text.

### `ANAT-TITLE` [error]
**Rule.** Each page must have exactly one H1 (`#`) title.
**Why.** Multiple titles confuse Obsidian's outline and break indexing assumptions.
**Fix.** Demote extra H1s to H2 or remove them.

### `ANAT-PLACEHOLDER` [warning]
**Rule.** `{{...}}` placeholders inherited from templates should be replaced before commit.
**Why.** A placeholder reaching the wiki indicates incomplete work.
**Fix.** Replace placeholders with verbatim source content, or with a valid `OQ-NNN` reference.

## Trilateral linking rules (eTOM ↔ SID ↔ ODA)

### `TRI-EMPTY` [error]
**Rule.** Each trilateral linking section ([[../CLAUDE]] §7) must contain at least one
wikilink or one `OQ-NNN` reference.

The trilateral sections per type:

| Type           | Trilateral sections                                                            |
|----------------|--------------------------------------------------------------------------------|
| etom-l2        | SID Entities Manipulated, ODA Components That Realise This Process             |
| sid-abe        | ODA Components That Own This Entity, eTOM Processes That Manipulate This Entity |
| oda-component  | SID Entities Owned, eTOM Processes Realised                                    |
| foundation     | (none — foundation pages are exempt)                                           |
| view           | (none — view pages have a different `Source Pages` requirement)                |

The `Component Dependencies` section on `oda-component` pages is **not** a trilateral
section — it is within-ODA navigation and is not enforced by the linter.

**Why.** An empty trilateral section means the page makes a normative claim without
satisfying the cross-referencing discipline.
**Fix.** Add the wikilinks the source establishes, or file an open question and reference it.

### `BI-NO-SECTION` [error]
**Rule.** When page A links to page B in a trilateral section, page B must contain the
reciprocal section (per [[../CLAUDE]] §7) so a return link is possible.
**Why.** Bidirectional consistency depends on both pages having their respective sections.
**Fix.** Add the reciprocal section to page B per its anatomy.

### `BI-MISSING` [error]
**Rule.** When page A links to page B, page B's reciprocal section must contain a return
link to page A.
**Why.** Asymmetric trilateral links produce silently broken graphs.
**Fix.** Add the reciprocal wikilink to page B. If the link from A was a mistake, remove
it from A instead.

## Link integrity rules

### `LINK-BROKEN` [error]
**Rule.** Every `[[wikilink]]` must resolve to an existing wiki page (or `CLAUDE.md`,
`templates/README.md`).
**Why.** Broken wikilinks degrade Obsidian navigation and indicate stale references.
**Fix.** Correct the path, or create the target page if it should exist.

### `SRC-MISSING` [error for `source_paths`, warning for `source_extract_paths`]
**Rule.** Files referenced by `source_paths` and `source_extract_paths` must exist.
**Why.** A wiki claim citing a non-existent source has no traceable authority.
**Fix.** Restore the missing raw file, or correct the path. For extraction paths, rerun
the extraction step.

## Log and open-question rules

### `LOG-MISSING` [error]
**Rule.** `wiki/log.md` must exist.
**Why.** The log is the audit trail; without it the corpus has no provenance history.
**Fix.** Create `wiki/log.md` and append the most recent ingest entry.

### `LOG-STALE` [warning]
**Rule.** When typed wiki pages have been modified after `wiki/log.md`, the log may be
missing the corresponding ingest entry.
**Why.** A wiki edit without a log entry is an undocumented change.
**Fix.** Append a log entry describing the change.

### `OQ-FILE` [error]
**Rule.** `wiki/open-questions.md` must exist.
**Why.** The open-questions register is required infrastructure; the trilateral lint
relies on `OQ-NNN` references resolving to it.
**Fix.** Create the file with at least the standard header.

### `OQ-NOT-FOUND` [warning]
**Rule.** `OQ-NNN` references in pages should correspond to a `## OQ-NNN` entry in
`wiki/open-questions.md`.
**Why.** A dangling OQ reference is either a typo or an open question that was never filed.
**Fix.** File the open question entry, or correct the reference number.

## Future rules (not yet implemented)

The following are deferred until they are needed:

- Validation that `abe_category` matches the file's directory (`wiki/sid/product/...`
  must have `abe_category: product`).
- Validation that `oda_domain` matches the file's directory.
- Validation that `psr_layer` (when present) is one of the documented values.
- Detection of paraphrased canonical names (would require a domain dictionary).
- Cross-version consistency checks when multiple spec versions are tracked.

These are tracked here so they are not lost; they will be added to the linter when the
corresponding discipline becomes load-bearing.
