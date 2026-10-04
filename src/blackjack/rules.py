"""!
@file rules.py
@brief Blackjack house rules as pure functions; no console input or output.
"""

import random
from collections.abc import Sequence
from enum import Enum

from blackjack.constants import (
    ACE_HIGH,
    ACE_LOW,
    BLACKJACK_MARKER,
    BLACKJACK_SCORE,
    CARDS,
    OPENING_HAND_SIZE,
)


class Outcome(Enum):
    """!
    @brief How a game ended, seen from the player.
    """

    DRAW = "draw"
    WIN = "win"
    WIN_BLACKJACK = "win_blackjack"
    WIN_DEALER_BUST = "win_dealer_bust"
    LOSE = "lose"
    LOSE_DEALER_BLACKJACK = "lose_dealer_blackjack"
    LOSE_BUST = "lose_bust"


def deal_card() -> int:
    """!
    @brief Draw one card from the unlimited deck.
    @return A card value; 11 is the ace and 10 covers 10, Jack, Queen and King.
    """
    return random.choice(CARDS)


def calculate_score(cards: Sequence[int]) -> int:
    """!
    @brief Score a hand.
    @param cards The card values in the hand.
    @return The total, or 0 for a blackjack (two cards: an ace and a 10).
    An ace counts 11 unless that would bust the hand, then it counts 1.
    """
    hand = list(cards)
    total = sum(hand)
    if len(hand) == OPENING_HAND_SIZE and total == BLACKJACK_SCORE:
        return BLACKJACK_MARKER
    while total > BLACKJACK_SCORE and ACE_HIGH in hand:
        hand[hand.index(ACE_HIGH)] = ACE_LOW
        total = sum(hand)
    return total


def compare(user_score: int, computer_score: int) -> Outcome:
    """!
    @brief Decide who won.
    @param user_score The player's score (0 means blackjack).
    @param computer_score The dealer's score (0 means blackjack).
    @return The outcome seen from the player.
    """
    if user_score == computer_score:
        return Outcome.DRAW
    if computer_score == BLACKJACK_MARKER:
        return Outcome.LOSE_DEALER_BLACKJACK
    if user_score == BLACKJACK_MARKER:
        return Outcome.WIN_BLACKJACK
    if user_score > BLACKJACK_SCORE:
        return Outcome.LOSE_BUST
    if computer_score > BLACKJACK_SCORE:
        return Outcome.WIN_DEALER_BUST
    if user_score > computer_score:
        return Outcome.WIN
    return Outcome.LOSE
