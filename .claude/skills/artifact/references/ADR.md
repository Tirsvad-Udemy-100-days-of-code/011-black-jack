# Architecture Decision Record (ADR)

Files: `docs/adr/adr-NNNN-kebab-case-title.md`. `NNNN` is 4-digit and
sequential; the ID is `ADR-NNNN` and must match the filename number (an
intentional exception to the usual 3-digit IDs). Use
`new-artifact.sh ADR --file docs/adr/adr-NNNN-title.md`.

Cite in `CrossReference` the artifacts this decision is about (pass each
with `--cite <ID>=<path>`); ADR has no fixed candidate list.

## Required sections (after Metadata / Version History)

- **Context** — the problem, the options evaluated and the forces
  (cost, risk, constraints).
- **Decision** — the outcome in one or two sentences, no hedging.
- **Consequences** — two bold labels, **Positive:** and **Negative:**, each
  with a bullet list.
- **Affected Artifacts** — other artifacts impacted, as `[ID]` links, or a
  single `-` if none.

Allowed statuses: `Proposed`, `Accepted`, `Rejected`, `Deprecated`,
`Superseded by ADR-NNNN`; no others (an ADR is never `Approved`). Status
changes (`Proposed` → `Accepted` → `Deprecated` / `Superseded by ADR-NNNN`, or
`Proposed` → `Rejected`) are new rows in `## Version History` (only the two
latest are kept; earlier ones stay in git); never rewrite a retained row.
