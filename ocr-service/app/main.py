
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import pytesseract
import fitz
import io

app = FastAPI(
    title="Receipt OCR Service",
    description="Local OCR service for receipt images and PDFs",
    version="1.0.0"
)

MAX_FILE_SIZE = 10 * 1024 * 1024

ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf"
}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "receipt-ocr"
    }


@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Unsupported file type"
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File exceeds 10 MB"
        )

    try:
        extracted_pages = []

        if file.content_type == "application/pdf":

            pdf = fitz.open(stream=content, filetype="pdf")

            if pdf.page_count > 30:
                raise HTTPException(
                    status_code=413,
                    detail="PDF exceeds 30 pages"
                )

            for page_number, page in enumerate(pdf, start=1):

                text = page.get_text().strip()

                method = "pdf_text"

                if not text:
                    pixmap = page.get_pixmap(
                        matrix=fitz.Matrix(2, 2),
                        alpha=False
                    )

                    image = Image.open(
                        io.BytesIO(pixmap.tobytes("png"))
                    )

                    text = pytesseract.image_to_string(
                        image,
                        lang="eng+swe"
                    )

                    method = "tesseract_ocr"

                extracted_pages.append({
                    "page": page_number,
                    "text": text,
                    "method": method
                })

            pdf.close()

            extraction_method = "pdf_text_or_ocr"

        else:

            image = Image.open(io.BytesIO(content))

            text = pytesseract.image_to_string(
                image,
                lang="eng+swe"
            )

            extracted_pages.append({
                "page": 1,
                "text": text,
                "method": "tesseract_ocr"
            })

            extraction_method = "tesseract_ocr"

        combined_text = "\n\n".join(
            page["text"]
            for page in extracted_pages
        )

        return {
            "status": "success",
            "filename": file.filename,
            "mime_type": file.content_type,
            "extraction_method": extraction_method,
            "page_count": len(extracted_pages),
            "extracted_text": combined_text,
            "pages": extracted_pages
        }

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Document extraction failed: {str(error)}"
        )
