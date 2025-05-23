
import streamlit as st
import openai
import os

# Set up the OpenAI API key from secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(page_title="Marketing Tool Match GPT", page_icon="🧩")

# Starter message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a friendly, expert marketing tools assistant created by LumelaWeb. Your job is to help small business owners, solopreneurs, and consultants find the right marketing tools based on their needs, skills, and business stage. Ask one question at a time and wait for the user to respond before continuing. At key checkpoints, ask if you can provide tool matches so far, rather than going on forever. Use a tone that reflects LumelaWeb’s style: warm, clear, no fluff, helpful."
        },
        {
            "role": "assistant",
            "content": "Hey there! 👋 I’m Marketing Tool Match GPT, created by LumelaWeb. My job is to help small business owners, solopreneurs, and consultants like you find the right marketing tools that actually fit your business — no fluff, no overwhelm.\n\nWhether you're building your first system or trying to clean up a tech mess, I help you match your goals and growth plans with tools for things like:\n\n- CRM (Customer Relationship Management)\n- Email marketing\n- Booking/calendar tools\n- Landing pages\n- Analytics\n…and more.\n\nI’m built on the same strategic approach LumelaWeb uses in their 90-Day Website Growth Blueprint. If you'd rather talk to a human, you can always book a free 30-minute call here.\n\nWant me to help match you with the right tools? I’ll just need to ask a few quick questions. Ready to get started?"
        }
    ]

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.markdown(f"**GPT:** {msg['content']}")
    else:
        st.markdown(f"**You:** {msg['content']}")

# User input
user_input = st.text_input("Your response:", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # GPT response using OpenAI Python v1 SDK
    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.rerun()
