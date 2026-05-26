# Streamlit entry point — run this
import streamlit as st
from chatbot.chain import get_chatbot_response
from chatbot.memory import initialize_memory
from ui.sidebar import show_sidebar
from ui.chat_window import display_chat

st.set_page_config(
    page_title="Simple AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Simple LangChain Chatbot")

show_sidebar()

if "messages" not in st.session_state:
    st.session_state.messages = []

initialize_memory()

display_chat()

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = get_chatbot_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()