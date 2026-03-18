from typing import TypedDict, List

class GraphState(TypedDict):
    question: str
    documents: List[str]
    result: str