# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [1d35410] |

---

## Purpose

Identify who has an interest in the Blackjack project and what they need, using the power/interest grid. IDs are stable and are cited by all other artifacts.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer, reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Complete the course assignment with a correct game, built and tracked with the planning process |
| S02 | Udemy coursists | Fellow participants of the course who share code | Udemy course community | LOW | MEDIUM | Keep Informed | Readable, runnable code they can compare with their own solution |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear README and a clean structure that gives them ideas to reuse |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts every milestone, writes and reviews the work.
- **Keep Informed (S02):** share and compare solutions; they do not decide anything but benefit from readable code and clear instructions.
- **Monitor (S03):** browse occasionally; no direct communication, they are served by the README and the repository description and topics.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Game behaves per the assignment's house rules | Functionality |
| S01 | Easy to run on a clean machine | Usability / Implementation |
| S01 | Rules can be tested and reviewed | Supportability |
| S02 | Code is readable and follows the assignment's function names | Supportability |
| S02 | Can run the game and tests from the README | Usability |
| S03 | Finds the idea quickly: description, topics, README | Usability |
| S03 | No setup surprises: no runtime dependencies | Implementation |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Pull request review on the git host | Once per milestone | Reviewed milestone deliverable | MIL-001, MIL-002 |
| S02 | Repository, README, source comments | On publication | Runnable game with documented code | MIL-002 |
| S03 | Repository description, topics and README | On publication | Discoverable, understandable repository | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Course hints suggest one flat script; the framework asks for testable, documented modules | S01, S02 | Keep the hint function names (`deal_card`, `calculate_score`, `compare`) but place them in importable modules |
| Coursists want a simple read-through; viewers want a polished project | S02, S03 | Keep modules small with Doxygen comments, and put the overview in the README |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct game | [BC-001] objective 1 |
| S01 | Reviewable, tracked steps | [BC-001] objective 6 |
| S02 | Readable, testable code | [BC-001] objectives 3 and 5 |
| S02, S03 | Run and test instructions | [BC-001] objective 4 |
| S03 | Discoverable repository | [BC-001] objective 4 |

## Sign-Off

Pending review by S01.

---

[BC-001]: ./business-case.md
[1d35410]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/011-blackjack/commit/1d35410b8d29df6c4991a0b9aff24f8509d58a86
