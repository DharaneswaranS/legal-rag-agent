import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def report_agent(question, risk_text):

    prompt = f"""
    Generate a professional legal analysis report.

    User query:
    {question}

    Risk findings:
    {risk_text}

    Structure:
    - Executive Summary
    - Key Findings
    - Risk Assessment
    - Recommendation
    """

    response = llm.invoke(prompt)

    return response.content