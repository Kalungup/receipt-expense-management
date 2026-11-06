
# WF-01 — Receipt Ingestion
## Version History

### Version 1.0

**Definition:** Basic receipt ingestion and validation workflow.

**Features:**
- Receipt upload form.
- Receipt metadata extraction.
- File type and size validation.
- Accepted and rejected branches.
- User completion messages.

**Limitation:** Accepted receipts were not automatically sent for OCR processing.

### Version 1.1 — Current Version

**Definition:** Receipt ingestion workflow integrated with the OCR processing system.

**New functionality:**
- Added Execute Sub-workflow node.
- Connected WF-01 to WF-02.
- Transfers receipt data and binary files.
- Waits for OCR processing to finish.
- Returns the sub-workflow execution result.

**Current capability:** Receipts can be uploaded, validated and automatically forwarded for text extraction.
