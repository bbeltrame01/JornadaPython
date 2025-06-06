# 🤖 Hashzap – Chat com IA via OpenAI e Streamlit

Este projeto faz parte da Jornada Python - Aula 4, uma aplicação simples de chat usando [Streamlit](https://streamlit.io/) e a API da OpenAI. Ele permite que usuários enviem mensagens e recebam respostas de um modelo de linguagem, em uma interface estilo chat.

## 🧠 Funcionalidades

- Interface interativa com `streamlit.chat_input`
- Armazenamento de histórico de conversas usando `st.session_state`
- Integração com a API da OpenAI (modelo `gpt-4o-mini`)
- Carregamento automático da chave da API via `.env`

## 📦 Requisitos

- Python 3
- Conta na [OpenAI](https://platform.openai.com/) com chave de API
- Biblotecas:
  - `streamlit`
  - `openai`
  - `python-dotenv`
```bash
pip install streamlit openai python-dotenv
````

## 🛠️ Como rodar

1. Clone o repositório ou copie os arquivos para um diretório local.
2. Crie um arquivo `.env` com a sua chave da OpenAI:

```
OPENAI_API_KEY=sua-chave-aqui
```

3. Execute o app com:

```bash
streamlit run main.py
```

4. Acesse no navegador: `http://localhost:8501`

## 🗂 Estrutura do Projeto

```
.
├── main.py         # Script principal do app
├── .env            # Arquivo com variável de ambiente da API Key (não incluído no repositório)
└── README.md       # Este arquivo
```

## 📌 Observações

* O modelo utilizado é o `gpt-4o-mini`, mas você pode alterar para outro modelo compatível, como `gpt-4`, `gpt-3.5-turbo`, etc.
* Certifique-se de não expor sua chave de API em repositórios públicos.
