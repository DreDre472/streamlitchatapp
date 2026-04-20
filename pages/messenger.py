import streamlit as st
import json
import os
from datetime import datetime
from streamlit import st_autorefresh

st_autorefresh(interval=2000, limit=None, key="refresh")

if 'username' not in st.session_state:
    st.error("Please log in first.")
    st.stop()
st.title("Misij")
st.write("misinjer")
CHAT_FILE = 'chat.txt'
def load_messages():
    if not os.path.exists(CHAT_FILE):
        return []
    with open(CHAT_FILE, 'r') as f:
        messages = []
        for line in f:
            if line.strip():
                messages.append(json.loads(line.strip()))
        return messages
def save_message(user, message):
    with open(CHAT_FILE, 'a') as f:
        data = {'user': user, 'message': message, 'timestamp': str(datetime.now())}
        json.dump(data, f)
        f.write('\n')
messages = load_messages()
for msg in messages:
    if msg['user'] == st.session_state.username:
        col1, col2 = st.columns([3, 1])
        with col2:
            st.markdown(f"""
<div style='text-align: right; background-color: #00FFFF; color: black; padding: 10px; border-radius: 10px; margin: 5px;'>
<strong>{msg['user']}</strong><br>
{msg['message']}
</div>
""", unsafe_allow_html=True)
    else:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"""
<div style='text-align: left; background-color: #B5B5B5; color: black; padding: 10px; border-radius: 10px; margin: 5px;'>
<strong>{msg['user']}</strong><br>
{msg['message']}
</div>
""", unsafe_allow_html=True)

if prompt := st.chat_input("Type your message..."):
    user = st.session_state.username
    save_message(user, prompt)
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown(f"""
<div style='text-align: right; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin: 5px;'>
<strong>{user}</strong><br>
{prompt}
</div>
""", unsafe_allow_html=True)
    st.rerun()

