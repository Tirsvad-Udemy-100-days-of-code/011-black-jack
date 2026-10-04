# Stakeholder Analysis (SA)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **BC** — Business Case objectives each stakeholder concern traces to (Business Goal Alignment section)

## Required sections (after Metadata / Version History)

1. **Purpose** — why the analysis exists and the methodology it follows.
2. **Stakeholder Summary Table** — `ID | Name | Role/Title | Organization |
   Power Level | Interest Level | Quadrant | Primary Concern (Business
   Language)`. Every row fully filled; no unclassified stakeholder.
3. **Power/Interest Classification Rationale** — narrative per quadrant,
   consistent with the table.
4. **Primary Concerns and FURPS+ Mapping** — each concern in business
   language *and* mapped to a FURPS+ attribute.
5. **Communication Requirements** — channel, frequency, deliverable type,
   tied to a project phase or milestone.
6. **Conflicting Interests and Mitigations** — every conflict has a
   mitigation.
7. **Traceability Analysis** — stakeholder → actor/use case mapping, and
   business-goal alignment citing Business Case (`[BC-001]`) objectives.
8. **Sign-Off**.

Stakeholder IDs (`S01`, `S02`, …) are **stable: never renumbered or reused**.
Every other artifact cites them for RACI, ownership and review assignment
(`AGENTS.md` rule 3). Add new stakeholders with the next free `S<NN>`.
