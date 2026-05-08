# Page Templates

These are the working stubs for every wiki page type. The agent copies the appropriate
template, fills in the frontmatter and body, and saves to the correct location per
[[../CLAUDE]] §5.

## Templates

| Page type      | Template              | Wiki location                                                        |
|----------------|-----------------------|----------------------------------------------------------------------|
| etom-l2        | `etom-l2.md`          | `wiki/etom/{domain}/{kebab}.md`                                      |
| sid-abe        | `sid-abe-entity.md`   | `wiki/sid/{product\|service\|resource\|common}/{kebab-entity}.md`    |
| oda-component  | `oda-component.md`    | `wiki/oda/{domain}/{kebab-component}.md`                             |
| foundation     | `foundation.md`       | `wiki/foundations/{kebab-name}.md`                                   |
| view           | `view.md`             | `wiki/views/{kebab-name}.md`                                         |

## Usage discipline

- **Section headings are normative.** Heading text and order match [[../CLAUDE]] §5
  exactly. The linter checks heading text verbatim. Do not rename, reorder, or merge
  required sections.
- **HTML comments are guidance for the agent.** Remove them once the section is filled.
  Lingering comments are not lint errors but indicate incomplete work.
- **Placeholders `{{like-this}}` mark slots.** Replace with verbatim content from raw
  sources. Never commit a page with `{{...}}` still present.
- **Empty bullet `- ` lines mean "fill or file an open question".** Do not leave them
  blank. Either populate with content/wikilinks, or replace with
  `See open-questions.md — OQ-{NNN}`.
- **Frontmatter is YAML.** Keep the field order consistent with the template; the linter
  is lenient on order but consistency aids review.
- **`source_paths` and `source_extract_paths` are lists** — even when there is only one
  source. Use `- ` list syntax.

## When templates conflict with CLAUDE.md

CLAUDE.md wins. Templates are implementations of §5 anatomy; if a template is wrong,
the template is wrong, not CLAUDE.md.
