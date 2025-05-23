import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Marketing Stack Matcher", page_icon="📎")

# Initial welcome message from the assistant
WELCOME_MESSAGE = (
    "Hey there! 👋 I’m Marketing Tool Match GPT, created by LumelaWeb. My job is to help small business owners, "
    "solopreneurs, and consultants like you find the right marketing tools that actually fit your business — no fluff, no overwhelm.\n\n"
    "Whether you're building your first system or trying to clean up a tech mess, I help you match your goals and growth plans with tools for things like:\n"
    "- CRM (Customer Relationship Management)\n"
    "- Email marketing\n"
    "- Booking/calendar tools\n"
    "- Landing pages\n"
    "- Analytics\n"
    "…and more.\n\n"
    "I’m built on the same strategic approach LumelaWeb uses in their 90-Day Website Growth Blueprint. If you'd rather talk to a human, you can always book a free 30-minute call here: https://calendly.com/lumelaweb/30min\n\n"
    "Want me to help match you with the right tools? I’ll just need to ask a few quick questions. Ready to get started?"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant that asks one question at a time and checks in after a few questions."},
        {"role": "assistant", "content": WELCOME_MESSAGE},
    ]

# Display title and get user input
st.title("📎 Marketing Tool Match GPT")
user_input = st.chat_input("Type your answer here...")

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process new user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get GPT response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
