# Domain Model (DM)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **UC** — Source of every concept (noun phrases) — cite each `UC-*` used
- **UCD** — Scope check: actors/goals the model must cover
- **SSD** — Forward: system operations that act on these concepts

## Required sections (after Metadata / Version History)

1. **Purpose and Scope** — which use cases the model covers.
2. **Diagram** — PlantUML class diagram (or linked source) showing
   **concepts, attributes and associations only — no operations**.
   Business language throughout ("Sale", not "SaleTable"/"SaleClass").
3. **Concept Table** — `Concept | Definition | Attributes | Source (use
   case noun phrase / glossary)`. Every concept traces to a noun in a use
   case or glossary. Attributes are simple domain data, not foreign-key-like
   references (model those as associations).
4. **Association Table** — `From | Association name (with reading
   direction) | To | Multiplicity (both ends)`. All multiplicities present.
5. **Generalizations** — only true "is-a" relationships, never inheritance
   for code reuse.

## Terminology

Concept names are the PO terms recorded in the dictionary (`DICT`); add a row there for each new concept.
