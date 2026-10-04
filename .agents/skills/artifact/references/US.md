# User Story (US)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **UCD** — The story's role must match an actor defined here
- **UC** — The use case each story traces to
- **BC** — Objective / epic the story ultimately supports
- **MIL** — The gateway (epic) each story delivers — one or more stories per gateway

## Required sections (after Metadata / Version History)

1. **Purpose and Scope** — the epic(s) covered.
2. **Story List** — each story with a stable ID `US-<doc-version>.<NN>` (e.g.
   `US-001.01`, so it cannot be confused with the document ID `US-001`):
   - Statement: **As a** `<actor>`, **I want** `<goal>`, **so that**
     `<benefit>` — one goal per story, no implementation detail.
   - **Acceptance Criteria** — clear and testable (Given/When/Then works).
   - **Traces to** — the use case (`UC-…`) or epic it comes from; a gateway
     (`MIL-…`) is an epic.
   - **Size** — fits a single iteration.
3. **INVEST Check** — one line confirming Independent, Negotiable,
   Valuable, Estimable, Small, Testable (flag any exception with reason).
