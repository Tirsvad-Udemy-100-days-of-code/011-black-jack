---
name: artifact
description: Create, edit or review any project document artifact — Business Case, Stakeholder Analysis, KPI, Business Model Canvas, BPMN, milestones/gateways, use case diagram, user stories, use cases, domain model, SSD, operation contracts, sequence diagrams, DCD, ERD, ADRs, SQA review records, traceability matrix, governance, QC checklists. Scaffolds the file with the correct ID, CrossReference and links, then gives the required sections for that type.
---

# Artifact

Every artifact is a markdown file with `## Metadata` and `## Version History`
tables, a registered short-name ID, and links only at the bottom. Types and
their related types are in `framework/registry/artifact-catalog.md`; this
project's file locations and next versions are in `docs/artifact-registry.md`.

## Creating an artifact

1. Find the type's short name (`BC`, `SA`, `MIL`, `DM`, `ADR`, `RC`, …) in
   the catalog. If the type is new, add it to the catalog and the registry.
2. Scaffold — this sets the ID, `CrossReference` (only artifacts that exist),
   the bottom link block and the registry version:

   ```bash
   bash framework/scripts/new-artifact.sh <SHORT> [--file <path>] [--title "<text>"] [--cite <ID>=<path>]...
   ```

   `--file` is required for multi-document types (`MIL`, `UC`, `ADR`, `RC`,
   `QC`); single-document types default to the registry's `Primary File`.
   The script refuses to overwrite an existing file.
3. Read `framework/.agents/skills/artifact/references/<SHORT>.md` (cite-for
   hints and required sections), then fill in the file. Keep the sections in
   order and replace every `<placeholder>`.

## Editing an artifact

Append a row to `## Version History` on every change (a status change such as
`Proposed` → `Accepted`, or a content change). To re-check `CrossReference`,
run `bash framework/scripts/find-crossreferences.sh <SHORT>`. When the first
instance of a type is created, add it to the `CrossReference` of every
existing artifact that lists that type as a candidate (with a new Version
History row).

### Version History rule

The table keeps only the **two latest** changes; git holds the rest. Columns:

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-01 | Accepted | Jane Doe | S02 | Added Risks section<br>Fixed scope wording | [a1b2c3d] |

- **Status** — `Proposed`, `Accepted`, `Rejected` or `Deprecated` for every
  artifact type (`ADR` also has `Superseded by ADR-NNNN`); `Approved` is not
  used. A new row starts `Proposed`. When the review gives Go, that row
  becomes `Accepted` and the row before it becomes `Deprecated`, so at most
  one row is `Accepted`: the latest reviewed one. If the reviewer refuses the
  change for good (not a No-Go that returns it for rework), the row becomes
  `Rejected`; the earlier `Accepted` row stays `Accepted` and nothing is
  deprecated.
- **Change** — a short summary of what this row changed; several lines are
  separated with `<br>`.
- **Commit** — the commit that made the change, as a reference-style link
  defined at the bottom of the file
  (`[a1b2c3d]: https://<host>/<owner>/<repo>/commit/<full-hash>`; Gitea and
  GitHub use the same `/commit/` form). A row cannot contain its own commit
  hash, so a new row says `pending` until the commit exists. Leave it
  `pending` and do not commit: only when the user asks for a commit, then:
  1. commit the edited documents;
  2. run `bash framework/scripts/resolve-pending-commits.sh <file>...`, which
     replaces `pending` with the link to that commit and adds the definition;
  3. commit the result as a follow-up commit, before opening the PR. Do not
     amend: an amend changes the hash, so the link would point at a commit
     that is never pushed.
- When adding a third row, delete the oldest row and its now-unused commit
  link definition. Never rewrite the content of the two retained rows other
  than resolving `pending` and setting Status to `Accepted` / `Deprecated`
  after a Go review.
- Every document uses this format, including QC checklists. A file still in the
  old four-column format is converted when next edited (old row kept as
  `Initial version`, plus a new row for the conversion).

## Reviewing an artifact

1. Take the QC checklist named in the catalog (`framework/qc/qc-*.md`).
2. Create the review record: `new-artifact.sh RC …`, following
   `references/RC.md`.
3. Add or update the instance's row in the Traceability Matrix.

## Rules

- **Links:** all links are reference-style, defined once at the bottom of the
  file after a final `---`, labelled by the target's ID (`[SA-001]`), never
  inline. No links → omit the block.
- **CrossReference:** cite only artifacts that exist now. Empty if none.
- **People:** use exact stakeholder IDs from the project's Stakeholder
  Analysis (`S01`) for owners, reviewers and RACI. Never invent role names.
- **Diagrams** are PlantUML blocks; check them with
  `bash framework/scripts/render-diagrams.sh --server <url> <file>` (or set
  `PLANTUML_URL`) before review.
- **QC checklists** are framework files: every criterion is tagged with an
  ISO/IEC 25010:2023 characteristic, and they never mention real instances.
- **IDs:** `<SHORT>-<version>`, 3 digits (`BC-001`); `ADR` uses 4 digits;
  `RC` is sequential across all types; QC is `QC-<SHORT>-<version>`.
- **Language:** artifacts carry no `DomainLanguages` row. The PO language and
  the register of each artifact type are in the `Languages` section of
  `docs/artifact-registry.md` (registers: `IT Executive English` for
  high-level, `IT Professional English` for technical).
- **Translations:** when the PO language is not English, each type the
  registry marks "Also kept as a PO-language file" is also saved as
  `<artifact>.<language>.md` beside its English source (`business-case.da.md`).
  A translation keeps the source's ID and sections, uses the PO terms from the
  dictionary (`DICT`), and has a Version History row naming the source version
  it follows. The English file is authoritative; update the translation in the
  same change. If the PO language is English, no translations are made.
- **Dictionary:** the Domain Model uses the PO term; the Operation Contract,
  Sequence Diagram, Design Class Diagram and ERD use the IT term. Every pair is
  recorded in `docs/dictionary.md` (`DICT`).
