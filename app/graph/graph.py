from langgraph.graph import StateGraph

from app.graph.edge import add_workflow_edges
from app.graph.nodes import (
    build_context_node,
    generate_answer_node,
    rerank_node,
    retrieve_node,
)
from app.graph.state import GraphState


def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("rerank", rerank_node)
    workflow.add_node("build_context", build_context_node)
    workflow.add_node("generate_answer", generate_answer_node)

    add_workflow_edges(workflow)

    return workflow.compile()


graph = build_graph()