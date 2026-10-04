# Operation Contract (OC)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **SSD** — **Required source**: each contract traces to exactly one SSD message
- **DM** — Classes/associations named in pre/postconditions
- **SD** — Forward: the design realizing each contract's postconditions

## Required sections (after Metadata / Version History)

One block per system operation, each containing:

1. **Operation** — complete signature: name, parameter types, return type
   (must match the SSD message).
2. **Cross References** — the SSD message it traces to (one contract per
   message) and the Domain Model concepts touched.
3. **Preconditions** — required state before execution, expressed in Domain
   Model terms.
4. **Postconditions** — state changes only, in Larman's style: *instance
   created / instance associated / attribute modified*. Declarative ("what"),
   never algorithmic ("how"); avoid vague text like "system processes the
   request".
5. **Exceptions** — error conditions, each with the failing precondition.

## Terminology

Use the IT terms from the dictionary (`DICT`), not the PO terms the Domain Model uses.
