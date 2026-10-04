# C conventions

C has no single official style guide. This sub-skill fixes one consistent
style built on common practice; MISRA C and SEI CERT C are the references for
safety-critical or security-sensitive code.

## Standard base

ISO C11 or C17 as set by the project's compiler flag (`-std=c11`). Compile
with warnings on (`-Wall -Wextra -Wpedantic`); treat warnings as errors in
release builds.

## Naming

| Element | Convention | Example |
| --- | --- | --- |
| Function, variable, parameter | `snake_case` | `parse_header`, `byte_count` |
| Public symbol | module prefix plus `snake_case` (C has no namespaces) | `stay_reader_open()` |
| File-local function / variable | `static`, no prefix needed | `static int next_token(...)` |
| Type (`struct`, `enum`, `typedef`) | `snake_case_t`, module prefix for public types | `stay_reader_t` |
| Enum constant, macro, constant | `UPPER_SNAKE` with the module prefix | `STAY_READER_OK` |
| Header / source file | `snake_case.h` / `snake_case.c`, same base name | `stay_reader.h` |
| Header guard | `MODULE_FILE_H` (or `#pragma once` if the project allows) | `STAY_READER_H` |

- Do not use reserved identifiers: a leading underscore followed by an
  uppercase letter, any double underscore, or a leading underscore at file
  scope.
- POSIX reserves the `_t` suffix; keep the module prefix on public types so
  they cannot collide.
- Macros are a last resort; prefer `static inline` functions and `enum` or
  `const` values.

## Formatting

- One formatter configuration for the project (`clang-format`); 4 spaces (or
  the project's setting), no tabs mixed in.
- Braces on every `if`, `else`, `for`, `while`, even for one statement.
- One declaration per line; declare variables at first use, initialised.
- Headers: include what you use, only what you use; public headers are
  self-contained; add `extern "C"` guards when C++ code consumes them.

## Language rules

- Check every return value that can fail; check every allocation.
- Every `malloc`/`open`/`lock` has one clear owner and one matching release;
  release on every exit path (single exit or `goto cleanup`).
- Use `size_t` for sizes and indices, fixed-width types (`<stdint.h>`) for
  data layout, `const` wherever data is not modified, `restrict` only with
  care.
- Bounds are explicit: pass a length with every buffer; use `snprintf`,
  never `sprintf`, `strcpy` or `gets`.
- No undefined behaviour: no signed overflow, no out-of-range shifts, no use
  after free, no uninitialised reads.
- Avoid global mutable state; if unavoidable, `static` and documented.

## Errors

Return a status code (an `enum`) or `-1`/`NULL` plus an error out-parameter;
document which in the header. Never ignore a failing call. Read `errno`
immediately after the failing call.

## Tests

A unit-test framework (for example Unity or CMocka); run under sanitizers
(`-fsanitize=address,undefined`) in at least one build.

## Tooling

`clang-format`, `clang-tidy` or `cppcheck`, compiler warnings, sanitizers.

Review with `QC-CL-001`.
