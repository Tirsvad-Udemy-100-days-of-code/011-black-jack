# SQA Review Record (RC)

One record per review of a specific artifact instance against its QC
checklist. Create one for **every** artifact instance in the project.

- **File:** `docs/sqa/reviews/rc-<NNN>-<instance-slug>.md`
- **ID:** `RC-NNN`, sequential across all artifact types (the registry's
  Next Available Version for `RC`).
- **Create:** `new-artifact.sh RC --file docs/sqa/reviews/rc-NNN-<slug>.md
  --cite <INSTANCE-ID>=<instance path> --cite QC-<SHORT>-001=framework/qc/<checklist>.md`

## Required sections (after Metadata / Version History)

- **Artifact Under Review** — links to the instance and to the QC checklist
  used.
- **Checklist Results** — `# | Criterion | Status (Pass/Fail/N-A) |
  Evidence/Notes`, one row per criterion copied from the QC checklist, in
  the same order.
- **Overall Verdict** — Go / Go-with-conditions / No-Go, with rationale.
- **Action Items** — `Action | Owner | Due`. `Owner` is a stakeholder ID from
  the project's Stakeholder Analysis, never a role name. Every `Fail` and
  every condition gets an item.

## After the review

- The reviewer must not be the artifact's author (see governance).
- Add or update the instance's row in the Traceability Matrix, including
  this `RC-*` in "Last Reviewed".
- On **Go**, set the reviewed artifact's latest `## Version History` row to
  `Accepted` and the row before it to `Deprecated` (`Approved` is not a
  status). On Go-with-conditions the status stays `Proposed` until the action
  items are closed. If the change is refused for good, set the row to
  `Rejected` (the earlier `Accepted` row stays).
- Step-by-step narrative: `framework/process/review-checklist-process.md`.
