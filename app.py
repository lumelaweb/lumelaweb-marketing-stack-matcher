import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Match GPT – Marketing Stack Matchmaker", page_icon="🧩")
st.title("🧩 Match GPT – Marketing Stack Matchmaker")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": """You are Match GPT, created by LumelaWeb to help entrepreneurs match the right marketing tools to their goals and tech comfort. 
You ask one clear question at a time. After 3–4 questions, ask if the user would like their customized stack.
Offer a free 30-min consultation: https://calendly.com/lumelaweb/30min. 
If they ask for a person, direct them to lumelaweb.com or ssimpson@lumelaweb.com."""}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Tell me what you're trying to solve...")
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    assistant_reply = response.choices[0].message.content
    st.chat_message("assistant").write(assistant_reply)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
