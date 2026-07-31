import uuid

import requests
import streamlit as st

# -----------------------------
# Configuration
# -----------------------------

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Production RAG Chatbot",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("Production RAG")

    st.write("Session ID")

    st.code(st.session_state.session_id)

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "docx", "txt"],
    )

    if st.button("Upload"):

        if uploaded_file is None:
            st.warning("Select a file first.")

        else:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type,
                )
            }

            with st.spinner("Indexing document..."):

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files,
                )

            if response.status_code == 200:

                data = response.json()

                st.success("Upload Successful")

                st.write(f"Filename : {data['filename']}")
                st.write(f"Chunks : {data['chunks']}")

            else:
                st.error(response.text)

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# -----------------------------
# Main Chat Window
# -----------------------------

st.title("Production RAG Chatbot")

st.caption("FastAPI • LangGraph • Groq • Qdrant • Redis")

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input("Ask anything about your documents...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": question,
                    "session_id": st.session_state.session_id,
                },
            )

            if response.status_code == 200:

                answer = response.json()["answer"]

            else:

                answer = "Something went wrong."

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )