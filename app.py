
import streamlit as st
import openai
import os

# Set up the OpenAI API key from secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(page_title="Marketing Tool Match GPT", page_icon="🧩")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a friendly, expert marketing tools assistant created by LumelaWeb. Your job is to help small business owners, solopreneurs, and consultants find the right marketing tools based on their needs, skills, and business stage. Ask one question at a time and wait for the user to respond before continuing. At key checkpoints, ask if you can provide tool matches so far, rather than going on forever. Use a tone that reflects LumelaWeb’s style: warm, clear, no fluff, helpful."
        },
        {
            "role": "assistant",
            "content": (
                "Hey there! 👋 I’m Marketing Tool Match GPT, created by LumelaWeb. "
                "My job is to help small business owners, solopreneurs, and consultants like you find the right marketing tools "
                "that actually fit your business — no fluff, no overwhelm.\n\n"
                "Whether you're building your first system or trying to clean up a tech mess, I help you match your goals and "
                "growth plans with tools for things like:\n\n"
                "- CRM (Customer Relationship Management)\n"
                "- Email marketing\n"
                "- Booking/calendar tools\n"
                "- Landing pages\n"
                "- Analytics\n"
                "…and more.\n\n"
                "I’m built on the same strategic approach LumelaWeb uses in their 90-Day Website Growth Blueprint. "
                "If you'd rather talk to a human, you can always book a free 30-minute call here.\n\n"
                "Want me to help match you with the right tools? I’ll just need to ask a few quick questions. Ready to get started?"
            )
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")

# Text input and form submission
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your response:")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    # Do NOT rerun the script manually — Streamlit handles it after form submission
