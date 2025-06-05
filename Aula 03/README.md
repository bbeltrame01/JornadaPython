# Classificação de Score de Clientes com Machine Learning 💳📊

Este projeto faz parte da **Jornada Python - Aula 3** e tem como objetivo aplicar técnicas de **aprendizado de máquina (ML)** para prever o **score de crédito de clientes** com base em uma base de dados de 100.000 clientes de um banco fictício.

---

## 🎯 Objetivo

- Prever o score de crédito dos clientes (Poor, Standard, Good);
- Treinar e comparar dois modelos de classificação;
- Identificar os atributos mais relevantes para definição do score;
- Fornecer insights úteis para tomada de decisão.

---

## 📁 Estrutura do Projeto

- `clientes.csv`: Base de dados com 100.000 registros.
- `previsoes.ipynb`: Notebook com todas as etapas do projeto.
- `novos_clientes.csv`: Base de dados com 3 novos registros para previsão.

---

## 📦 Requisitos

- Python 3
- Bibliotecas:
  - `pandas`
  - `scikit-learn`

Instalação:
```bash
pip install pandas scikit-learn
````

---

## 🧾 Etapas do Projeto

### 1. Importação da Base de Dados

```python
import pandas as pd
tabela = pd.read_csv("clientes.csv")
```

A base contém 25 colunas e 100.000 linhas com dados pessoais e financeiros dos clientes.

---

### 2. Tratamento dos Dados

* Verificação de valores vazios.
* Conversão de colunas do tipo texto (`object`) para numérico com `LabelEncoder`.

```python
from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

for coluna in tabela.columns:
  if tabela[coluna].dtype == 'object' and coluna != 'score_credito':
    tabela[coluna] = codificador.fit_transform(tabela[coluna])
```

---

### 3. Separação de Treino e Teste

Separar os dados em **variáveis preditoras (X)** e **alvo (y)**, e em conjuntos de treino/teste:

```python
from sklearn.model_selection import train_test_split

X = tabela.drop(['score_credito','id_cliente'], axis=1)
y = tabela["score_credito"]

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
```

---

## 🤖 Modelos Utilizados

### 1. Árvore de Decisão

```python
from sklearn.tree import DecisionTreeClassifier
modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(X_treino, y_treino)
```

### 2. KNN (K-Nearest Neighbors)

```python
from sklearn.neighbors import KNeighborsClassifier
modelo_knn = KNeighborsClassifier()
modelo_knn.fit(X_treino, y_treino)
```

---

### 4. Avaliação dos Modelos

Utilizando a métrica de **acurácia**:

```python
from sklearn.metrics import accuracy_score

previsao_arvore = modelo_arvore.predict(X_teste)
previsao_knn = modelo_knn.predict(X_teste)

print("Acurácia Árvore:", accuracy_score(y_teste, previsao_arvore))  # ~82%
print("Acurácia KNN:", accuracy_score(y_teste, previsao_knn))        # ~73%
```

> ✅ Modelo escolhido: **Árvore de Decisão (82%)**

---

### 5. Importância das Variáveis

Após treinar a árvore, podemos verificar as **características mais relevantes**:

```python
import matplotlib.pyplot as plt

importancias = modelo_arvore.feature_importances_
colunas = X.columns

plt.barh(colunas, importancias)
plt.xlabel("Importância")
plt.title("Importância das Variáveis para Score")
plt.show()
```

Principais atributos:

* `divida_total`
* `mix_credito`
* `juros_empréstimo`

---

## ✅ Conclusão

* Com uma **acurácia de 82%**, o modelo consegue prever bem o score dos clientes;
* A análise dos dados é essencial para entender e melhorar o negócio;
* Com esse modelo, o banco pode tomar decisões mais assertivas sobre **crédito, empréstimos e limites**.
