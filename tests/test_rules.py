"""!
@file test_rules.py
@brief Unit tests for the house rules in blackjack.rules.
"""

import unittest
from unittest.mock import patch

from blackjack.constants import CARDS
from blackjack.rules import Outcome, calculate_score, compare, deal_card


class TestDealCard(unittest.TestCase):
    """!
    @brief Tests for deal_card.
    """

    def test_returns_card_from_deck(self) -> None:
        """!
        @brief Every draw is a card of the deck.
        """
        for _ in range(200):
            self.assertIn(deal_card(), CARDS)

    def test_uses_random_choice_on_the_deck(self) -> None:
        """!
        @brief The card comes from random.choice over the deck constant.
        """
        with patch("blackjack.rules.random.choice", return_value=7) as choice:
            self.assertEqual(deal_card(), 7)
        choice.assert_called_once_with(CARDS)

    def test_deck_is_not_consumed(self) -> None:
        """!
        @brief Drawing does not remove cards from the deck.
        """
        before = list(CARDS)
        for _ in range(50):
            deal_card()
        self.assertEqual(CARDS, before)


class TestCalculateScore(unittest.TestCase):
    """!
    @brief Tests for calculate_score.
    """

    def test_normal_total(self) -> None:
        """!
        @brief A plain hand scores the sum of its cards.
        """
        self.assertEqual(calculate_score([2, 3, 9]), 14)

    def test_blackjack_scores_zero(self) -> None:
        """!
        @brief Ace plus 10 in two cards is a blackjack, in either order.
        """
        self.assertEqual(calculate_score([11, 10]), 0)
        self.assertEqual(calculate_score([10, 11]), 0)

    def test_three_card_21_is_not_blackjack(self) -> None:
        """!
        @brief 21 with more than two cards is a normal 21.
        """
        self.assertEqual(calculate_score([7, 7, 7]), 21)

    def test_ace_counts_one_when_hand_would_bust(self) -> None:
        """!
        @brief An ace drops from 11 to 1 when the total exceeds 21.
        """
        self.assertEqual(calculate_score([11, 5, 10]), 16)

    def test_two_aces(self) -> None:
        """!
        @brief Two aces score 12: one counts 11, the other 1.
        """
        self.assertEqual(calculate_score([11, 11]), 12)

    def test_only_needed_aces_are_demoted(self) -> None:
        """!
        @brief Aces drop one at a time, only until the hand no longer busts.
        """
        self.assertEqual(calculate_score([11, 11, 9]), 21)

    def test_bust(self) -> None:
        """!
        @brief A hand over 21 without aces keeps its total.
        """
        self.assertEqual(calculate_score([10, 10, 5]), 25)

    def test_does_not_change_the_hand(self) -> None:
        """!
        @brief Scoring leaves the caller's list unchanged.
        """
        hand = [11, 5, 10]
        calculate_score(hand)
        self.assertEqual(hand, [11, 5, 10])


class TestCompare(unittest.TestCase):
    """!
    @brief Tests for compare, in the order of the house rules.
    """

    def test_equal_scores_draw(self) -> None:
        """!
        @brief Equal scores are a draw, also two blackjacks.
        """
        self.assertEqual(compare(18, 18), Outcome.DRAW)
        self.assertEqual(compare(0, 0), Outcome.DRAW)

    def test_dealer_blackjack_loses(self) -> None:
        """!
        @brief A dealer blackjack beats the player.
        """
        self.assertEqual(compare(20, 0), Outcome.LOSE_DEALER_BLACKJACK)

    def test_user_blackjack_wins(self) -> None:
        """!
        @brief A player blackjack wins.
        """
        self.assertEqual(compare(0, 20), Outcome.WIN_BLACKJACK)

    def test_user_bust_loses(self) -> None:
        """!
        @brief A player over 21 loses.
        """
        self.assertEqual(compare(22, 18), Outcome.LOSE_BUST)

    def test_user_bust_loses_even_when_dealer_busts(self) -> None:
        """!
        @brief The player's bust is checked before the dealer's.
        """
        self.assertEqual(compare(23, 25), Outcome.LOSE_BUST)

    def test_dealer_bust_wins(self) -> None:
        """!
        @brief A dealer over 21 loses.
        """
        self.assertEqual(compare(15, 24), Outcome.WIN_DEALER_BUST)

    def test_higher_score_wins(self) -> None:
        """!
        @brief Otherwise the higher score wins.
        """
        self.assertEqual(compare(19, 18), Outcome.WIN)
        self.assertEqual(compare(17, 20), Outcome.LOSE)


if __name__ == "__main__":
    unittest.main()
