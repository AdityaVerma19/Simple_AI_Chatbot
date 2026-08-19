import requests
import streamlit as st


API_URL = "https://simple-ai-chatbot-2.onrender.com/"


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)


st.title("🤖 AI Chatbot")

st.caption("FastAPI + OpenAI + Streamlit")


if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
prompt = st.chat_input("Ask me anything...")


if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Send request to FastAPI
    response = requests.post(
        API_URL,
        json={
            "message": prompt
        }
    )


    if response.status_code == 200:

        answer = response.json()["response"]

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    else:

        st.error(
            f"API Error: {response.status_code}"
        )
