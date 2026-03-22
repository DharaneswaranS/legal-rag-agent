from app.graph.workflow import build_graph

graph = build_graph()

result = graph.invoke({
    "question": "What are termination conditions?"
})

print(result["final_report"])