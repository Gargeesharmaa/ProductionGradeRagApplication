from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

from app.graph.graph import graph
from app.llm.groq_client import GroqLLM
from app.retrieval.context_builder import ContextBuilder
from app.retrieval.retriever import Retriever
from app.retrieval.reranker import DocumentReranker
from app.schema.chat import StreamChatRequest

router = APIRouter(
    prefix="/stream",
    tags=["Streaming Chat"],
)

retriever = Retriever()
reranker = DocumentReranker()
context_builder = ContextBuilder()
llm = GroqLLM()


@router.post("/")
async def stream_chat(request: StreamChatRequest):

    async def event_generator():

        docs = retriever.retrieve(
            request.question
        )

        docs = reranker.rerank(
            request.question,
            docs
        )

        context = context_builder.build(docs)

        for token in llm.stream(
            request.question,
            context,
        ):

            yield {
                "event": "message",
                "data": token
            }

    return EventSourceResponse(
        event_generator()
    )