import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from streamlit_chat import message

load_dotenv(override=True)

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an advanced AI assistant modeled after ChatGPT, engaging naturally and informatively."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{user_query}")
])

def main():
    st.set_page_config(page_title="DWAI - Chat", page_icon="🤖", layout="wide")

    st.title("DWAI")
    st.write("Smart. Fast. Engaging. Your AI Companion!")

    # Session for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Show conversation
    for i, (role, msg) in enumerate(st.session_state.chat_history):
        is_user = (role == "user")
        message(msg, is_user=is_user, key=f"msg_{i}")

    # Text input at the bottom
    user_query = st.chat_input(
        "Ask anything", # Placeholder as the first argument
        key="user_input",  # Key to access the text input
    )

    # Only process the query when the user submits it
    if user_query:
        chain = prompt | llm
        response = chain.invoke({
            "chat_history": st.session_state.chat_history,
            "user_query": user_query
        })

        answer = response.content if hasattr(response, 'content') else response

        # Save messages
        st.session_state.chat_history.append(("user", user_query))
        st.session_state.chat_history.append(("assistant", answer))

        # Trigger rerun to display the response
        st.rerun()

if __name__ == "__main__":
    main()