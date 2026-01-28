# Data Engineering Technical Challenge

## Overview

This repository implements a complete **Data Engineering system** designed to fulfill the requirements of the technical challenge. The solution demonstrates the design and implementation of an **ETL pipeline**, a **data lake with medallion architecture**, a **data warehouse with star schema**, a **vector-based search engine**, and a **REST API** to expose data access and search capabilities.

The project prioritizes **clarity, maintainability, and explainability**, following a **layered architecture** and using only open-source technologies.

---

## Architecture Summary

The system is composed of the following main components:

* **Data Lake (Medallion Architecture)**

  * Bronze: Raw structured and unstructured data
  * Silver: Cleaned and modeled relational data (Star Schema)
  * Gold: Aggregated, analytics-ready datasets

* **Data Warehouse**

  * SQLite database managed via SQLModel (ORM)

* **Vector Database**

  * Typesense, used for semantic search over textual fields

* **REST API**

  * Built with FastAPI
  * Exposes endpoints for seeding, CRUD operations, analytical queries, and vector search

Mermaid diagrams describing each layer and the overall architecture are located in `diagrams/mermaid/`.

---

## Dataset

### Source Data

The system uses a **publicly available e-commerce dataset** (CSV) containing transactional data, including:

* Orders
* Products
* Customers
* Prices and quantities
* Countries

This dataset is sufficiently complex to support:

* Fact and dimension modeling
* Analytical aggregations
* Text-based semantic search (product descriptions)

Optional unstructured data (PDFs / text documents) can be added to the Bronze layer and indexed in the vector database.

File with data is on /archive folder.

---

## Data Architecture

### Bronze Layer

* Stores raw data exactly as received
* Supports structured (CSV, JSON) and unstructured data (PDF)
* No transformations are applied
* Metadata such as source and ingestion timestamp can be added

### Silver Layer (Star Schema)

The Silver layer follows a **star schema**, optimized for analytical workloads.

**Fact Table:**

* `fact_sales`

**Dimension Tables:**

* `dim_product`
* `dim_customer`
* `dim_date`
* `dim_country`
* `dim_channel`

Transformations are performed using **Pandas**, not SQL queries.

### Gold Layer

The Gold layer contains **aggregated datasets**, such as:

* Sales by country
* Sales by product
* Customer lifetime value

Transformations are performed using **Pandas**, not SQL queries.
These datasets are optimized for fast consumption via the API.

---

## Vector Search

Typesense is used as a **Vector Database** to enable fast and flexible search capabilities.

### Indexed Content

* Product descriptions
* Text extracted from unstructured documents (e.g., PDFs)

### Search Capabilities

* Full-text / semantic search
* Filtering (e.g., by country or entity type)

The vector search complements relational queries and enables discovery use cases not suitable for SQL alone.

---

## REST API

The REST API is implemented using **FastAPI** and follows a layered design:

1. API / Routes
2. Services
3. Domain Entities
4. Data Access

### Key Endpoints

* **Seeding**

  * Initialize the system with source data

* **CRUD (Raw Data)**

  * Single and batch operations

* **Gold Layer Queries**

  * Access analytics-ready datasets

* **Search**

  * Semantic search using the vector database

### Authentication

The API implements **Basic Authentication** to protect endpoints,
Just for testing the credentials are:

USERNAME = "admin"
PASSWORD = "admin123"

---

## Code Structure

The project follows a **Layered Architecture**, ensuring separation of concerns:

* `api/` – HTTP routes and request handling
* `services/` – Business logic and orchestration
* `domain/` – Pydantic models representing domain entities
* `data_access/` – ORM models, repositories, database access
* `etl/` – ETL logic for Bronze, Silver, and Gold layers

Domain entities are intentionally **decoupled** from ORM/database models.

---

## Technologies Used

* **Python 3.10+**
* **FastAPI** – REST API
* **Pandas** – ETL transformations
* **SQLModel** – ORM and database modeling
* **SQLite** – Data warehouse storage
* **Typesense** – Vector database
* **Docker / Docker Compose** – Infrastructure
* **Mermaid** – Architecture diagrams

---

## How to Run the Project

### 1. Start the Vector Database

```bash
docker-compose up -d
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the API

```bash
uvicorn app.main:app --reload

or

python -m uvicorn app.main:app --reload
```

### 4. Seed the Data

Use the `/seed` endpoint to ingest and process the initial dataset.

---

## Design Decisions & Trade-offs

* **SQLite** was chosen for simplicity and portability
* **Pandas** was used for ETL to comply with the requirement of not using SQL for transformations
* **Typesense** provides fast and simple vector search without excessive operational overhead
* The system favors **clarity and explainability** over premature optimization

---

## Testing

The project can be extended with unit and integration tests for:

* ETL transformations
* API endpoints
* Vector search logic

Testing is intentionally minimal to focus on architecture and correctness.

---

## Use of AI Tools

AI-assisted tools were used responsibly to:

* Generate boilerplate code
* Draft documentation
* Review design decisions

All architectural choices and implementations were validated and refined manually.

---

## Future Improvements

* Incremental and streaming ingestion
* Authentication via OAuth or JWT
* Data quality checks
* Partitioning and performance optimizations
* CI/CD pipeline

---

## Conclusion

This project demonstrates an end-to-end **Data Engineering solution**, covering ingestion, transformation, modeling, analytics, and search. It is designed to be **easy to understand, easy to extend, and easy to defend** in a technical interview.
