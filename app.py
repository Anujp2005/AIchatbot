from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## enviroment variable call

#os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

#Langsmith tracking

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## creating chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework

st.title("AI chat Bot")
col1, col2 = st.columns([4, 1])

with col1:
    input_text = st.text_input("Search the topic you want", label_visibility="collapsed")

with col2:
    send = st.button("➡️")

if send and input_text:
    st.write(f"You: {input_text}")
# open AI LLM call

llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()

##  chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

