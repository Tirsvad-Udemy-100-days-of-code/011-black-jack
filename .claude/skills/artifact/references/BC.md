# Business Case (BC)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **SA** — Stakeholders section — cite S-IDs instead of re-describing roles
- **BMC** — Cost–Benefit Assessment must agree with its cost/revenue blocks
- **BPMN** — Forward: the process that realizes the objectives
- **KPI** — Success Criteria — each criterion is operationalized by a KPI
- **UCD** — Forward: scope expressed as actors and goals

## Required sections (after Metadata / Version History)

In this order:

1. **Executive Summary** — one paragraph framing the problem and the
   proposed solution.
2. **Methodological and Standards Foundation** — states the methodology
   (e.g. Larman's *Applying UML and Patterns*) and quality standards (e.g.
   ISO/IEC 25002/25010/25019) the rest of the document and downstream
   artifacts are built on.
3. **Problem Statement** — the recurring problems that justify the project.
4. **Business Opportunity** — what becomes possible if the problem is
   solved.
5. **Objectives** — concrete, verifiable statements of what the project
   will achieve.
6. **Scope** — split into `## In Scope` and `## Out of Scope` subsections.
7. **Expected Benefits** — split into `### Tangible Benefits` and
   `### Intangible Benefits`.
8. **Strategic Alignment** — how the project supports organizational goals.
9. **Success Criteria** — a table with explicit, measurable targets (not
   aspirations).
10. **Risks** — a table with `Risk | Impact | Mitigation` columns; every
    risk must have a mitigation.
11. **Assumptions** — bullet list, kept distinct from Constraints.
12. **Constraints** — bullet list, kept distinct from Assumptions.
13. **Cost–Benefit Assessment** — a table (`Costs | Benefits`); may be
    qualitative if explicitly justified.
14. **Stakeholders** — a table referencing exact stakeholder IDs from the
    project's Stakeholder Analysis (e.g. `S01`, `S07`) if `SA` exists per
    the CrossReference check above. **Never re-describe stakeholder roles
    inline instead of citing their IDs** — this is the single most common
    defect found when reviewing Business Cases (see `QC-BC-001`'s Common
    Defects).
15. **Recommendation** — a single, unambiguous "proceed" or "do not
    proceed" statement.
