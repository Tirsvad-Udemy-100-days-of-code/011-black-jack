"""!
@file __main__.py
@brief Entry point: python -m blackjack.
"""

from blackjack.constants import MESSAGE_GOODBYE
from blackjack.game import play


def main() -> None:
    """!
    @brief Run the game; leave quietly on Ctrl+C or Ctrl+D.
    """
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{MESSAGE_GOODBYE}")


if __name__ == "__main__":
    main()
