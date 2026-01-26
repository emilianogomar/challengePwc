```mermaid

flowchart TB
    FACT[Fact Sales] --> AGG1[Sales by Country]
    FACT --> AGG2[Sales by Product]
    FACT --> AGG3[Customer Lifetime Value]

    AGG1 --> Gold[(Gold Layer)]
    AGG2 --> Gold
    AGG3 --> Gold
