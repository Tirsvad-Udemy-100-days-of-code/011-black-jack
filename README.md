# Blackjack

A console Blackjack game against a computer dealer, played with emoji cards.
It is the day 11 capstone of Udemy's *100 Days of Code: The Complete Python Pro
Bootcamp*, built with a plan-first process (milestones and issues in `docs/`).

## House rules

- The deck is unlimited; cards are not removed when drawn. No jokers.
- Jack, Queen and King count 10. An ace counts 11 or 1.
- A two-card hand of ace + 10 is a blackjack.
- The computer is the dealer and draws while its score is below 17.

## Requirements

- Python 3.13 or newer
- No runtime dependencies
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation
- A terminal with UTF-8 and emoji support (for example Windows Terminal)

## Setup

Create and activate a local virtual environment, upgrade pip, then install the
project in editable mode with the development tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`.

## Run

The game entry point is added in the *Game Implementation* milestone:

```bash
python -m blackjack
```

## Test

```bash
python -m unittest discover -s tests
```

`pytest` also runs the same tests (`python -m pytest`).

## Lint and type check

```bash
ruff check .
ruff format --check .
mypy src
```

## Documentation

Generate the source documentation (Doxygen comments in `src/`) into
`docs/doxygen/`:

```bash
doxygen Doxyfile
```

Planning documents (business case, stakeholder analysis, project plan and
milestones) are in `docs/`.

## Project layout

```text
src/blackjack/   game package (constants.py, ...)
tests/           unit tests
docs/            planning documents and generated Doxygen output
pyproject.toml   project configuration
Doxyfile         Doxygen configuration
```

## License

See [LICENSE](LICENSE).
