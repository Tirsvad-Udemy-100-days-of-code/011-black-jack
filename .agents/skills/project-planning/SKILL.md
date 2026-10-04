---
name: project-planning
description: Plan a project (or a new phase of one) in phases with tasks, and sync those phases and tasks to Gitea or GitHub as Milestones and Issues. Use when starting a new project, adding or updating a phase/gateway, breaking a phase down into tasks, deciding whether a task needs its own use case or user story, or asked to create/update project milestones or issues on the git host.
---

# Project Planning

Plans a project as phases (gateways), each phase as a set of tasks, and
keeps those phases and tasks in sync with the git host's own project
management (Milestones and Issues). It builds on the `artifact` skill's
`PP` (Project Plan) and `MIL` (Milestone/Gateway) types.

## Domain language first

Before planning, find the Product Owner's (PO's) domain language. Take it from
the first of these that states it:

1. the user's prompt;
2. a file the user included or that the project already has (the `Languages`
   section of `docs/artifact-registry.md`).

If none states it, **ask the user for it** and stop planning until it is
answered; never assume one. Record the answer in the registry's `Languages`
section. If it differs from the project's working language, the high-level
artifacts are also kept in it (see the registry's translation list).

## Start here

Before planning or building anything, check that the baseline exists (the
`docs/artifact-registry.md` rows and files): the Business Case (`BC`), the
Stakeholder Analysis (`SA`), the Project Plan (`PP`) and at least one
milestone (`MIL`). If one is missing, create it first, in that order, with
`new-artifact.sh` (it refuses when a type in the catalog's `Requires` column
is missing).

A "build X" request is planning-first. Produce the phases, tasks and issues,
show the dry run of `sync-project.sh`, and ask for a go-ahead before any code
is written; running `--apply` is the user's decision. Only the user can waive
the plan, in chat, for that request; the waiver does not carry over. The rule
is defined in `framework/process/plan-first-gate.md`.

## The hierarchy

```
Business goal → Feature/requirement → Use case/user story → Tasks
```

The use case/user story explains **why** a feature exists; tasks explain
**how** the team implements it. Not every task needs a use case:

- **Needs a use case/user story** — the task is something a user, or
  another system, actually does: "User resets password", "Admin exports
  customer report", "Payment service processes refund".
- **Plain task, no use case** — purely technical/implementation work:
  "Refactor authentication middleware", "Add database index", "Upgrade
  React version", "Fix null-pointer bug", "Add unit tests", "Configure CI
  pipeline", "Optimize SQL query".

When in doubt, ask: does this row describe a goal an actor is pursuing, or
a step the team takes to build something? Goals get a use case; steps stay
a plain task.

## Use cases get their own folder

Each use case lives in `docs/uc-NNN/` (`UC-001` → `docs/uc-001/`), together
with the artifacts that belong to it. Nothing about a use case goes in a
shared `docs/use-cases/` folder.

1. **Create the folder and the use case:**
   `bash framework/scripts/new-artifact.sh UC --file docs/uc-001/uc.md`.
2. **Create only the artifacts this use case affects,** in this order, each in
   the same folder with a fixed file name. Skip any it does not touch (no
   `erd.md` if nothing is stored; no `dm.md` if it adds no concept).

   | Order | Type | File | Create when the use case… |
   | --- | --- | --- | --- |
   | 1 | `SSD` | `ssd.md` | has system interaction to show (almost always) |
   | 2 | `DM` | `dm.md` | introduces or changes domain concepts |
   | 3 | `OC` | `oc.md` | has system operations that change state |
   | 4 | `SD` | `sd.md` | needs a collaboration design for an operation |
   | 5 | `DCD` | `dcd.md` | adds or changes design classes |
   | 6 | `ERD` | `erd.md` | adds or changes persisted data |

   ```bash
   bash framework/scripts/new-artifact.sh SSD --file docs/uc-001/ssd.md
   bash framework/scripts/new-artifact.sh DM  --file docs/uc-001/dm.md      --cite UC-001=docs/uc-001/uc.md
   ```

   `new-artifact.sh` cites only the artifacts in the same use-case folder
   (and project-level ones); for `DM`, `DCD` and `ERD`, add the use case and
   sibling artifacts by hand with `--cite`. Each gets its own ID (the next
   version in the registry, e.g. `DM-002`) and its own `RC-*` review.
3. **Reconcile with the project models.** The use-case artifacts are a scoped
   view; the project-level `docs/domain-model.md`, `docs/dcd.md` and
   `docs/erd.md` are the consolidated truth. When the use case's `DM`, `DCD`
   or `ERD` are done, compare each with its project-level document:
   - add the new concepts, classes, attributes and entities; change the ones
     the use case modified;
   - keep names identical to the existing ones, and resolve any conflict
     with another use case's model instead of duplicating the element;
   - give each project-level document a new `## Version History` row (Change:
     which use case caused it), and create it from the first use case's
     document if it does not exist yet;
   - if nothing needs to change, say so in the use case's task and PR
     description ("project DM/DCD/ERD unchanged: <reason>").

## Planning a project (or a new phase)

1. **Phases are gateways.** Each phase is a `MIL-*` document (the `artifact`
   skill's `MIL` type): purpose, deliverable, Go/No-Go criteria, dependencies,
   ownership, target date. Create one with
   `bash framework/scripts/new-artifact.sh MIL --file docs/milestones/mil-<NNN>-<slug>.md`.
2. **The plan schedules the phases.** `docs/project-plan.md` (the `artifact`
   skill's `PP` type) lists every phase with its window and owner, and holds
   the overall timeline diagram. Create it once with
   `bash framework/scripts/new-artifact.sh PP`.
3. **Break each phase into tasks.** In the phase's `## Tasks` section, add
   one row per task using the hierarchy rule above. Tasks that need a use
   case or user story get one created first (`UC`/`US` types; a use case
   follows "Use cases get their own folder" below), then are referenced from
   the Tasks row; plain tasks just describe the work.
4. **Sync to the git host.** Run the sync tool (below) to create or update
   the corresponding Milestones and Issues. Do this whenever a phase or its
   tasks change — the tool is idempotent (matches by title, never creates a
   duplicate).

## Syncing to Gitea/GitHub

```bash
bash framework/scripts/sync-project.sh              # prints the plan only — no network calls
bash framework/scripts/sync-project.sh --milestone MIL-002   # limit to one phase
bash framework/scripts/sync-project.sh --apply      # actually create/update on the git host
```

- **Default is a dry run**: it parses `docs/milestones/mil-*.md` and prints
  what would be created or updated. Nothing is sent anywhere.
- **`--apply`** performs the real requests. It needs:
  - **Gitea** (default — detected from `origin`'s hostname): `GITEA_TOKEN`
    env var, a personal access token. This is an HTTP API call (milestones,
    issues) — a deploy key cannot be used, since deploy keys only
    authenticate SSH git transport (clone/fetch/push), not the REST API.
    Scope the token to issues only if your Gitea version supports scoped
    tokens, rather than a full-account one.
  - **GitHub** (detected when `origin` is on github.com, or pass
    `--host github`): the `gh` CLI, already logged in (`gh auth login`).
- **`--with-project`** additionally tries to create/attach a Kanban Project
  board. This is best-effort: some Gitea versions (confirmed on 1.27.3) show
  Projects/Kanban only in the web UI and expose **no REST API for it at
  all**, so this always fails there — check your server's own
  `https://<host>/swagger.v1.json` for any `project` path if unsure. GitHub
  Projects (v2) needs `gh` with the `project` scope. Either way the script
  warns and continues; Milestones and Issues are unaffected. Where there's
  no API, create the board by hand at `https://<host>/<owner>/<repo>/projects`.
- Read the script's header comment for the full flag list, including
  `--owner`, `--repo`, `--api-base` to override auto-detection.

`--apply` is an outward-facing, hard-to-reverse action (it creates real
Milestones/Issues on the git host) — run it yourself once you're ready, or
ask explicitly for it to be run.

## Branching before commits

**Never commit, push or open a PR unless the user asks.** The user reviews
the working-tree changes first; finish the edits, summarise them and stop.
Everything below (branching, closing keywords, resolving commit links, the
PR) describes how to do those steps once the user has asked for them; it is
not permission to start them.

Never commit directly on `main`. This is enforced locally by a pre-commit
hook (`framework/githooks/pre-commit`) once
`bash framework/scripts/install-git-hooks.sh` has been run in this clone —
run it once per clone; it points `core.hooksPath` at the versioned
`framework/githooks/` instead of the per-clone, untracked `.git/hooks/`.
The hook refuses the commit with a pointer back to this section; a rare,
deliberate exception can bypass it with `ALLOW_MAIN_COMMIT=1 git commit`.

Before the first commit of a piece of work, create and switch to a new
branch, then commit there:

```bash
git checkout -b <branch-name>
# ... commits ...
git push -u origin <branch-name>
```

- Name the branch for the gateway/task it covers, kebab-case, e.g.
  `g2-kpi-bmc-bpmn` or `mil-002-kpi-baseline` — short enough to read in a
  PR list, specific enough to say what it's for.
- Open a PR (`gh pr create` on GitHub, or the Gitea equivalent) instead of
  merging straight to `main`; this project's own history is a merged PR
  per phase (e.g. "Merge pull request 'Close G1 inception baseline...'"),
  so keep following that pattern.
- This applies to every commit, not just gateway/task work — if in doubt
  whether the current branch is `main`, check (`git branch --show-current`)
  before committing.

## Closing tasks from commits

When a commit finishes the work for a task that `sync-project.sh` has
already synced as an Issue, reference that Issue number in the commit
message so Gitea/GitHub auto-closes it once that commit lands on the
default branch (`main`) — via the PR merge required by "Branching before
commits" above, not by pushing the closing keyword to a feature branch.
Use `Refs #N` instead when the commit only touches the task without
finishing it — that links the commit without closing.

- **One issue per commit:** use `Closes #5`.
- **Several issues closed by the same commit:** put one `Closes #N` per
  line, not a comma-separated list (`Closes #5, #6, #7` only closed `#5` on
  a confirmed live Gitea instance — the comma form is not reliably parsed):

  ```
  Closes #5
  Closes #6
  Closes #7
  ```
- Get each issue number either from the most recent `sync-project.sh` /
  `sync-project.sh --apply` output (it prints `updated issue #N` /
  `created issue #N` per task) or, if that's not at hand, from the git
  host's issue list for the milestone.
- Match commits to issues by the task row they implement — one task row in
  a `MIL-*` document's `## Tasks` section is one Issue, so a commit that
  completes that row's work closes that Issue.
- Don't guess an issue number; if it isn't known from a recent sync or a
  lookup, ask rather than omit or fabricate one.
- **After pushing a multi-issue closing commit, verify** each issue's state
  came back `closed` (e.g. `GET /repos/<owner>/<repo>/issues/<N>` with
  `GITEA_TOKEN`) rather than assuming the whole list closed; close any that
  didn't with a direct `PATCH .../issues/<N>` `{"state":"closed"}` call.

## Pull requests close the issues they complete

Every PR must close the Issues its work finishes, so the board matches
reality once it merges. Before opening (or updating) a PR:

1. **List the issues the branch completes.** Go through the task rows the
   branch implements (`git log main..HEAD`, plus the `## Tasks` of the
   `MIL-*` it belongs to) and get each Issue number as described in "Closing
   tasks from commits".
2. **Put one closing line per issue in the PR description**, one per line,
   never comma-separated:

   ```
   Closes #5
   Closes #6
   ```

   Use `Refs #N` for an issue the PR only touches. A PR that finishes no
   issue says so explicitly ("No issue closed: <reason>") instead of saying
   nothing.
3. **Ask, don't guess.** If an issue number is unknown or a task is only
   partly done, ask rather than omit or invent one. Leave a partly done task
   open and note what remains.
4. **After the merge, verify** that each issue is `closed` (the check in
   "Closing tasks from commits") and close any stragglers by hand. Also make
   sure the finished task rows are reflected in the `MIL-*` document and, when
   every task of a phase is closed, that the Milestone is closed too.

5. **Resolve pending commit links before the PR** (see "Version History rule"
   in the `artifact` skill): commit, run
   `bash framework/scripts/resolve-pending-commits.sh <changed docs>`, then
   commit the result as a follow-up commit.
6. **Never ask for, offer or perform the merge.** A PR needs a reviewer: ask
   the user to open the PR / request a review, and stop there. Merging,
   enabling auto-merge and "shall I merge?" are not yours to do.

Closing keywords in the PR description and in commit messages both count on
Gitea and GitHub; they only take effect when the PR merges into the default
branch.

## Files this skill touches

- `docs/project-plan.md` — `PP`, via the `artifact` skill.
- `docs/milestones/mil-*.md` — `MIL`, via the `artifact` skill, each with a
  `## Tasks` section.
- `docs/uc-NNN/*.md` (the use case and its `SSD`, `DM`, `OC`, `SD`, `DCD`, `ERD`), `docs/user-stories.md` — only for tasks that need one; plus `docs/domain-model.md`, `docs/dcd.md`, `docs/erd.md` when reconciling.
- `framework/scripts/sync-project.sh` — never edited per project; propose
  changes upstream in the framework.
