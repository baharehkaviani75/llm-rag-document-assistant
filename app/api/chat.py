from fastapi import APIRouter

from app.rag.chain import ask_pdf


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("")
async def chat(question: str):

    result = ask_pdf(question)

    return {
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"],
    }