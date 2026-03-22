from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes import (
    retrieval_node,
    comparison_node,
    risk_node,
    report_node
)

def build_graph():

    graph = StateGraph(GraphState)

    graph.add_node("retrieve", retrieval_node)
    graph.add_node("compare", comparison_node)
    graph.add_node("risk", risk_node)
    graph.add_node("report", report_node)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "compare")
    graph.add_edge("compare", "risk")
    graph.add_edge("risk", "report")
    graph.add_edge("report", END)

    return graph.compile()