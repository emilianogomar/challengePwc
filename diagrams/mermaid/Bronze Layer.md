```mermaid

flowchart LR
    CSV[CSV Files] --> Bronze[(Bronze Layer)]
    JSON[JSON Files] --> Bronze
    PDF[PDF Files] --> Bronze

    Bronze --> Meta[Metadata<br/>source, ingest_date]

