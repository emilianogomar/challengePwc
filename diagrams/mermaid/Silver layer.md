```mermaid

erDiagram
    FACT_SALES {
        string order_id PK
        string product_id FK
        string customer_id FK
        int quantity
        float unit_price
        float total_amount
    }

    DIM_PRODUCT {
        string product_id PK
        string description
    }

    DIM_CUSTOMER {
        string customer_id PK
        string country
    }

    DIM_DATE {
        string date_id PK
        int day
        int month
        int year
    }

    DIM_COUNTRY {
        string country_id PK
        string country_name
    }

    DIM_CHANNEL {
        string channel_id PK
        string channel_name
    }

    FACT_SALES }o--|| DIM_PRODUCT : product
    FACT_SALES }o--|| DIM_CUSTOMER : customer
    FACT_SALES }o--|| DIM_DATE : date
    FACT_SALES }o--|| DIM_COUNTRY : country
    FACT_SALES }o--|| DIM_CHANNEL : channel
