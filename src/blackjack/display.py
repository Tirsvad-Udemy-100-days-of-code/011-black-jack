"""!
@file display.py
@brief Turns cards, scores and outcomes into text for the console.
"""

from collections.abc import Sequence

from blackjack.constants import (
    BLACKJACK_MARKER,
    CARD_RANKS,
    CARD_SUITS,
    LABEL_BLACKJACK,
    MESSAGE_DRAW,
    MESSAGE_LOSE,
    MESSAGE_LOSE_BUST,
    MESSAGE_LOSE_DEALER_BLACKJACK,
    MESSAGE_WIN,
    MESSAGE_WIN_BLACKJACK,
    MESSAGE_WIN_DEALER_BUST,
)
from blackjack.rules import Outcome

_OUTCOME_MESSAGES: dict[Outcome, str] = {
    Outcome.DRAW: MESSAGE_DRAW,
    Outcome.WIN: MESSAGE_WIN,
    Outcome.WIN_BLACKJACK: MESSAGE_WIN_BLACKJACK,
    Outcome.WIN_DEALER_BUST: MESSAGE_WIN_DEALER_BUST,
    Outcome.LOSE: MESSAGE_LOSE,
    Outcome.LOSE_DEALER_BLACKJACK: MESSAGE_LOSE_DEALER_BLACKJACK,
    Outcome.LOSE_BUST: MESSAGE_LOSE_BUST,
}


def render_hand(cards: Sequence[int]) -> str:
    """!
    @brief Show a hand as emoji cards.
    @param cards The card values in the hand.
    @return The emoji faces separated by spaces.
    """
    return " ".join(
        f"{CARD_RANKS[card]}{CARD_SUITS[index % len(CARD_SUITS)]}"
        for index, card in enumerate(cards)
    )


def format_score(score: int) -> str:
    """!
    @brief Show a score for the player.
    @param score A score from calculate_score (0 means blackjack).
    @return The number, or the blackjack label.
    """
    return LABEL_BLACKJACK if score == BLACKJACK_MARKER else str(score)


def outcome_message(outcome: Outcome) -> str:
    """!
    @brief Message announcing how the game ended.
    @param outcome The outcome seen from the player.
    @return The text to show.
    """
    return _OUTCOME_MESSAGES[outcome]
