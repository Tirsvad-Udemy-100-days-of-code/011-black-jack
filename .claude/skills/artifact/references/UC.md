# Use Case (UC)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **UCD** — Actor and use-case names must match it exactly
- **US** — Stories this use case decomposes into
- **SA** — Stakeholders & Interests — cite S-IDs
- **DM** — Forward: concepts derived from this use case's nouns
- **SSD** — Forward: the SSD depicting this use case's main scenario

## Location

`docs/uc-NNN/uc.md`, one folder per use case (create with
`new-artifact.sh UC --file docs/uc-NNN/uc.md`). The artifacts this use case
affects are saved in the same folder; see the `project-planning` skill, "Use
cases get their own folder".

## Required sections (after Metadata / Version History)

Pick the format explicitly (`Format: Brief | Casual | Fully Dressed`) and
state the **scope/level** (summary, user-goal, subfunction). Always: primary
actor, pre/postconditions, goal-perspective wording with no UI or
implementation detail.

- **Brief** — a single paragraph summarizing only the main success scenario.
- **Casual** — informal multi-paragraph narrative; may mention some
  alternate flows.
- **Fully Dressed** — all sections, in order: Scope, Level, Primary Actor,
  Stakeholders and Interests (cite `SA` S-IDs), Preconditions,
  Postconditions (success guarantee), Main Success Scenario (numbered
  steps), Extensions / Alternative Flows (reference `<<include>>` /
  `<<extend>>` use cases), Special Requirements / Business Rules (per step),
  Open Issues.

Title and actor names must match `UCD` and `US` exactly.
