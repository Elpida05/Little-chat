
import streamlit as st

st.title("💬 Little Chat")
st.write("Let's talk! 💗")

if "step" not in st.session_state:
    st.session_state.step = 0

if "messages" not in st.session_state:
    st.session_state.messages = []

questions = [
    "Hi! What's your name?",
    "How old are you?",
    "Are you happy to talk to me?",
    "Is there anything you want to say?",
    "ARE YOU HIDING SOMETHING? 👀"
]

replies = [
    "Nice to meet you! 💗",
    "Oh, interesting! ✨",
    "I hope you're having fun! 😊",
    "I'm listening! 👀",
    "Hehe, I'll let you decide! 😏"
]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.step < len(questions):
    answer = st.chat_input(questions[st.session_state.step])

    if answer:
        st.session_state.messages.append(
            {"role": "user", "content": answer}
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": replies[st.session_state.step]
            }
        )

        st.session_state.step += 1
        st.rerun()
else:
    st.success("Chat finished! 💖")
    
