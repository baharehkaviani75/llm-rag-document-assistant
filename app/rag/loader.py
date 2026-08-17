from pathlib import Path

import fitz


def extract_pdf_text(file_path: str) -> list[dict]:
    """
    Extract text from each PDF page.

    Returns:
        A list of dictionaries containing:
        - text
        - page
        - source
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("File must be a PDF")

    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text("text").strip()

        if not text:
            continue

        pages.append(
            {
                "text": text,
                "page": page_number,
                "source": path.name,
            }
        )

    document.close()

    return pages