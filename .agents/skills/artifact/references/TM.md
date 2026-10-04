# Traceability Matrix (TM)

One matrix per project: `docs/sqa/traceability-matrix.md`. It makes the
Business Case's cross-artifact traceability target measurable.

## Required sections (after Metadata / Version History)

- **Purpose**.
- **Traceability Table** — one row per artifact instance:
  `Artifact Instance | Type | Upstream (Backward Link) | Downstream (Forward
  Link) | Last Reviewed (RC-ID)`. Add or update a row whenever an instance
  is created or reviewed.
- **Coverage Notes** — which types have no instance yet, and how to read
  `-`: in Upstream it means foundational; in Downstream it means nothing
  is built on it yet; in Last Reviewed it means no `RC-*` exists yet.
