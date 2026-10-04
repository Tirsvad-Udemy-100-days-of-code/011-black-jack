# Python conventions

## Standard base

PEP 8 (style), PEP 257 (docstrings), PEP 484 and later (type hints). Target
the Python version declared in `pyproject.toml`.

## Naming

| Element | Convention | Example |
| --- | --- | --- |
| Package / module | short `snake_case` | `billing`, `stay_reader.py` |
| Class, exception | `PascalCase`; exceptions end in `Error` | `StayReader`, `InvalidDateError` |
| Function, method, variable, parameter | `snake_case` | `total_price`, `read_stays()` |
| Constant (module level) | `UPPER_SNAKE` | `MAX_RETRIES` |
| Internal (not public API) | one leading underscore | `_parse_row` |
| Type variable | short `PascalCase`; `_co` / `_contra` for variance | `T`, `KeyT`, `ItemT_co` |
| Boolean | `is_`, `has_`, `can_` prefix | `is_active` |
| Test file / function | `test_<module>.py` / `test_<behavior>_<condition>` | `test_total_when_empty` |

- Avoid name mangling (`__name`) unless you need it to prevent a subclass clash.
- Never use `l`, `O` or `I` as single-letter names.
- Do not shadow builtins (`list`, `id`, `type`); add a trailing underscore
  (`type_`) only as a last resort.

## Formatting

- 4 spaces, no tabs. Maximum line length set once in the formatter config
  (88 with `ruff format`; 79 if the project follows PEP 8 strictly).
- Imports at the top, grouped standard library / third party / local, one
  blank line between groups, no wildcard imports.
- Double quotes for strings unless the formatter says otherwise.
- Trailing commas in multi-line literals and calls.

## Language rules

- Annotate every function signature (parameters and return, `-> None` too).
  Modern syntax: `X | None`, `list[str]`. Avoid `Any` without a comment.
- `pathlib` over `os.path`; f-strings over `%` or `.format`; `enum` over
  magic strings; `dataclass` (frozen where possible) over ad-hoc dicts.
- No mutable default arguments; no bare `except:`; no `print` for logging
  (use `logging`).
- Use context managers (`with`) for files, locks and connections.
- Prefer comprehensions over `map`/`filter` with lambdas; keep them simple.
- Docstrings (PEP 257) on public modules, classes and functions; say what,
  not how.

## Errors

Raise specific exceptions; catch the narrowest type; re-raise with
`raise ... from err` to keep the cause. Do not use exceptions for normal
control flow.

## Tests

`pytest`; one behaviour per test; `tmp_path` for files; fakes over mocks where
a simple fake is possible; tests do not depend on order or on the network.

## Tooling

`ruff` (lint and format) and `mypy --strict` (types), configured in
`pyproject.toml`. Architecture rules (layers, ports, dataframes) are in
`.agents/rules/python.md` and the `python-developer` agent; this sub-skill
covers naming and style only.

Review with `QC-PY-001`.
