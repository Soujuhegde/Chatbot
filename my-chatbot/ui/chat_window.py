# Message rendering logic
import streamlit as st

def display_chat():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])