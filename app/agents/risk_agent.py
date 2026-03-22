import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def risk_agent(comparison_text):

    prompt = f"""
    You are a legal risk analysis assistant.

    Analyse the following document comparison:
    {comparison_text}

    Identify:
    - legal risks
    - compliance issues
    - ambiguous clauses
    - financial exposure

    Provide structured bullet points.
    """

    response = llm.invoke(prompt)

    return response.content