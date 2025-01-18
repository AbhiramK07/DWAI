import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override= True)

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp")

prompt = ChatPromptTemplate.from_messages([("system", "You are a translator that translates {input_lang} to {output_lang}. Translate the user sentence."), ("user", "{input_text}")])

def main():
    st.title("Welcome to the AI translator!")

    input_lang = st.text_input("Select the Input Language")
    output_lang = st.text_input("Select the Output Language")
    input_text = st.text_input("Type the Text to Translate")

    if st.button("Translate"):
        chain = prompt | llm

        response = chain.invoke({"input_lang":input_lang, "output_lang": output_lang, "input_text": input_text})

        st.subheader("The Translated Sentence")

        st.write(response.content)

if __name__ == "__main__":
    main()