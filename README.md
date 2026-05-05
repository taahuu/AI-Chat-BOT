# 🤖 AI Chatbot (Streamlit + Hugging Face)

An interactive AI chatbot built using Streamlit and Llama 3.1 via Hugging Face.  
This project demonstrates how to build a conversational AI system with memory, clean UI, and real-time response rendering.

---

## 🚀 Features

- 💬 ChatGPT-like interface using Streamlit  
- 🧠 Conversation memory (context-aware responses)  
- ⚡ Real-time typing effect  
- 🎯 Lightweight and fast  
- 🔐 Secure API handling using environment variables  

---

## 🛠 Tech Stack

- **Language:** Python  
- **Frontend:** Streamlit  
- **Backend:** LangChain  
- **Model:** Hugging Face (Llama 3.1 8B Instruct)  

---

## 📂 Project Structure

ai-chatbot/

│── app.py

│── requirements.txt

│── .env

│── .gitignore

│── README.md



---

## ▶️ Run Locally

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Setup Environment Variables

Create a .env file in the root directory and add:

HUGGINGFACEHUB_API_TOKEN=your_token_here

⚠️ Do NOT upload your .env file to GitHub

### 4️⃣ Run the Application

streamlit run app.py


