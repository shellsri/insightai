import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)


def show_chat(df):

    st.title("💬 Chat with Dataset")

    if not api_key:
        st.error("Google Gemini API key not found.")
        st.stop()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous conversation
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask anything about your dataset..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        summary = f"""
Dataset Shape:
{df.shape}

Columns:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

Missing Values:
{df.isnull().sum().to_string()}

Numerical Summary:
{df.describe().to_string()}

Sample Rows:
{df.head(10).to_string()}
"""

        prompt = f"""
You are an expert Data Scientist.

The user uploaded a dataset.

Dataset Information:

{summary}

User Question:

{question}

Rules:

- Answer ONLY using the dataset information.
- If information is unavailable, clearly say so.
- Explain in simple language.
- Give recommendations whenever appropriate.
"""

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        with st.spinner("Thinking..."):

            response = model.generate_content(prompt)

        answer = response.text

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )