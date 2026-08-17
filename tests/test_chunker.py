from app.rag.chunker import create_chunks


def test_create_chunks():

    pages = [
        {
            "text": (
                "Machine learning is a field of artificial intelligence. "
                * 100
            ),
            "page": 1,
            "source": "sample.pdf",
        }
    ]

    chunks = create_chunks(
        pages,
        chunk_size=200,
        chunk_overlap=50,
    )

    assert len(chunks) > 1

    for chunk in chunks:
        assert chunk.page_content
        assert chunk.metadata["page"] == 1
        assert chunk.metadata["source"] == "sample.pdf"