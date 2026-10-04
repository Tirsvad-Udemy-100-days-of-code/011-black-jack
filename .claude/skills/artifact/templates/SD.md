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

## Sequence: <operationName>

**Realizes:** `operationName` in [OC-<n>]

### Diagram

```plantuml
@startuml
participant ":Controller" as C
participant ":Collaborator" as X
C -> X : message(args)
activate X
X --> C : result
deactivate X
@enduml
```

### Pattern Annotations

| Pattern (GRASP / GoF) | Applied to | Rationale |
| --- | --- | --- |

### Postcondition Coverage

| Postcondition (from contract) | Satisfied by message |
| --- | --- |

### Responsibility Check

---

@LINKS@
