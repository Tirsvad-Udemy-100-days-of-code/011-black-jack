# @TITLE@

## Metadata
| Key | Value |
| --- | --- |
| ID | @ID@ |
| CrossReference | @CROSSREF@ |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| @DATE@ | Accepted | @AUTHOR@ | <reviewer S-ID> | Initial version | pending |

---

## Purpose

Defines how this project applies Quality Criteria (QC) checklists to real
artifact instances, producing SQA Review Records and Go/No-Go decisions.

## ARB Review Workflow

1. **Submission** — the artifact owner submits an instance for review,
   identifying its type's QC checklist (`framework/qc/qc-*.md`).
2. **QC Checklist Review** — the assigned reviewer (see RACI) applies the
   checklist criterion by criterion.
3. **Review Record** — the reviewer documents the outcome as an SQA Review
   Record (`RC-*` under `docs/sqa/reviews/`).
4. **Go/No-Go Decision** — the Accountable role for the artifact category
   decides; contested or cross-cutting cases escalate to the ARB Chair.
5. **Sign-off** — on **Go**, the artifact's `## Version History` gets an
   `Accepted` row (the previous row becomes `Deprecated`). On **Go-with-conditions**, status stays `Proposed` until
   the Action Items are closed. On **No-Go**, the artifact returns to its
   owner.
6. **Traceability Update** — the Traceability Matrix is updated with the
   instance and its `RC-*` reference.

## RACI by Artifact Category

Fill every cell with stakeholder IDs from the Stakeholder Analysis (`S<NN>`),
never role names.

| Artifact Category | Responsible (runs the review) | Accountable (Go/No-Go owner) | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Strategic (Stakeholder Analysis, Business Case, BMC) | S<NN> | S<NN> | S<NN> | S<NN> |
| Process/Business (BPMN, KPI, Milestones/Gateways) | S<NN> | S<NN> | S<NN> | S<NN> |
| Requirements (Use Case Diagram, User Story, Use Case) | S<NN> | S<NN> | S<NN> | S<NN> |
| Modeling/Design (Domain Model, SSD, Operation Contract, Sequence Diagram, DCD, ERD) | S<NN> | S<NN> | S<NN> | S<NN> |

Cross-cutting escalations and disputed verdicts are Accountable to the ARB
Chair (`S<NN>`), overriding the category-level Accountable role.

## Escalation Rules

- A **No-Go** verdict, or any disagreement between the Responsible reviewer
  and the category's Accountable owner, escalates to the ARB Chair.
- A reviewer may not review an instance they authored.
- Repeated No-Go verdicts (2 or more) on the same artifact type trigger a
  review of the corresponding `QC-*` checklist itself.

## Cadence

- Reviews are triggered per artifact instance as it is produced or revised.
- QC checklists are reviewed annually.

---

@LINKS@
