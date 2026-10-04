# System Sequence Diagram (SSD) (SSD)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **UC** — **Required source** of every SSD: cite the use case (name and ID) it depicts
- **DM** — Concepts behind message parameters / returned values
- **OC** — Forward: contract per system operation shown

## Required sections (after Metadata / Version History)

1. **Source Use Case** — name and ID (`[UC-…]`) and the specific scenario.
2. **Diagram** — PlantUML sequence diagram with just the actor and
   `:System`; **no internal objects**. Dashed return arrows for operations
   that produce a result. One scenario per diagram — separate diagrams for
   alternate/exception flows (or state them out of scope).
3. **System Operations Table** — `Step | Message (verb phrase) | Parameters
   | Return | Use case step`. Messages match the use case's main success
   scenario step-for-step; justify any deviation. Message names become the
   Operation Contract names.
4. **Lifecycle Notes** — creation/destruction of the System instance where
   relevant (session/transaction scope).
