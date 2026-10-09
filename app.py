
import streamlit as st

st.title("💬 Little Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = "name"

questions = {
    "name": "Hi, what's your name?",
    "age": "How old are you?",
    "happy": "Are you happy to talk to me?",
    "anything": "is anything you want to say and I should know that?",
    "anything_what": "what?",
    "hiding": "ARE YOU HIDING SOMETHING?",
    "hiding_what": "what is it?"
}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

step = st.session_state.step

if step != "done":
    answer = st.chat_input(questions[step])

    if answer:
        st.session_state.messages.append(
            {"role": "user", "content": answer}
        )

        reply = ""
        next_step = step

        if step == "name":
            reply = f"hello {answer}"
            next_step = "age"

        elif step == "age":
            try:
                age = float(answer)

                if age <= 19:
                    reply = "aww,so you are just a litle boy"
                elif age >= 20:
                    reply = "don't lie"

                next_step = "happy"

            except ValueError:
                reply = "Please enter your age as a number."

        elif step == "happy":
            if answer == "Yes":
                reply = "good boy"
            elif answer == "No":
                reply = "that's not the answer you're supposed to give. think more"
            else:
                reply = "I'll take your answer as a yes"

            next_step = "anything"

        elif step == "anything":
            if answer == "Yes":
                next_step = "anything_what"
            elif answer == "No":
                reply = "perfect"
                next_step = "hiding"
            else:
                reply = "hmmmmm"
                next_step = "hiding"

        elif step == "anything_what":
            reply = "aham"
            next_step = "hiding"

        elif step == "hiding":
            if answer == "Yes":
                next_step = "hiding_what"
            elif answer == "No":
                reply = "good boy"
                next_step = "done"
            else:
                reply = "!!!!!?"
                next_step = "done"

        elif step == "hiding_what":
            reply = "got it"
            next_step = "done"

        if reply:
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

        st.session_state.step = next_step
        st.rerun()

else:
    st.success("End of chat 💗")
  
