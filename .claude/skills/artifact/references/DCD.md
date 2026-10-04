# Design Class Diagram (DCD) (DCD)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **DM** — Concepts each design class refines — names must stay consistent
- **SD** — Messages that become method signatures
- **ERD** — Forward: persistence of the classes' attributes

## Required sections (after Metadata / Version History)

1. **Purpose and Scope**.
2. **Diagram** — PlantUML class diagram: visibility markers (`+` `-` `#`)
   on every member; association vs aggregation vs composition vs dependency
   used per true ownership/lifecycle; multiplicity and navigability on every
   association.
3. **Class Table** — `Class | Refines (Domain Model concept) |
   Responsibility (one sentence) | Attributes | Operations`. SOLID applied;
   no god classes; names consistent with the Domain Model.
4. **Method Traceability** — `Method signature | Operation Contract / SD
   message`; every method traces to one.
5. **Pattern Annotations** — `Pattern | Classes | Rationale`, explicit.
6. **Dependency Check** — note confirming no circular class/package
   dependencies (or an explicit justification).

## Terminology

Class and attribute names are the IT terms from the dictionary (`DICT`), not the PO terms the Domain Model uses.
