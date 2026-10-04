# Use Case Diagram (UCD)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **SA** — Each actor traces to a stakeholder need — cite S-IDs
- **BC** — Scope / objectives the boundary reflects
- **US** — Forward: stories whose role must match an actor here
- **UC** — Forward: the use cases detailing each goal shown

## Required sections (after Metadata / Version History)

1. **Purpose and Scope** — the system boundary in words.
2. **Diagram** — actors with correct stereotypes (`<<Actor>>`,
   `<<System>>`), a labelled system boundary, `<<include>>` / `<<extend>>`
   used per UML 2.5.1 (not as generic "uses"). Embed PlantUML or link the
   diagram source; no UI or implementation detail.
3. **Actor Table** — `Actor | Stereotype | Stakeholder ID (SA) | Goals
   (use cases)`. No orphan actors: every actor appears in at least one use
   case.
4. **Use Case Table** — `Use Case | Actor(s) | Goal`, names as **verb
   phrases describing actor goals** ("Place Order"), not system operations
   ("Validate Input").
5. **Relationships** — every `<<include>>` / `<<extend>>` with a one-line
   justification.
