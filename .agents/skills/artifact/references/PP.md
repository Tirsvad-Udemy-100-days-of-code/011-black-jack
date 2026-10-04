# Project Plan (PP)

One per project: `docs/project-plan.md`. Schedules the phases (`MIL-*`
gateways) over the Business Case's timeline/duration constraint.

Cite in `CrossReference` only if the instance exists (`new-artifact.sh`
checks this for you):

- **BC** — the duration/constraint and objectives the plan schedules against
- **SA** — the communication cadence (e.g. sync frequency) the phase length follows
- **MIL** — every phase gateway the plan schedules (add each as it is created)
- **US** — the gateway user stories, once they exist

## Required sections (after Metadata / Version History)

1. **Purpose** — what the plan schedules and over what constraint.
2. **Planning Assumptions** — start date, phase length, any resolved
   conflicts the phasing follows (cite `SA`/`BC` where relevant).
3. **Gateway Schedule** — one row per phase: `Gateway | Document | Window |
   Decision date | Owner | Stories | Main deliverable | Milestone`. One row
   per `MIL-*`. `Milestone` links to that phase's Gitea/GitHub Milestone once
   `sync-project.sh` has created it (see "Phases, tasks and the git host"
   below); leave it blank until then.
4. **Timeline diagram** — a PlantUML Gantt chart, one bar per phase plus a
   milestone marker per Go/No-Go decision.
5. **Scope Coverage** — maps each Business Case scope item to the gateway
   that delivers it.
6. **Dependencies** — the gateway order (usually a simple chain) and what a
   No-Go does to later dates.
7. **Plan Risks** — risks specific to the plan (schedule slip, dependency
   risk), separate from the Business Case's own Risks table.
8. **Open Issues** — anything unresolved (start date to confirm, ambiguous
   targets, missing checklists needed by a later phase).

## Phases, tasks and the git host

Each phase is a `MIL-*` gateway document (see `references/MIL.md`), which
also holds that phase's task breakdown in its own `## Tasks` section. The
Project Plan does not repeat the tasks — it only lists the phases and their
schedule, plus a link to each phase's Milestone once synced (see above). Use
the `project-planning` skill to break a phase into tasks and sync phases (as
Milestones) and tasks (as Issues) to Gitea/GitHub:

```bash
bash framework/scripts/sync-project.sh              # dry run — prints the plan, no network calls
bash framework/scripts/sync-project.sh --apply      # creates/updates Milestones and Issues
```

`--apply` needs a token: `GITEA_TOKEN` (Gitea, a personal access token — not
a deploy key) or `gh auth login` (GitHub). `GITEA_TOKEN` can come from a
`.env` file at the project root (copy `.env.example`, never commit it). If
`.env` is missing or has no token when a sync is needed, ask the user for
one and create `.env` from `.env.example` with it rather than skipping the
sync or inventing a value.

After a real `--apply` run, copy each Milestone's URL into the Gateway
Schedule's `Milestone` column (a content update, not a status change — it
does not need a new `## Version History` row).

## Validating

`PP` has no QC checklist yet (open item) — validate a plan against the
Business Case constraint it schedules and against `## Go / No-Go Criteria`
in each `MIL-*` it lists, rather than a dedicated checklist.
