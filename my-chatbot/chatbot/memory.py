# Chat history / memory management
import streamlit as st

def initialize_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []