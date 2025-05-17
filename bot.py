import datetime
import os
from langchain_groq import ChatGroq
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import StructuredOutputParser
import streamlit as st

# Get API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)


def answer_question(question, data):
    prompt_system = SystemMessagePromptTemplate.from_template(
        """
        You are Tejas Agarwal, CEO of Truwealth. You are answering customer queries. Use the data provided to answer the question. dont make up any information. answer only if you are sure. 
        If something is not mentioned in the data, say you don't know and that you will find out and get back to them. 
        Always answer in the same language as the question. Type like a human. Be casual and friendly. Dont write huge paragraphs. 
        Keep the answer short and concise. mostly around 40 words max.
        
        """
    )

    prompt_human = HumanMessagePromptTemplate.from_template("""
    here is the data you have. 
    {data}
    here is the question. 
    {question}
    """)

    prompt = ChatPromptTemplate.from_messages([prompt_system, prompt_human])
    chain = prompt | llm

    response = chain.invoke({"question": question, "data": data})
    return response.content


# Remove the direct file reading from here since we'll handle it in app.py
















