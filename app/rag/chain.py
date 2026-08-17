from langchain_core.prompts import ChatPromptTemplate

from app.models.llm import get_llm
from app.rag.retriever import get_retriever


PROMPT = """
You are an enterprise PDF assistant.

Answer the user's question using ONLY the provided context.

Do not use outside knowledge.

Every factual statement must be supported by the context.

If the answer cannot be found in the context, say:

"I could not find the answer in the provided document."

Keep the answer concise and factual.

Context:
{context}

Question:
{question}

Answer:
"""


def build_context(documents):

    context_parts = []

    for document in documents:

        page = document.metadata.get("page")
        source = document.metadata.get("source")

        context_parts.append(
            f"""
[Page {page}]
Source: {source}

Content:
{document.page_content}
"""
        )

    return "\n\n".join(context_parts)



def build_sources(documents):

    sources = []

    seen = set()

    for document in documents:

        page = document.metadata.get("page")
        source = document.metadata.get("source")

        key = (source, page)

        if key in seen:
            continue

        seen.add(key)

        sources.append(
            {
                "source": source,
                "page": page,
            }
        )

    return sources



def ask_pdf(question: str):

    print("START ASK PDF:", question)

    try:

        retriever = get_retriever(
            k=5
        )

        print("Retriever created")


        documents = retriever.invoke(
            question
        )

        print(
            "Documents retrieved:",
            len(documents)
        )


        context = build_context(
            documents
        )

        print("Context built")


        prompt = ChatPromptTemplate.from_template(
            PROMPT
        )


        llm = get_llm()

        print("LLM loaded")


        chain = prompt | llm


        response = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        print("LLM response received")


        return {
            "answer": response.content,

            "documents": documents,

            "sources": build_sources(
                documents
            ),
        }


    except Exception as e:

        import traceback

        print("\nERROR INSIDE ASK_PDF")

        traceback.print_exc()

        raise e