"""!
@file test_game.py
@brief Tests for rendering and the console game flow, with scripted input.
"""

import ast
import inspect
import unittest
from collections.abc import Iterator

from blackjack import rules
from blackjack.art import LOGO
from blackjack.constants import (
    CARD_SUITS,
    DEALER_STAND_SCORE,
    MESSAGE_GOODBYE,
    MESSAGE_INVALID_ANSWER,
)
from blackjack.display import format_score, outcome_message, render_hand
from blackjack.game import ask_yes_no, play, play_game
from blackjack.rules import Outcome


class Script:
    """!
    @brief Scripted console: queued answers, queued cards, recorded output.
    """

    def __init__(self, answers: list[str], cards: list[int]) -> None:
        """!
        @param answers The answers the player types, in order.
        @param cards The cards drawn, in order.
        """
        self._answers: Iterator[str] = iter(answers)
        self._cards: Iterator[int] = iter(cards)
        self.output: list[str] = []
        self.clears = 0

    def read(self, prompt: str) -> str:
        """!
        @brief Next scripted answer.
        """
        return next(self._answers)

    def write(self, text: str) -> None:
        """!
        @brief Record a line of output.
        """
        self.output.append(text)

    def draw(self) -> int:
        """!
        @brief Next scripted card.
        """
        return next(self._cards)

    def clear(self) -> None:
        """!
        @brief Count a console clear.
        """
        self.clears += 1

    @property
    def text(self) -> str:
        """!
        @brief All output as one string.
        """
        return "\n".join(self.output)


class TestDisplay(unittest.TestCase):
    """!
    @brief Tests for the rendering helpers.
    """

    def test_render_hand_shows_rank_and_suit(self) -> None:
        """!
        @brief Each card is its rank followed by a suit emoji, joined by spaces.
        """
        self.assertEqual(
            render_hand([11, 10, 7]),
            f"A{CARD_SUITS[0]} 10{CARD_SUITS[1]} 7{CARD_SUITS[2]}",
        )

    def test_format_score_blackjack(self) -> None:
        """!
        @brief Score 0 is shown as Blackjack, other scores as numbers.
        """
        self.assertEqual(format_score(0), "Blackjack")
        self.assertEqual(format_score(17), "17")

    def test_every_outcome_has_a_message(self) -> None:
        """!
        @brief No outcome is left without a message.
        """
        for outcome in Outcome:
            self.assertTrue(outcome_message(outcome))


class TestAskYesNo(unittest.TestCase):
    """!
    @brief Tests for ask_yes_no.
    """

    def test_accepts_yes_and_no(self) -> None:
        """!
        @brief Answers are trimmed and case-insensitive.
        """
        script = Script([" Y ", "N"], [])
        self.assertTrue(ask_yes_no("?", script.read, script.write))
        self.assertFalse(ask_yes_no("?", script.read, script.write))

    def test_repeats_on_invalid_answer(self) -> None:
        """!
        @brief An invalid answer is rejected and the question is asked again.
        """
        script = Script(["maybe", "y"], [])
        self.assertTrue(ask_yes_no("?", script.read, script.write))
        self.assertEqual(script.output, [MESSAGE_INVALID_ANSWER])


class TestPlayGame(unittest.TestCase):
    """!
    @brief Scripted games for each way a game can end.
    """

    def run_game(self, answers: list[str], cards: list[int]) -> tuple[Outcome, Script]:
        """!
        @brief Play one scripted game.
        """
        script = Script(answers, cards)
        outcome = play_game(script.read, script.write, script.draw)
        return outcome, script

    def test_stand_and_win(self) -> None:
        """!
        @brief Stand on 19; dealer draws from 12 to 22 and busts.
        """
        # user 10+9, dealer 10+2, dealer draws 10
        outcome, _ = self.run_game(["n"], [10, 9, 10, 2, 10])
        self.assertEqual(outcome, Outcome.WIN_DEALER_BUST)

    def test_hit_then_bust(self) -> None:
        """!
        @brief Hitting on 16 and drawing a 10 busts; the dealer does not draw.
        """
        # user 10+6, dealer 10+7, user hits 10
        outcome, script = self.run_game(["y"], [10, 6, 10, 7, 10])
        self.assertEqual(outcome, Outcome.LOSE_BUST)
        self.assertIn("Your final hand", script.text)

    def test_player_blackjack_ends_without_prompt(self) -> None:
        """!
        @brief A player blackjack ends the game before any question.
        """
        outcome, _ = self.run_game([], [11, 10, 10, 9])
        self.assertEqual(outcome, Outcome.WIN_BLACKJACK)

    def test_dealer_blackjack(self) -> None:
        """!
        @brief A dealer blackjack ends the game and the player loses.
        """
        outcome, _ = self.run_game([], [10, 9, 11, 10])
        self.assertEqual(outcome, Outcome.LOSE_DEALER_BLACKJACK)

    def test_dealer_draws_until_stand_score(self) -> None:
        """!
        @brief The dealer draws below 17 and stops at 17 or more.
        """
        # user 10+8 stands; dealer 2+3, draws 4 (9), 5 (14), 3 (17)
        outcome, script = self.run_game(["n"], [10, 8, 2, 3, 4, 5, 3])
        self.assertEqual(outcome, Outcome.WIN)
        self.assertIn(f"final score: {DEALER_STAND_SCORE}", script.text)

    def test_draw(self) -> None:
        """!
        @brief Equal final scores are a draw.
        """
        outcome, _ = self.run_game(["n"], [10, 8, 10, 8])
        self.assertEqual(outcome, Outcome.DRAW)


class TestPlay(unittest.TestCase):
    """!
    @brief Scripted end-to-end sessions including restart.
    """

    def test_full_session_with_restart(self) -> None:
        """!
        @brief Two games: hit-and-stand, then a restart answer of no.
        """
        script = Script(
            answers=["y", "y", "n", "y", "n"],
            # game 1: user 5+5, dealer 10+8; user hits 10 (20), stands; dealer stands 18
            # game 2: blackjack for the player
            cards=[5, 5, 10, 8, 10, 11, 10, 10, 9],
        )
        play(script.read, script.write, script.draw, script.clear)
        self.assertEqual(script.clears, 2)
        self.assertEqual(script.text.count(LOGO), 2)
        self.assertIn(outcome_message(Outcome.WIN), script.text)
        self.assertIn(outcome_message(Outcome.WIN_BLACKJACK), script.text)
        self.assertEqual(script.output[-1], MESSAGE_GOODBYE)

    def test_quit_straight_away(self) -> None:
        """!
        @brief Answering no at the first prompt plays no game.
        """
        script = Script(["n"], [])
        play(script.read, script.write, script.draw, script.clear)
        self.assertEqual(script.clears, 0)


class TestRulesAreFreeOfConsoleIo(unittest.TestCase):
    """!
    @brief The rule functions must not read or print.
    """

    def test_no_input_or_print_in_rules(self) -> None:
        """!
        @brief blackjack.rules contains no call to input() or print().
        """
        tree = ast.parse(inspect.getsource(rules))
        called = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        }
        self.assertFalse(called & {"input", "print"})


if __name__ == "__main__":
    unittest.main()
