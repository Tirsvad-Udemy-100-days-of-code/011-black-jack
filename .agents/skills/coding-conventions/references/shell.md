# Shell conventions (bash)

## Standard base

Bash 4 or later, POSIX `test` semantics through `[[ ]]`. Start every script
with `#!/usr/bin/env bash` and `set -euo pipefail`. State the bash version and
the external tools it needs in the header comment.

## Naming

| Element | Convention | Example |
| --- | --- | --- |
| Script file | `kebab-case.sh`, executable | `check-plan.sh`, `new-artifact.sh` |
| Function | `snake_case`, a verb | `read_registry`, `die` |
| Local variable, parameter | `snake_case`, declared with `local` | `msgfile`, `changed` |
| Constant, environment variable | `UPPER_SNAKE` | `PLAN_GATE`, `PROJECT_ROOT` |
| Boolean | `is_` / `has_` prefix, value `0` or `1` | `is_enabled=1` |

- Name a script and its functions by what they do, not how.
- Do not shadow a command with a function of the same name.

## Formatting

- 2 spaces, no tabs. One command per line; `then` and `do` on the same line as
  `if` and `for`. Keep lines near 80 characters; break long pipelines at `|`.
- Format with `shfmt -i 2 -ci`; lint with `shellcheck`. Commit the project's
  `.editorconfig` or `.shellcheckrc` with the code.

## Language rules

- **Quote every expansion** (`"$var"`, `"${arr[@]}"`); use arrays, not
  space-separated strings, for lists. Use `[[ ]]`, not `[ ]`, and `$(...)`,
  not backticks.
- Declare function variables `local`; no globals except constants.
- Parse options with `case` and `shift`, check required arguments with
  `"${1:?usage: ...}"`, and print a usage line on bad input.
- Read input with `read -r`; iterate files with globs or `find -print0`, never
  by parsing `ls`.
- Use `mktemp` for temporary files and remove them with `trap ... EXIT`; never
  a fixed `/tmp` name.

## Errors and exit codes

- Errors go to standard error, start with `error:`, say what is wrong and what
  to do, and end the script with a non-zero exit code (`die` helper).
- `0` is success, `1` a failed check or bad input, `2` a usage error; document
  any other code in the header.
- Never swallow a failure with `|| true` without a comment that says why.

## Safety

- A script that changes state outside its own directory defaults to a dry run
  or asks for an explicit flag (`--apply`, `--force`); say so in the header.
- Never echo a token or password, put one on a command line, or commit one;
  read secrets from the environment or a gitignored file.
- Do not `eval` input; do not build a command from unvalidated text.

## Tools

Formatter `shfmt`, linter `shellcheck`, syntax check `bash -n`. These are the
recommended tools, not a pipeline: enforcing them in CI is outside this
framework's scope.
