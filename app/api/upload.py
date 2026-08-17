from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import settings
from app.rag.chunker import create_chunks
from app.rag.loader import extract_pdf_text
from app.rag.vectorstore import add_documents


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing"
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    storage_path = Path(settings.pdf_storage_path)

    storage_path.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = storage_path / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        pages = extract_pdf_text(
            str(file_path)
        )

        chunks = create_chunks(
            pages
        )

        add_documents(
            chunks
        )

    except Exception as exc:

        file_path.unlink(
            missing_ok=True
        )

        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {exc}"
        )

    return {
        "status": "success",
        "filename": file.filename,
        "pages": len(pages),
        "chunks": len(chunks),
    }