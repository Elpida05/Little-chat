import streamlit as st

st.title("💬 Little Chat")

if "step" not in st.session_state:
st.session_state.step = 0
st.session_state.name = ""

if "messages" not in st.session_state:
st.session_state.messages = []

for message in st.session_state.messages:
with st.chat_message(message["role"]):
st.write(message["content"])

questions = [
"Hi! What's your name?",
"How old are you?",
"Are you happy to talk to me? 😊",
"Is there anything you want to say?",
"ARE YOU HIDING SOMETHING? 👀"
]

if st.session_state.step < len(questions):
answer = st.chat_input(questions[st.session_state.step])

if answer:
    st.session_state.messages.append(
        {"role": "user", "content": answer}
    )

    step = st.session_state.step

    if step == 0:
        st.session_state.name = answer
        reply = f"Hello, {answer}! 💗"

    elif step == 1:
        try:
            age = float(answer)
            reply = "Aww, so young! 🥹" if age <= 19 else "Oh, interesting! ✨"
        except ValueError:
            reply = "Haha, tell me your age in numbers! 😭"
            st.session_state.step -= 1

    elif step == 2:
        reply = "Yay! I'm happy you're here! 💕" if answer.lower() in ["yes", "yeah", "yep", "sure"] else "Aww, that's okay 🥺"

    elif step == 3:
        reply = "I'm listening 👀💗" if answer.lower() in ["yes", "yeah", "yep"] else "Okay, I'll ask again later 😌"

    else:
        reply = "Hehe, I knew it! 👀😂" if answer.lower() in ["yes", "yeah", "yep"] else "Hmm... I'll believe you for now 😏"

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.session_state.step += 1
    st.rerun()

else:
st.success("That's all for now! 💖")
