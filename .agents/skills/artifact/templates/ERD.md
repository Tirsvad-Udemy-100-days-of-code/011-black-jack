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

## Diagram

```plantuml
@startuml
hide circle
entity CUSTOMER {
  * id : int <<PK>>
  --
  name : string
}
entity ORDER {
  * id : int <<PK>>
  --
  * customer_id : int <<FK>>
}
CUSTOMER ||--o{ ORDER : places
@enduml
```

## Entity Table

### <ENTITY>

| Attribute | Type | PK/FK | Nullable | Source (DCD class.attribute) |
| --- | --- | --- | --- | --- |

## Relationship Table

| Entity | Cardinality | Entity | FK | Rule |
| --- | --- | --- | --- | --- |

## Normalization Notes

---

@LINKS@
