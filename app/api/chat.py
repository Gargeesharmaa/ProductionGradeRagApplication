from fastapi import APIRouter

from app.graph.graph import graph
from app.schema.chat import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question,
            "retrieved_documents": [],
            "context": "",
            "answer": "",
        }
    )

    return ChatResponse(
        answer=result["answer"]
    )