from app.rag.retriever import load_retriever
from app.agents.comparator import compare_agent
from app.graph.state import GraphState
from app.agents.risk_agent import risk_agent
from app.agents.report_agent import report_agent

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
def risk_node(state: GraphState):

    risk = risk_agent(
        state["comparison_result"]
    )

    return {
        "risk_analysis": risk
    }


def report_node(state: GraphState):

    report = report_agent(
        state["question"],
        state["risk_analysis"]
    )

    return {
        "final_report": report
    }