from langgraph.graph import END, START, StateGraph


def add_workflow_edges(workflow: StateGraph) -> None:
    """
    Register all graph edges.
    """

    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "rerank")
    workflow.add_edge("rerank", "build_context")
    workflow.add_edge("build_context", "generate_answer")
    workflow.add_edge("generate_answer", END)