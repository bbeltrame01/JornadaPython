# Projeto de Automação com Python 🐍

Este projeto faz parte da **Jornada Python - Aula 1**, com o objetivo de automatizar o cadastro de produtos em um sistema web utilizando Python.

## 🚀 Objetivo

Automatizar tarefas repetitivas como o preenchimento de formulários com centenas de registros, usando Python e a biblioteca `pyautogui`.

Imagine ter que cadastrar 264 produtos manualmente — este projeto mostra como o Python pode fazer isso por você, controlando mouse e teclado como se fosse um usuário real.

---

## 📂 Estrutura do Projeto

- `produtos.csv`: Base de dados com os produtos (código, marca, tipo, preço, custo e observações).
- `auto_fill.py`: Script principal de automação.
- `pegar_posicao.py`: Script auxiliar para capturar posições do mouse na tela.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3**
- [pandas](https://pandas.pydata.org/)
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/)

Instalação das dependências:
```bash
pip install pandas pyautogui
````

---

## 📊 Importação e Visualização dos Dados

Utilizamos o `pandas` para ler e inspecionar a base de dados:

```python
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)
```

---

## 🖱️ Automação com PyAutoGUI

### Comandos Utilizados

* `pyautogui.press()` – Pressiona teclas
* `pyautogui.write()` – Digita textos
* `pyautogui.click()` – Clica em posições específicas
* `pyautogui.scroll()` – Usa a rolagem do mouse
* `pyautogui.PAUSE = 1` – Tempo entre os comandos

### Capturando a Posição do Mouse

```python
import pyautogui
import time

time.sleep(5)
print(pyautogui.position())
```

> Use este script para descobrir as coordenadas corretas para os cliques no seu monitor.

---

## 🔁 Lógica da Automação

1. Abrir o navegador e acessar o site.
2. Realizar login (usuário/senha).
3. Iterar linha por linha na base de dados:

   * Preencher os campos no formulário.
   * Validar o campo de observação (se estiver vazio, ignorar).
   * Enviar o formulário.
4. Repetir até o fim dos registros.

### Exemplo de estrutura com `for`:

```python
for i in range(len(tabela)):
    pyautogui.click(x=..., y=...)  # Clique no campo
    pyautogui.write(str(tabela.loc[i, "codigo"]))
    ...
```

---

## ✅ Conclusão

Com essa automação você ganha:

* Agilidade no processo
* Redução de erros manuais
* Mais produtividade (deixa a automação rodando enquanto realiza outras tarefas)
