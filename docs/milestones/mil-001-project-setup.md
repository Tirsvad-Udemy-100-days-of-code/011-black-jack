# Gateway 1 - Project Setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project foundation (repository metadata, layout, tooling, documentation skeleton) is ready so that game code can be added on top of it.

## Deliverable

A repository with `src/`, `tests/`, `docs/`, a `pyproject.toml` (Python 3.13+, no runtime dependencies), `constants.py`, a Python `.gitignore`, a `Doxyfile`, a `README.md` that documents the local `.venv` and the pip upgrade, and a repository description with topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .` works in a fresh `.venv` on Python 3.13+ | Succeeds | Fails |
| 2 | `python -m unittest` runs (with at least one smoke test) | Exit code 0 | Non-zero |
| 3 | `doxygen Doxyfile` runs | No errors | Errors |
| 4 | README documents venv creation, `python -m pip install --upgrade pip`, run and test | All present | Any missing |
| 5 | Repository has a description and topics | Visible on the git host | Missing |
| 6 | `.env` is git-ignored and not referenced by any file under `src/` or `tests/` | True | False |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4, 5 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-06 - within the two-evening effort assumed in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add repository description and topics | Set a one-line description and topics (python, blackjack, udemy, 100-days-of-code, cli-game) on the git host repository through its API, using the token from the local `.env`. The `.env` file is for personal use only and is never imported, tested or committed. | No | |
| 2 | Create project layout and pyproject.toml | Create `src/`, `tests/` and a `pyproject.toml` that requires Python 3.13 or newer, defines the package under `src/`, has no runtime dependencies and configures the unittest entry. Verify the existing Python `.gitignore` covers `.venv/` and `.env`. | No | |
| 3 | Add constants module | Create `constants.py` with the deck list `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`, the blackjack target 21, the dealer stand threshold 17, the ace values and the emoji card faces, so no magic numbers appear in game code. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` that reads `src/`, writes to `docs/doxygen/`, and extracts Python documentation from Doxygen-style comments. | No | |
| 5 | Write README with venv and run/test instructions | Write `README.md` (standard layout) with description, requirements, creating and activating a local `.venv`, `python -m pip install --upgrade pip`, installing the project, running the game, running the tests and generating Doxygen documentation. | No | |
| 6 | Add smoke test for package import | Add one unittest that imports the package, so the test command is proven to work before any game logic exists. | No | |

---

[BC-001]: ../business-case.md
