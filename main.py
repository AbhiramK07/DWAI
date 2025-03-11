import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an advanced AI assistant modeled after ChatGPT, designed to engage in natural,\
      informative, and context-aware conversations. Your primary goal is to provide accurate, insightful,\
      and engaging responses across various topics, including general knowledge, technology, science, \
     education, entertainment, and daily life queries."),
    ("user", "{user_query}")
])

def main():

    st.title("DWAI")
    st.write("Smart. Fast. Engaging. Your AI Companion!")

    user_query = st.text_input("Enter your question:")

    if st.button("ANSWER"):
        if user_query:
            chain = prompt | llm
            response = chain.invoke({"user_query": user_query})
            
            answer = response.content if hasattr(response, 'content') else response

            st.subheader("Answer:")
            st.write(answer)

        else:
            st.warning("Please enter a question before asking.")

if __name__ == "__main__":
    main()
