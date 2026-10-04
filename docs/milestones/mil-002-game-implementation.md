# Gateway 2 - Game Implementation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [1d35410] |

---

## Purpose

Decide whether the Blackjack game is complete, correct under the house rules and ready to be played from the console.

## Deliverable

A runnable console game (`python -m blackjack` from the activated venv) with emoji cards and the course logo, a unit-test suite covering the rules, and Doxygen comments on all public functions.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Unit tests for `deal_card`, `calculate_score` and `compare` cover every house rule | All pass | Any fail |
| 2 | An Ace + 10 two-card hand scores 0 (blackjack); an Ace is demoted from 11 to 1 when the hand exceeds 21 | Verified by test | Not verified |
| 3 | The dealer draws while its score is below 17 | Verified by test | Not verified |
| 4 | A scripted full game (hit, stand, restart answer) runs to the end without error | Passes | Fails |
| 5 | Rule functions contain no `input()` or `print()` calls | True | False |
| 6 | `doxygen Doxyfile` documents every public function | No warnings | Warnings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the layout, constants, tooling and test runner |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2, 3 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-11 - five days after the setup gateway, within the Business Case effort estimate.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement deal_card | Return a random card from the deck constant using `random.choice`. The deck is unlimited and cards are never removed, so each draw is independent. Add a Doxygen comment and unit tests with `random.choice` patched. | No | |
| 2 | Implement calculate_score | Sum a list of cards, return 0 for a two-card Ace + 10 blackjack, and replace an 11 with 1 while the total exceeds 21. Pure function without console I/O; unit-tested for blackjack, bust, multiple aces and normal totals. | No | |
| 3 | Implement compare | Take user and computer scores and return the outcome: draw on equal scores, user loses on dealer blackjack or user bust, user wins on user blackjack or dealer bust, otherwise the higher score wins. Check order follows the assignment's hint 13. | No | |
| 4 | Render emoji cards and logo | Convert card values to emoji faces (suit emoji with the card rank) from the constants, and print the course logo from `art.py` at the start of each game. Keep rendering separate from the rules. | No | |
| 5 | Implement dealer play and game loop | Deal two cards each, show hands, let the user hit or stand until bust, blackjack or stand, then let the dealer draw while below 17, compare and print the result. Console input and output sit in one module that calls the pure rule functions. | No | |
| 6 | Implement restart prompt and console clear | After each game ask whether to play again; on yes clear the console and start a new game, on no exit cleanly. Handle invalid answers by asking again. | No | |
| 7 | Add scripted end-to-end test | Run a full game with `input` and `random.choice` patched, covering hit, stand, bust, blackjack and restart, and assert the printed outcome. | No | |
| 8 | Add Doxygen comments and generate docs | Ensure every public module, function and constant has a Doxygen comment, run `doxygen Doxyfile` and fix any warnings. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-project-setup.md
[1d35410]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/011-black-jack/commit/1d35410b8d29df6c4991a0b9aff24f8509d58a86
