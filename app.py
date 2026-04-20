import streamlit as st
import requests
st.title("Login")

username = st.text_input("Enter your username")

if st.button("Login"):
    if username.strip():
        st.session_state.username = username.strip()
        st.success(f"Logged in as {username}")
        st.switch_page("pages/messenger.py")
    else:
        st.error("Please enter a username")

