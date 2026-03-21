from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes import retrieval_node, comparison_node

def build_graph():

    graph = StateGraph(GraphState)

    graph.add_node("retrieve", retrieval_node)
    graph.add_node("compare", comparison_node)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "compare")
    graph.add_edge("compare", END)

    return graph.compile()