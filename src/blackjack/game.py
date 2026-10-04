"""!
@file game.py
@brief Console game flow: one game, the restart loop and console clearing.
"""

import os
from collections.abc import Callable

from blackjack.art import LOGO
from blackjack.constants import (
    ANSWER_NO,
    ANSWER_YES,
    BLACKJACK_MARKER,
    BLACKJACK_SCORE,
    DEALER_STAND_SCORE,
    MESSAGE_GOODBYE,
    MESSAGE_INVALID_ANSWER,
    OPENING_HAND_SIZE,
    PROMPT_HIT,
    PROMPT_RESTART,
)
from blackjack.display import format_score, outcome_message, render_hand
from blackjack.rules import Outcome, calculate_score, compare, deal_card

## Reads one answer from the player.
type Reader = Callable[[str], str]
## Shows one line to the player.
type Writer = Callable[[str], None]
## Draws one card.
type Draw = Callable[[], int]


def clear_console() -> None:
    """!
    @brief Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def ask_yes_no(prompt: str, read: Reader, write: Writer) -> bool:
    """!
    @brief Ask until the player answers yes or no.
    @param prompt The question to show.
    @param read Reads the player's answer.
    @param write Shows a message to the player.
    @return True for yes, False for no.
    """
    while True:
        answer = read(prompt).strip().lower()
        if answer == ANSWER_YES:
            return True
        if answer == ANSWER_NO:
            return False
        write(MESSAGE_INVALID_ANSWER)


def play_game(read: Reader, write: Writer, draw: Draw) -> Outcome:
    """!
    @brief Play one game: the player draws, then the dealer, then compare.
    @param read Reads the player's answers.
    @param write Shows text to the player.
    @param draw Draws one card.
    @return The outcome seen from the player.
    """
    user_cards = [draw() for _ in range(OPENING_HAND_SIZE)]
    computer_cards = [draw() for _ in range(OPENING_HAND_SIZE)]
    computer_score = 0
    user_score = 0
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        write(
            f"   Your cards: {render_hand(user_cards)}, "
            f"current score: {format_score(user_score)}"
        )
        write(f"   Dealer's first card: {render_hand(computer_cards[:1])}")
        if (
            user_score == BLACKJACK_MARKER
            or computer_score == BLACKJACK_MARKER
            or user_score > BLACKJACK_SCORE
        ):
            is_game_over = True
        elif ask_yes_no(PROMPT_HIT, read, write):
            user_cards.append(draw())
        else:
            is_game_over = True

    is_user_bust = user_score > BLACKJACK_SCORE
    while (
        not is_user_bust
        and computer_score != BLACKJACK_MARKER
        and computer_score < DEALER_STAND_SCORE
    ):
        computer_cards.append(draw())
        computer_score = calculate_score(computer_cards)

    write(
        f"   Your final hand: {render_hand(user_cards)}, "
        f"final score: {format_score(user_score)}"
    )
    write(
        f"   Dealer's final hand: {render_hand(computer_cards)}, "
        f"final score: {format_score(computer_score)}"
    )
    outcome = compare(user_score, computer_score)
    write(outcome_message(outcome))
    return outcome


def play(
    read: Reader = input,
    write: Writer = print,
    draw: Draw = deal_card,
    clear: Callable[[], None] = clear_console,
) -> None:
    """!
    @brief Play games until the player does not want another one.
    @param read Reads the player's answers.
    @param write Shows text to the player.
    @param draw Draws one card.
    @param clear Clears the screen before each game.
    """
    while ask_yes_no(PROMPT_RESTART, read, write):
        clear()
        write(LOGO)
        play_game(read, write, draw)
    write(MESSAGE_GOODBYE)
