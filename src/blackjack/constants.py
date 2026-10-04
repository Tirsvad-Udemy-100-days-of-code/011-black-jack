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

## Emoji face for each card value.
CARD_FACES: dict[int, str] = {
    ACE_HIGH: "\U0001f170️",
    ACE_LOW: "\U0001f170️",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣",
    9: "9️⃣",
    10: "\U0001f51f",
}
