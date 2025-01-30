import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent and interactive student chatbot designed to assist learners in AI and Data Science. Your role is to provide clear, concise, and well-structured explanations of AI and Data Science concepts, including Machine Learning, Deep Learning, Data Analysis, and related programming languages like Python."),
    ("user", "{user_query}")  # Fixed placeholder
])

def main():
    """
    Streamlit app for an AI & Data Science learning chatbot.
    """
    st.title("DWAI")
    st.write("Got questions about AI, Data Science, Machine Learning, or Python? Ask away!")

    # User Input
    user_query = st.text_input("🔍 Enter your question:")

    if st.button("GENERATE"):
        if user_query:
            chain = prompt | llm
            response = chain.invoke({"user_query": user_query})
            
            # Ensure correct response extraction
            answer = response.content if hasattr(response, 'content') else response

            # Display Response
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question before asking.")

if __name__ == "__main__":
    main()
