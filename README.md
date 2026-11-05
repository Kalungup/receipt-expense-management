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

- n8n: Workflow orchestration.
- Docker: Local environment and deployment.
- PostgreSQL: Expense data storage (planned).
- AI vision/OCR service: Receipt extraction (planned).
- Git and GitHub: Version control.

### Other implementations

- Python.
- FastAPI.
- LangChain.
- Pydantic.
- PostgreSQL.
- Direct LLM API integration.

## 7. High-Level Architecture

The intended processing pipeline is:

Receipt Upload  
→ Document Validation  
→ OCR / Vision Processing  
→ Information Extraction  
→ Structured Data Validation  
→ Expense Categorisation  
→ Database Storage  
→ Financial Reporting

## 8. n8n Workflow Design

The initial workflow is:

**WF-01: Receipt Ingestion**

1. Receive a receipt through an upload form.
2. Validate the uploaded file.
3. Prepare receipt metadata.
4. Return an upload confirmation.

Future workflows:

- WF-02: Receipt Text Extraction.
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

| Component | Status |
|---|---|
| Project requirements | Defined |
| Architecture | Initial design |
| n8n environment | Pending setup |
| Receipt ingestion | Pending |
| OCR / vision | Not started |
| Structured extraction | Not started |
| Categorisation | Not started |
| Database integration | Not started |
| Reporting | Not started |

## 12. Future Improvements

- Expense dashboards.
- Bank statement imports.
- Receipt-to-bank transaction matching.
- Conversational expense analysis.
- Spending trends and budget monitoring.
- Multi-user support.

---

**Documentation is maintained progressively as development advances.**