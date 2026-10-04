# Reviewer Training Record (TRR)

The project's record that a reviewer training session happened: the evidence
that mitigates the "resistance to standardized reviews" risk and satisfies a
"training delivered and recorded" gateway criterion. It records one session
of the framework's training material (`TRN`); it holds project data
(stakeholder IDs, dates), so it lives in the project, not in the framework.

- **File:** `docs/sqa/reviewer-training-record.md` (one per project; add a new
  row under `## Attendees and Assessment` and a Version History row for each
  further session).
- **Create:** `new-artifact.sh TRR --file docs/sqa/reviewer-training-record.md
  --cite TRN-001=framework/process/reviewer-training.md`.
- **CrossReference:** `TRN` (the material that was taught).

## Required sections (after Metadata / Version History)

Session (material, date, facilitator, format), Attendees and Assessment
(stakeholder IDs, attended, Pass or Not yet against the assessment in the
material), Feedback, Follow-ups (action, owner as a stakeholder ID, due).
Fill the record after the session; never before.
