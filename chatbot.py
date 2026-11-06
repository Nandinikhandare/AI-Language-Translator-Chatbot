import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from datetime import datetime

# Load API key
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="English-Hinglish AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 English-Hinglish AI Chatbot")
st.write("Ask me anything in English, Hindi, or Hinglish!")

# Create LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)
     # Get current date and time
    current_datetime = datetime.now()

    current_date = current_datetime.strftime("%d-%m-%Y")
    current_time = current_datetime.strftime("%I:%M %p")


    # System instruction
    prompt = f"""
You are a friendly AI chatbot.

You understand English, Hindi, and Hinglish.

Current date: {current_date}
Current time: {current_time}

Rules:
- If the user asks in English, answer in English.
- If the user asks in Hinglish, answer in Hinglish.
- If the user asks in Hindi, answer in simple Hindi.
- Keep explanations simple and beginner-friendly.
- For technical questions, explain with simple examples.
- Be polite and helpful.

User question:
{user_input}
"""

    # Get AI response
    response = llm.invoke(prompt)

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)

    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response.content
    })