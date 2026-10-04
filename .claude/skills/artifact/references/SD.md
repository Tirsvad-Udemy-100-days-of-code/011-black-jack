# Sequence Diagram (Design) (SD)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **OC** — **Required source**: the contract whose postconditions each diagram realizes
- **DCD** — Forward: classes/methods these messages become

## Required sections (after Metadata / Version History)

One block per realized Operation Contract:

1. **Realizes** — the contract (`[OC-…]`) and its operation name.
2. **Diagram** — PlantUML sequence diagram: sync (solid filled arrow),
   async (open arrow), returns (dashed); activations matching the call
   nesting; `create` / `destroy` shown for transient objects;
   `loop` / `alt` / `opt` fragments for conditional/repeated behavior.
3. **Pattern Annotations** — table `Pattern (GRASP/GoF) | Applied to |
   Rationale`. Patterns are labelled, never implicit.
4. **Postcondition Coverage** — `Postcondition | Satisfied by message`;
   every postcondition of the contract must be covered.
5. **Responsibility Check** — a short note showing no god-object receives
   all messages (low coupling, high cohesion).

## Terminology

Use the IT terms from the dictionary (`DICT`), not the PO terms the Domain Model uses.
