from typing import TypedDict, List

class GraphState(TypedDict):
    question: str
    context: List[str]
    comparison_result: str