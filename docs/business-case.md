# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

This project delivers a console Blackjack game written in Python as the first capstone of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp* (day 11). The player plays against a computer dealer under simple house rules, using emoji playing cards. The project doubles as a worked example of the SQA/QC framework: a small, fully planned, tested and documented Python 3.13+ code base that is easy to review.

## Methodological and Standards Foundation

The work follows the project's SQA and QC framework (artifact-first, plan-first gate, review records per artifact). Quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Source code follows the framework's Python coding conventions and is documented with Doxygen comments.

## Problem Statement

The course assignment asks for a complete program that combines functions, lists, loops, conditionals and user input. Without a plan, the work is easily done as one unstructured script that is hard to test, review or reuse, and that loses the course's learning value.

## Business Opportunity

A small, well-structured game shows the full delivery chain (plan, tracked issues, branches and pull requests, tests, generated documentation) on a problem that is simple enough to finish quickly. The result can be reused as a template for the remaining capstone projects.

## Objectives

1. Implement Blackjack for one player against a computer dealer following the house rules below.
2. Render cards as emoji and show the course's ASCII logo at the start of every game.
3. Separate game rules (pure functions) from console input/output so the rules can be unit-tested.
4. Provide a reproducible local setup (venv, `pyproject.toml`) and run/test instructions.
5. Document the source with Doxygen comments and ship a `Doxyfile`.
6. Track every step as a milestone, issue and pull request on the project's git host.

House rules: unlimited deck, no jokers, Jack/Queen/King count 10, Ace counts 11 or 1, drawn cards are not removed, the computer is the dealer and draws while its score is below 17, a two-card Ace + 10 hand is a blackjack.

## Scope

### In Scope

- Game logic: `deal_card`, `calculate_score`, `compare`, dealer play, game loop and restart prompt.
- Emoji card rendering and the logo from the assignment.
- Project scaffolding: `src/`, `tests/`, `docs/`, `pyproject.toml`, `constants.py`, Python `.gitignore`, `Doxyfile`, `README.md`.
- Unit tests for the rules and the console flow (with scripted input).
- Git host housekeeping: repository description and topics.

### Out of Scope

- Splitting, doubling down, insurance, betting and multi-player.
- Graphical or web user interface; network play.
- Packaging for PyPI or any deployment.
- Runtime third-party dependencies.

## Expected Benefits

### Tangible Benefits

- A working, tested console game that matches the assignment's behaviour.
- A reusable project skeleton and documentation set.

### Intangible Benefits

- Practice of planning-first delivery with traceable issues and pull requests.
- Confidence in the Python tooling chain (venv, pyproject, tests, Doxygen).

## Strategic Alignment

The project supports the owner's goal of completing the 100 Days of Code course while building a public portfolio of repositories that follow one consistent, reviewable quality process, shared with fellow coursists and useful as an idea source for GitHub visitors.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Functional suitability: the house rules behave as specified | 100 % of rule unit tests pass | `python -m unittest` exit code 0 |
| 2 | Maintainability: rules are testable without console I/O | `calculate_score`, `compare` and `deal_card` contain no `input()`/`print()` calls | Code review |
| 3 | Portability: runs on Python 3.13+ with no runtime dependencies | `pyproject.toml` lists zero runtime dependencies | Inspection of `pyproject.toml` |
| 4 | Usability: documentation lets a new user run and test the game | Setup to first game in under 5 minutes following the README only | Walkthrough on a clean clone |
| 5 | Maintainability: source documentation is generated | `doxygen Doxyfile` completes without warnings | Doxygen log |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Emoji cards render badly in some Windows terminals | Cards unreadable, poor usability | Document a UTF-8 capable terminal; keep the card symbols in `constants.py` so they are easy to change |
| Randomness makes tests flaky | Unreliable tests | Patch `random.choice` or inject the card source in tests |
| Scope creep (betting, splitting) | Late delivery | Out of Scope list; changes need a new milestone |
| Secrets in `.env` leak into the repository | Credential exposure | `.env` is git-ignored and is never imported or tested by the project |

## Assumptions

- The Product Owner and sole developer is stakeholder `S01`.
- The repository is public, so coursists (`S02`) and viewers (`S03`) can read it.
- The git host is `git.tirsystem.com`, organisation `Tirsvad-Udemy-100_days_of_code`.
- Python 3.13 or newer is installed locally.

## Constraints

- Python 3.13+ and a venv-based workflow; `pyproject.toml` for configuration.
- Constants live in `constants.py`; layout is `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- Nothing is committed, pushed or merged without the owner's request; work is done on branches and pull requests.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About two evenings of developer time (qualitative: learning project, no budget) | Completed capstone, reusable skeleton, practised process |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns scope and acceptance; takes the course, builds and reviews the game |
| S02 | Fellow coursists who share code and compare solutions |
| S03 | GitHub viewers who browse the repository for ideas |

## Recommendation

Proceed - the scope is small, the rules are fully specified by the assignment and the risks are cheap to mitigate.

---

[SA-001]: ./stakeholder-analysis.md
