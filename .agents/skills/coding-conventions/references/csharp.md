# C# conventions

## Standard base

Microsoft's C# coding conventions and .NET Framework Design Guidelines, with
the analyzers that ship in the SDK. Target the language version of the
project's `LangVersion` / target framework.

## Naming

| Element | Convention | Example |
| --- | --- | --- |
| Namespace | `PascalCase`, matches folder path | `Billing.Stays` |
| Class, struct, record, enum, delegate | `PascalCase` (nouns) | `StayReader` |
| Interface | `I` + `PascalCase` | `IStayReader` |
| Method, property, event, public field | `PascalCase` | `ReadStays()`, `CheckIn` |
| Constant, `static readonly` | `PascalCase` | `MaxRetries` |
| Enum value | `PascalCase`; `[Flags]` enums are plural | `Status.NotFound` |
| Parameter, local variable | `camelCase` | `byteCount` |
| Private / internal field | `_camelCase` | `_buffer` |
| Generic type parameter | `T` or `T` + `PascalCase` | `T`, `TKey` |
| Async method | ends in `Async` | `ReadStaysAsync()` |
| Exception, attribute | end in `Exception` / `Attribute` | `InvalidDateException` |
| Boolean | `Is`, `Has`, `Can` prefix | `IsActive` |
| File | the type's name, one top-level type per file | `StayReader.cs` |

- Two-letter acronyms are upper case (`IO`); longer ones are `PascalCase`
  (`Xml`, `Http`).

## Formatting

- `.editorconfig` checked in; `dotnet format` applies it. 4 spaces, Allman
  braces, braces on every control-flow body.
- File-scoped namespaces (`namespace X;`); `using` directives outside the
  namespace, `System` first.
- `var` when the type is obvious from the right-hand side, explicit type
  otherwise.

## Language rules

- Enable nullable reference types (`<Nullable>enable</Nullable>`) and treat
  nullable warnings as errors; do not suppress with `!` without a comment.
- `IDisposable` owners use `using`; implement the dispose pattern only when
  needed.
- `async`/`await` all the way; no `.Result` or `.Wait()`; no `async void`
  except event handlers; pass `CancellationToken` through public async APIs.
- Prefer properties over public fields, `readonly` and `init` for
  immutability, `record` for value-like data, pattern matching and switch
  expressions over long `if` chains.
- LINQ for queries, loops for side effects; do not enumerate a sequence twice.
- String interpolation over concatenation; `StringBuilder` in loops;
  `DateTimeOffset` over `DateTime` for points in time; `decimal` for money.
- XML documentation comments (`///`) on public types and members.

## Errors

Throw specific exceptions (`ArgumentNullException`, custom types); validate
arguments at the public boundary (`ArgumentNullException.ThrowIfNull`). Catch
the narrowest type; `throw;` (not `throw ex;`) to rethrow. Never an empty
`catch`.

## Tests

xUnit, NUnit or MSTest; names like `Method_Condition_Expected`; one behaviour
per test; no dependence on order, time or the network.

## Tooling

`dotnet format`, the .NET analyzers (`AnalysisLevel`, `EnforceCodeStyleInBuild`)
and optionally StyleCop.Analyzers, configured in `.editorconfig`.

Review with `QC-CS-001`.
