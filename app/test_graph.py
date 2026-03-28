from app.graph.workflow import build_graph

graph = build_graph()

state = {
    "question": "What are termination conditions?",
    "chat_history": []
}

# First question
result = graph.invoke(state)

print("Q1 Answer:\n", result["final_report"])

# Follow-up question
state = {
    "question": "What risks are associated with them?",
    "chat_history": result["chat_history"]
}

result2 = graph.invoke(state)

print("\nQ2 Answer:\n", result2["final_report"])