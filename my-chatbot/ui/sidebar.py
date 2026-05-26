# Settings sidebar (model selector, clear button)
import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.header("⚙️ Settings")
        st.write("Simple AI Chatbot using LangChain + Streamlit")

        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
