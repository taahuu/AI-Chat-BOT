from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Title
st.title("🤖 AI Chatbot")

# Load model (cached)
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

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input (ENTER works + auto clears)
user_input = st.chat_input("Type your message...")

# When user sends message
if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message instantly
    with st.chat_message("user"):
        st.markdown(user_input)

    # 🔥 Build conversation memory
    chat_history = ""
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_history += f"User: {msg['content']}\n"
        else:
            chat_history += f"Assistant: {msg['content']}\n"

    final_prompt = chat_history + "Assistant:"

    # Get response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        response = model.invoke(final_prompt)

        # Typing effect ⚡
        for word in response.content.split():
            full_response += word + " "
            message_placeholder.markdown(full_response)

        # Store bot response
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )