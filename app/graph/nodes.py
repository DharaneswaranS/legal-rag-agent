from app.rag.retriever import load_retriever
from app.agents.comparator import compare_agent
from app.graph.state import GraphState
from app.agents.risk_agent import risk_agent
from app.agents.report_agent import report_agent

retriever = load_retriever()

def retrieval_node(state: GraphState):

    query = state["question"]

    docs = retriever.invoke(query)

    context = []
    sources = []

    for d in docs:
        context.append(d.page_content)

        source_info = f"{d.metadata.get('source', 'unknown')} (page {d.metadata.get('page', '-')})"
        sources.append(source_info)

    return {
        "context": context,
        "sources": sources
    }
def comparison_node(state: GraphState):

    result = compare_agent(
        state["context"],
        state["question"],
        state.get("chat_history", [])
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
        state["risk_analysis"],
        state["sources"]
    )

    updated_history = state.get("chat_history", []) + [
        f"Q: {state['question']}",
        f"A: {report}"
    ]

    return {
        "final_report": report,
        "chat_history": updated_history
    }