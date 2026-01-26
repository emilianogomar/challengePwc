```mermaid

flowchart LR
    Source[Public Dataset<br/>CSV / PDF] --> Bronze
    Bronze --> Silver
    Silver --> Gold

    Silver --> Typesense
    Gold --> API
    Typesense --> API

    API --> Client[REST Consumers]
