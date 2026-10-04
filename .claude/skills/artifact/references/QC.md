# Quality Criteria checklist (QC)

A QC checklist is the reusable review checklist for one artifact **type**.
It lives in the framework (`framework/qc/qc-<type>.md`), is
project-independent, and **must never name or link a real artifact
instance** (no `[BC-001]`, no `RC-*`, no stakeholder IDs). Refer to types
generically ("the Stakeholder Analysis").

- **ID:** `QC-<short-name>-<version>` (e.g. `QC-BC-001`); the version starts
  at `001` and only changes when the checklist itself is revised.
- **Create:** `new-artifact.sh QC --id QC-XX-001 --file framework/qc/qc-<type>.md
  --cite QC-<adjacent>=framework/qc/qc-<adjacent>.md ...`
- **CrossReference:** the QC checklists immediately backward and forward in
  Larman's chain, in both directions:

```
QC-SA → QC-BC → { QC-BMC, QC-BPMN, QC-KPI } → QC-MIL
QC-BC, QC-SA → QC-UCD → { QC-US, QC-UC }
QC-UC → QC-DM → QC-SSD → QC-OC → QC-SD → QC-DCD → QC-ERD
QC-ADR ↔ QC-DCD, QC-ERD
QC-DCD, QC-ADR → { QC-PY, QC-CL, QC-CPP, QC-CS }   (language code checklists)
```

## Version History statuses

The statuses are `Proposed`, `Accepted`, `Rejected` and `Deprecated`, as for every
artifact type (rule in the `artifact` skill, "Version History rule").

## Required sections (after Metadata / Version History)

- **Purpose** — why this type matters, what decision it supports.
- **Quality Criteria Checklist** — `# | Criterion | Level | ISO/IEC 25010
  Characteristic(s) | Notes`. `Level` is `Mandatory` (baseline every instance
  must meet) or `Optional` (advanced, may be deferred); a checklist with an
  extra column (e.g. `Format`) keeps `Level` right after `Criterion`. Every criterion is tagged with at least one of
  the eight ISO/IEC 25010:2023 characteristics (Functional Suitability,
  Performance Efficiency, Compatibility, Usability, Reliability, Security,
  Maintainability, Portability). Never add an untagged criterion.
- **Common Defects** — anti-patterns a reviewer rejects on sight.
- **Traceability Rule** — Backward / Forward bullets with the same `[QC-*]`
  labels as `CrossReference`.

Also add an entry to `framework/CHANGELOG.md`. Reviews of real instances are
recorded in the project as `RC-*` records, not in the checklist.
