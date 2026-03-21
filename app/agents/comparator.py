import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def compare_agent(context, question):

    joined = "\n\n".join(context)

    prompt = f"""
    You are a legal document analysis assistant.

    Using the following context:
    {joined}

    Answer the question:
    {question}

    Highlight key clauses and differences.
    """

    response = llm.invoke(prompt)

    return response.content