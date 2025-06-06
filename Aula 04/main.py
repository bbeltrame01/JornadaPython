# Título
# Input do chat
# A cada mensagem enviada:
  # mostra a mensagem que o usuário enviou
  # enviar essa mensagem para a IA responder
  # aparece na tela a resposta da IA

# streamlit
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Carrega variáveis de ambiente do .env
_ = load_dotenv(find_dotenv())

# Obtém a API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
  raise ValueError("A API Key não foi encontrada. Verifique o .env ou as variáveis de ambiente.")

# Inicializa client OpenAI
client = OpenAI()

st.title("Hashzap")

user_message = st.chat_input("Digite sua mensagem")

# Session state para armazenar mensagens
if not "messages" in st.session_state:
  st.session_state["messages"] = []


if user_message:
  # Exibir a mensagem do usuário no chat
  message = {
    "role": "user",
    "content": user_message,
  }
  st.session_state["messages"].append(message)


  # Exibir a resposta da IA
  model_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=st.session_state["messages"],
  )
  ai_response = model_response.choices[0].message.content
  response = {
    "role": "assistant",
    "content": ai_response,
  }
  st.session_state["messages"].append(response)

  # Exibir todas as mensagens do chat
  for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])