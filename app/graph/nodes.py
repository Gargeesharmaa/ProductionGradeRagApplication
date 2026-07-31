from app.graph.state import GraphState
from app.retrieval.retriever import Retriever
from app.retrieval.reranker import DocumentReranker
from app.retrieval.context_builder import ContextBuilder
from app.llm.prompt import GroqLLM


retriever = Retriever()
reranker = DocumentReranker()
context_builder = ContextBuilder()
llm = GroqLLM()


def retrieve_node(state: GraphState) -> GraphState:
    """
    Retrieve relevant documents.
    """

    documents = retriever.retrieve(
        query=state["question"]
    )

    state["retrieved_documents"] = documents

    return state


def rerank_node(state: GraphState) -> GraphState:
    """
    Rerank retrieved documents.
    """

    documents = reranker.rerank(
        query=state["question"],
        documents=state["retrieved_documents"],
    )

    state["retrieved_documents"] = documents

    return state


def build_context_node(state: GraphState) -> GraphState:
    """
    Convert retrieved documents into formatted context.
    """

    context = context_builder.build(
        state["retrieved_documents"]
    )

    state["context"] = context

    return state


def generate_answer_node(state: GraphState) -> GraphState:
    """
    Generate the final answer.
    """

    answer = llm.generate(
        question=state["question"],
        context=state["context"],
    )

    state["answer"] = answer

    return state