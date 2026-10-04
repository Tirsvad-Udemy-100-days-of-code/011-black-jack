"""!
@file test_package.py
@brief Smoke tests: the package imports and its constants match the house rules.
"""

import unittest

import blackjack
from blackjack import constants


class TestPackage(unittest.TestCase):
    """!
    @brief Checks that the package and its constants load.
    """

    def test_package_has_version(self) -> None:
        """!
        @brief The package exposes a version string.
        """
        self.assertTrue(blackjack.__version__)

    def test_deck_matches_house_rules(self) -> None:
        """!
        @brief The deck is the 13-card list from the assignment.
        """
        self.assertEqual(constants.CARDS, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

    def test_every_card_has_an_emoji_face(self) -> None:
        """!
        @brief Every card in the deck can be rendered.
        """
        for card in constants.CARDS:
            self.assertIn(card, constants.CARD_FACES)


if __name__ == "__main__":
    unittest.main()
