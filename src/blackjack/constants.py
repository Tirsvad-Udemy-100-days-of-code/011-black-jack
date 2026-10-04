"""!
@file constants.py
@brief Constants for the Blackjack game; no magic numbers live in game code.
"""

## Value of an ace when it is counted as eleven.
ACE_HIGH: int = 11

## Value of an ace when it is counted as one.
ACE_LOW: int = 1

## The best possible score; a hand above it is bust.
BLACKJACK_SCORE: int = 21

## The dealer keeps drawing while its score is below this value.
DEALER_STAND_SCORE: int = 17

## Number of cards in the opening hand.
OPENING_HAND_SIZE: int = 2

## Score returned by the scoring function to mark a blackjack.
BLACKJACK_MARKER: int = 0

## Unlimited deck: cards are never removed. 11 is the ace, 10 covers 10/J/Q/K.
CARDS: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## Rank text for each card value; plain text renders in every terminal.
CARD_RANKS: dict[int, str] = {
    ACE_HIGH: "A",
    ACE_LOW: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
}

## Suit emoji shown after the rank; cards in a hand cycle through them.
CARD_SUITS: tuple[str, ...] = ("♠️", "♥️", "♦️", "♣️")

## Answer that means yes at a yes/no prompt.
ANSWER_YES: str = "y"

## Answer that means no at a yes/no prompt.
ANSWER_NO: str = "n"

## Prompt asking the player whether to draw another card.
PROMPT_HIT: str = "Type 'y' to get another card, type 'n' to pass: "

## Prompt asking the player whether to play a game.
PROMPT_RESTART: str = "Do you want to play a game of Blackjack? Type 'y' or 'n': "

## Message shown after an answer that is neither yes nor no.
MESSAGE_INVALID_ANSWER: str = "Please answer 'y' or 'n'."

## Message shown when the player leaves the game.
MESSAGE_GOODBYE: str = "Goodbye!"

## Label shown instead of a score when a hand is a blackjack.
LABEL_BLACKJACK: str = "Blackjack"

## Outcome messages.
MESSAGE_DRAW: str = "Draw \U0001f643"
MESSAGE_WIN: str = "You win \U0001f603"
MESSAGE_WIN_BLACKJACK: str = "Win with a Blackjack \U0001f60e"
MESSAGE_WIN_DEALER_BUST: str = "Opponent went over. You win \U0001f601"
MESSAGE_LOSE: str = "You lose \U0001f624"
MESSAGE_LOSE_DEALER_BLACKJACK: str = "Lose, opponent has Blackjack \U0001f631"
MESSAGE_LOSE_BUST: str = "You went over. You lose \U0001f62d"
