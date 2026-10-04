# Entity Relationship Diagram (ERD) (ERD)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **DCD** — **Required source**: classes/attributes each entity persists; data types must match

## Required sections (after Metadata / Version History)

1. **Purpose and Scope**.
2. **Diagram** — PlantUML entity diagram with PK/FK marked on every entity and
   cardinality (1:1, 1:N) on every relationship; N:M relationships resolved
   through explicit junction entities.
3. **Entity Table** — per entity: `Attribute | Type | PK/FK | Nullable |
   Source (DCD class.attribute)`. Types consistent with the DCD; consistent
   naming, no implementation-specific abbreviations.
4. **Relationship Table** — `Entity | Cardinality | Entity | FK | Rule`.
5. **Normalization Notes** — 3NF confirmed; any denormalization documented
   with its performance justification.

## Terminology

Entity and column names follow the IT terms from the dictionary (`DICT`), not the PO terms the Domain Model uses.
