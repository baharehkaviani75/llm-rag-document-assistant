from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_text_splitter(
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
):
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ],
        length_function=len,
    )


def pages_to_documents(pages: list[dict]) -> list[Document]:

    documents = []

    for page in pages:

        document = Document(
            page_content=page["text"],
            metadata={
                "page": page["page"],
                "source": page["source"],
            },
        )

        documents.append(document)

    return documents


def create_chunks(
    pages: list[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[Document]:

    documents = pages_to_documents(pages)

    splitter = create_text_splitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = splitter.split_documents(documents)

    return chunks