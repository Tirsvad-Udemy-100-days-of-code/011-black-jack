# KPI Definitions (KPI)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **BC** — The Success Criteria row each KPI is aligned to (`[BC-001]`)

## Required sections (after Metadata / Version History)

1. **Purpose** — which Business Case success criteria this document
   operationalizes.
2. **KPI Definitions** — one row per KPI: `KPI ID | Name | SMART statement |
   Baseline | Target | Business Case Success Criterion | Owner | Frequency &
   Method | Data Source`.
3. **Thresholds** — per KPI: acceptable / at-risk / failing bounds.
4. **Reporting** — where results are reported and to whom.

Rules: every KPI is SMART (reject goals/activities like "improve quality");
baseline *and* target are both present; `Owner` is a stakeholder ID from
the project's Stakeholder Analysis (e.g. `S07`), never free text; give KPIs stable IDs (`KPI-01`, …) so
Milestones can cite them.
