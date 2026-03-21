from app.rag.retriever import load_retriever
from app.agents.comparator import compare_agent
from app.graph.state import GraphState
retriever = load_retriever()

def retrieval_node(state: GraphState):
    
    query = state["question"]

    docs = retriever.invoke(query)

    context = [d.page_content for d in docs]

    return {
        "context": context
    }
def comparison_node(state: GraphState):

    result = compare_agent(
        state["context"],
        state["question"]
    )

    return {
        "comparison_result": result
    }