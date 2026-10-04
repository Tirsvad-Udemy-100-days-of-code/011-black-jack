# @TITLE@

## Metadata
| Key | Value |
| --- | --- |
| ID | @ID@ |
| CrossReference | @CROSSREF@ |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| @DATE@ | Accepted | @AUTHOR@ | <reviewer S-ID> | Initial version | pending |

---

## Purpose and Scope

Covers: <use cases>

## Diagram

Concepts, attributes and associations only — no operations.

```plantuml
@startuml
class Order {
  date
  status
}
class Customer {
  name
}
Customer "1" --> "0..*" Order : places
@enduml
```

## Concept Table

| Concept | Definition | Attributes | Source (use case / glossary) |
| --- | --- | --- | --- |

## Association Table

| From | Association (reading direction) | To | Multiplicity |
| --- | --- | --- | --- |

## Generalizations

| General | Specializations | Is-a justification |
| --- | --- | --- |

---

@LINKS@
