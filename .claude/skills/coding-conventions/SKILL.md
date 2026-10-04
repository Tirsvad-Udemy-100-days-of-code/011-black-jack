---
name: coding-conventions
description: Programming conventions for writing or reviewing source code — naming, layout, formatting and language idioms — for Python, C, C++, C# and Shell (bash). Use when writing, editing, reviewing or refactoring code in one of those languages, choosing names, setting up a formatter/linter config, or adding conventions for another language. Holds the rules shared by every language and points to a per-language sub-skill.
---

# Coding Conventions

One skill for all languages. This file holds what is true in every language;
everything specific to one language is in a sub-skill that is read only when
that language is in hand:

| Language | Sub-skill | QC checklist |
| --- | --- | --- |
| Python | `references/python.md` | `framework/qc/qc-programming-python.md` (`QC-PY-001`) |
| C | `references/c.md` | `framework/qc/qc-programming-c.md` (`QC-CL-001`) |
| C++ | `references/cpp.md` | `framework/qc/qc-programming-cpp.md` (`QC-CPP-001`) |
| C# | `references/csharp.md` | `framework/qc/qc-programming-csharp.md` (`QC-CS-001`) |
| Shell (bash) | `references/shell.md` | `framework/qc/qc-programming-shell.md` (`QC-SH-001`) |

Read the sub-skill for the language you are working in, then write or review
the code. To review, use the language's QC checklist and record the result as
an `RC-*` (see the `artifact` skill).

## Precondition: a planned task

Before writing or editing code under `src/` or `tests/`, name the task row
(`MIL-NNN`, task N) or the synced issue, and the use case or design artifact
it implements, or say it is a plain technical task. If you cannot, refuse and
use the `project-planning` skill instead (rule: `framework/process/plan-first-gate.md`).
Reviewing code needs no task.

## Rules for every language

1. **The existing code wins.** In a file or project that already has a
   convention, follow it, even if the sub-skill says otherwise. Do not mix
   styles within a file; do not reformat code you are not changing.
2. **Naming follows the language, not your habits.** Casing differs per
   language (table below). Never carry one language's casing into another.
3. **A name says what, not how.** Name by purpose in the domain's language
   (IT Professional English, as the registry's `Languages` section says), not by
   type or implementation (`customer_list`, not `arr2`).
4. **Length follows scope.** Short names (`i`, `n`) only for tiny scopes;
   wider scope, longer name. No abbreviations except ones the whole domain
   uses (`id`, `url`, `http`).
5. **Booleans read as a question:** `is_valid`, `has_items`, `can_retry`
   (cased per language). No negated names (`is_not_ready`).
6. **Functions are verbs, types are nouns.** A function that returns a value
   without side effects may be a noun (`total`, `Total`) where the language
   community does so.
7. **Formatting is done by the formatter,** not by hand and not in review
   comments. Each sub-skill names the formatter and linter; commit its
   configuration file with the code.
8. **Comments say why,** never what the code already says. Public APIs get
   the language's documentation-comment form.
9. **No dead or commented-out code, no unexplained magic numbers.** Name the
   constant.
10. **Errors are handled or propagated, never swallowed.** Each sub-skill says
    how its language does this.

## Casing at a glance

| Element | Python | C | C++ | C# |
| --- | --- | --- | --- | --- |
| Type / class | `PascalCase` | `snake_case_t` | `PascalCase` | `PascalCase` |
| Function / method | `snake_case` | `snake_case` | `snake_case` | `PascalCase` |
| Variable / parameter | `snake_case` | `snake_case` | `snake_case` | `camelCase` |
| Constant | `UPPER_SNAKE` | `UPPER_SNAKE` | `kPascalCase` | `PascalCase` |
| Private member | `_leading` | file-scope `static` | `trailing_` | `_camelCase` |
| Namespace / module | `snake_case` module | `mod_` prefix | `snake_case` | `PascalCase` |
| File | `snake_case.py` | `snake_case.c/.h` | `snake_case.cpp/.h` | `PascalCase.cs` |

The table is a summary; the sub-skill is authoritative. Shell (bash) is not in
the table: functions and variables are `snake_case`, constants and environment
variables `UPPER_SNAKE`, files `kebab-case.sh`.

## Governance boundary

Conventions are **defined and governed** here but **not enforced** by this
framework: writing a linter or CI job that enforces them is outside the
framework's scope. The formatter and linter names in each sub-skill are the
recommended tools, not a pipeline. A new or changed convention follows the
process in the project's Coding Standards Governance document and is recorded
in `framework/CHANGELOG.md`. No project data belongs in this skill.

## Adding a language

1. Add `references/<language>.md` with these sections: Standard base, Naming,
   Formatting, Language rules, Errors, Tests, Tooling.
2. Add `framework/qc/qc-<language>.md` (`QC-<SHORT>-001`) using the `QC` type
   of the `artifact` skill, tagging every criterion with an ISO/IEC 25010:2023
   characteristic and a Level.
3. Add the row to the table above, the casing table, and a row for the
   language in `framework/registry/artifact-catalog.md`; note it in
   `framework/CHANGELOG.md`; run `bash framework/scripts/install-skills.sh`.
