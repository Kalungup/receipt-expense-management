# AI Receipt & Expense Management System

**Project:** Receipt & Expense Management  
**Current implementation:** n8n  
**Project status:** In development  
**Version:** 0.1.0

---

## 1. Project Overview

The AI Receipt & Expense Management System is an application designed to automate the ingestion, processing, categorisation and analysis of financial receipts.

The system accepts receipt images and PDF documents, extracts relevant financial information, converts unstructured receipt data into structured expense records, categorises transactions and generates expenditure summaries.

The overall application will be implemented using three independent approaches:

1. n8n workflow automation.
2. Python with LangChain.
3. Pure Python implementation using direct APIs and custom logic.

All three implementations will follow the same functional requirements and use shared test data and evaluation criteria.

This repository initially focuses on the n8n implementation.

## 2. Problem Statement

Manually processing receipts is time-consuming and makes it difficult to maintain accurate financial records.

Receipts contain unstructured information such as:

- Merchant names.
- Transaction dates.
- Purchased items.
- Quantities and prices.
- Subtotals.
- VAT.
- Total amounts.
- Payment methods.

The objective is to automate the conversion of these documents into structured and searchable expense records.

## 3. Project Objectives

The application aims to:

- Accept image and PDF receipts.
- Extract receipt information automatically.
- Identify merchants and transaction dates.
- Extract individual items and prices where possible.
- Identify transaction currencies.
- Categorise expenses.
- Validate extracted information.
- Store structured expense records.
- Detect potential duplicate receipts.
- Generate daily, weekly and monthly expenditure summaries.
- Provide a foundation for future financial analysis.

## 4. Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | Accept receipt images |
| FR-02 | Accept PDF receipts |
| FR-03 | Extract text from receipts |
| FR-04 | Identify merchant information |
| FR-05 | Extract transaction dates |
| FR-06 | Extract financial amounts |
| FR-07 | Identify currencies |
| FR-08 | Categorise expenses |
| FR-09 | Validate extracted information |
| FR-10 | Store structured transactions |
| FR-11 | Detect duplicate receipts |
| FR-12 | Generate expenditure summaries |

## 5. Non-Functional Requirements

- Reliability: Failed operations must be identifiable.
- Accuracy: Incorrect or uncertain extraction must be flagged.
- Security: Financial documents and credentials must be protected.
- Maintainability: Workflows must be organised and documented.
- Scalability: The architecture should support increasing receipt volumes.
- Observability: Workflow executions and failures must be traceable.

## 6. Technology Stack

### Current n8n implementation

- n8n: Workflow orchestration and automation.
- Docker: Containerisation and local development environment.
- Docker Compose: Management of application services.
- Python: Backend OCR service implementation.
- FastAPI: HTTP API for the OCR service.
- Tesseract OCR: Text recognition from receipt images.
- PyMuPDF: PDF processing and embedded text extraction.
- Git and GitHub: Version control and project collaboration.

### Planned Technologies

- PostgreSQL: Structured expense data storage.
- Pydantic: Structured data validation.
- LangChain: Alternative AI application implementation.
- LLM APIs: Intelligent receipt information extraction.
- AI vision: Advanced processing of receipt images.

### Alternative Implementations

The application will also be implemented using:

1. Python with LangChain.
2. Pure Python with direct API integration and custom logic.

## 7. High-Level Architecture

###The intended processing pipeline is:

Receipt Upload  
→ Document Validation  
→ OCR / Vision Processing  
→ Information Extraction  
→ Structured Data Validation  
→ Expense Categorisation  
→ Database Storage  
→ Financial Reporting

## 8. n8n Workflow Design

The n8n implementation uses modular workflows to separate
receipt processing responsibilities.

### Implemented Workflows

#### WF-01: Receipt Ingestion

Responsibilities:

1. Receive receipts through an upload form.
2. Extract receipt metadata.
3. Validate file type and file size.
4. Separate accepted and rejected uploads.
5. Send accepted receipts to WF-02.
6. Wait for the receipt extraction workflow to finish.

#### WF-02: Receipt Text Extraction

Responsibilities:

1. Receive receipt data and binary files from WF-01.
2. Inspect and validate the input.
3. Preserve original receipt metadata.
4. Send the receipt to the local OCR service.
5. Extract text from images and PDF documents.
6. Return extracted text and processing metadata.

### Planned Workflows

- WF-03: Structured Information Extraction.
- WF-04: Expense Categorisation.
- WF-05: Expense Validation.
- WF-06: Database Storage.
- WF-07: Expense Reporting.
- WF-08: Duplicate Detection.

## 9. Expense Categories

Initial categories:

- Groceries.
- Transport.
- Housing.
- Restaurants.
- Shopping.
- Healthcare.
- Entertainment.
- Utilities.
- Other.

## 10. Development Methodology

Development will progress incrementally.

Each milestone will include:

1. Requirements and concepts.
2. Implementation.
3. Testing.
4. Error handling.
5. Documentation.

The three application implementations will follow equivalent milestones to enable meaningful technical comparisons.

## 11. Current Development Status

## 11. Current Development Status

| Component | Status |
|---|---|
| Project requirements | Defined |
| High-level architecture | Initial design completed |
| Docker environment | Implemented |
| n8n environment | Running |
| Local OCR service | Implemented and tested |
| WF-01: Receipt Ingestion | Implemented |
| WF-02: Receipt Text Extraction | Implemented |
| WF-01 / WF-02 integration | Implemented |
| Structured information extraction | Pending |
| Expense categorisation | Pending |
| Expense validation | Pending |
| PostgreSQL integration | Pending |
| Duplicate detection | Pending |
| Financial reporting | Pending |

### Current Milestone

The initial receipt ingestion and OCR processing pipeline
has been implemented.

The application can receive receipt images and PDF documents,
validate uploads, forward accepted documents to the OCR service
and return extracted text with receipt metadata.

The next milestone is structured information extraction.

---

**Documentation is maintained progressively as development advances.**