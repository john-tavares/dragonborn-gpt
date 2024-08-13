import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import os
import utils

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("🐉 Dragonborn GPT")
st.caption("🧠 Inteligência Artificial treinada para tirar dúvidas sobre The Elder Scrolls V: Skyrim.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Dovahkiin, qual é a sua dúvida?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    docs = PineconeVectorStore(embedding=OpenAIEmbeddings(), index_name=os.getenv('INDEX_NAME')).similarity_search(prompt)
    messages = utils.main_prompt+st.session_state.messages
    if len(docs) > 0:
        messages += utils.database_message(docs)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)