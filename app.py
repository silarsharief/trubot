import streamlit as st
from bot import answer_question
import os

# Set page config
st.set_page_config(
    page_title="Truwealth Q&A Chat",
    page_icon="💬",
    layout="centered"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load data
@st.cache_data
def load_data():
    with open(os.path.join(os.path.dirname(__file__), 'clean.txt'), 'r', encoding='utf-8') as file:
        return file.read()

data = load_data()

# Display chat title
st.title("💬 Truwealth Q&A Chat")
st.markdown("Ask me anything about Truwealth!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        response = answer_question(prompt, data)
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response}) 