from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# Custom dark theme styling
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #e6edf3;
        }
        .stApp {
            background-color: #0e1117;
        }
        .chat-container {
            max-width: 700px;
            margin: auto;
        }
        .user-message {
            background-color: #1f6feb;
            color: white;
            padding: 10px 15px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: right;
        }
        .bot-message {
            background-color: #30363d;
            color: #e6edf3;
            padding: 10px 15px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: left;
        }
        .title {
            text-align: center;
            color: #58a6ff;
            font-size: 32px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 AI Chatbot</div>', unsafe_allow_html=True)

# Initialize model (only once)
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
    )
    return ChatHuggingFace(llm=llm)

model = load_model()

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input box
# user_input = st.text_input("Type your message...")
user_input = st.text_input("Type your message...", key="input")
# user_input = st.chat_input("Type your message...", key="input")


# Send button
if st.button("Send") and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response
    response = model.invoke(user_input)

    # Add bot response
    st.session_state.messages.append({"role": "bot", "content": response.content})

    # Rerun to update UI
    st.rerun()