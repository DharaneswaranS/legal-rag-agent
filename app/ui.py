import sys
import os

sys.path.append(os.path.abspath("."))
import streamlit as st
from app.graph.workflow import build_graph

st.set_page_config(page_title="AI Legal Analyzer")

st.title("📄 AI Legal Document Analyzer")

graph = build_graph()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a question about your documents:")

if st.button("Submit") and user_input:

    state = {
        "question": user_input,
        "chat_history": st.session_state.chat_history
    }

    result = graph.invoke(state)

    st.session_state.chat_history = result["chat_history"]

    st.write("### 🧠 AI Response")
    st.write(result["final_report"])