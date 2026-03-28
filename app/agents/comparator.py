import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def compare_agent(context, question, chat_history):

    history = "\n".join(chat_history)

    joined = "\n\n".join(context)

    prompt = f"""
    You are a legal document analysis assistant.

    Conversation History:
    {history}

    Context:
    {joined}

    Current Question:
    {question}

    Answer clearly and refer to previous context if needed.
    """

    response = llm.invoke(prompt)

    return response.content