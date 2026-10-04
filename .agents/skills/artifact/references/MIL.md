# Milestone / Gateway (MIL)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **BC** — The objective / constraint (e.g. project duration) the milestone traces to
- **KPI** — The KPI IDs evaluated at this gate
- **US** — Forward: the user stories (`US-<v>.<NN>`) that deliver this gateway

## Required sections (after Metadata / Version History)

1. **Purpose** — what decision this gate supports.
2. **Deliverable** — the concrete, tangible output evaluated (never just a date).
3. **Go / No-Go Criteria** — objectively checkable, one per row.
4. **Dependencies** — other milestones that must precede this one.
5. **Traceability** — the Business Case objective and/or KPI ID(s) it maps to.
6. **Ownership** — owner and approving reviewer as `SA` stakeholder IDs.
7. **Target Date** — consistent with Business Case constraints.
8. **Tasks** — the implementation-level breakdown for this phase, one row
   per task: `# | Task | Summary | Needs its own Use Case/User Story? |
   Reference`. `Task` is a short title (becomes the Issue title on sync);
   `Summary` is one to three sentences of real context — what the task
   actually involves and why, grounded in this project's own documents, not
   a restatement of the title — so someone reading the Issue on Gitea/GitHub
   understands it without opening this file (becomes the Issue body).

## Breaking a phase into tasks

Not every task needs a use case — only model one when the task is something
a user, or another system, actually does:

- **Needs a use case/user story** — "User resets password", "Admin exports
  customer report", "Payment service processes refund". Set the column to
  `Yes` and put the `US-…`/`UC-…` ID in Reference.
- **Plain task, no use case** — "Refactor authentication middleware", "Add
  database index", "Upgrade React version", "Fix null-pointer bug", "Add
  unit tests", "Configure CI pipeline", "Optimize SQL query". Set the column
  to `No` and leave Reference blank, or point at the design artifact it
  implements (`DCD-…`, `OC-…`).

The hierarchy is: Business goal → Feature/requirement → Use case/user story
→ Tasks. The use case explains *why* a feature exists; tasks explain *how*
the team implements it — most tasks stay at that level.

## Syncing to Gitea/GitHub

Each `MIL-*` gateway becomes one Milestone on the git host; its `## Tasks`
row become Issues assigned to that milestone. Use the `project-planning`
skill and `framework/scripts/sync-project.sh` — do not create these by hand.
