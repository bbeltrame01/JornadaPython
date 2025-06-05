# Análise de Cancelamento de Clientes 📉

Este projeto faz parte da **Jornada Python - Aula 2** e tem como objetivo realizar uma **análise de dados para entender os motivos de cancelamento de clientes** em uma empresa fictícia. Com base nos dados, buscamos propor melhorias para **reduzir a taxa de cancelamentos**.

---

## 🎯 Objetivo

- Analisar uma base de clientes;
- Verificar padrões que indicam cancelamentos;
- Tratar e limpar os dados;
- Criar gráficos interativos;
- Propor soluções com base em dados.

---

## 📁 Estrutura do Projeto

- `cancelamentos.ipynb`: Notebook com todas as etapas do projeto.
- `cancelamentos.csv`: Base de dados com informações dos clientes.
- `cancelamentos_sample.csv`: Base de dados com informações dos clientes (simplificada).

---

## 📦 Requisitos

- Python 3
- VSCode com Jupyter
- Bibliotecas:
  - `pandas`
  - `plotly`

Instalação:
```bash
pip install pandas plotly
````

---

## 🧾 Informações da Base de Dados

Colunas presentes:

* `Idade`
* `Sexo`
* `Tempo_como_cliente`
* `Frequencia_uso`
* `Ligacoes_callcenter`
* `Dias_atraso`
* `Assinatura`
* `Duracao_contrato` (Mensal, Trimestral, Anual)
* `Total_gasto`
* `Meses_ultima_interação`
* `Cancelou` (0 = Não, 1 = Sim)

---

## 🔍 Etapas do Projeto

### 1. Importação e Leitura dos Dados

```python
import pandas as pd
tabela = pd.read_csv("cancelamentos.csv")
```

### 2. Limpeza dos Dados

Remoção de dados desnecessários e vazios:

```python
tabela = tabela.drop(columns=["CustomerID"])
tabela = tabela.dropna()
```

---

## 📊 Análises Realizadas

### Taxa de Cancelamento Inicial

```python
tabela["cancelou"].value_counts(normalize=True)
```

> Resultado: **56,7% de cancelamentos**

---

### Cancelamento por Tipo de Contrato

Clientes com **contrato mensal** apresentaram quase 100% de cancelamentos.

```python
tabela.groupby("duracao_contrato").mean(numeric_only=True)
```

Remoção dos clientes com contrato mensal:

```python
tabela = tabela[tabela["duracao_contrato"] != "Mensal"]
```

> Novo índice: **46,1% de cancelamentos**

---

### Assinaturas

Distribuição equilibrada entre os planos, mas sem impacto direto sobre o cancelamento.

---

### Gráficos com Plotly

Utilizando:

```python
import plotly.express as px
```

Análises que mostraram impacto:

* **Dias de Atraso** > 20 ➜ Alta taxa de cancelamento
* **Ligações ao Call Center** > 5 ➜ Alta taxa de cancelamento

Filtrando esses dados:

```python
tabela = tabela[(tabela["dias_atraso"] < 20) & (tabela["ligacoes_callcenter"] < 5)]
```

> Resultado: **18,4% de cancelamentos**

---

## ✅ Resultados Finais

| Etapa                         | % Cancelamento |
| ----------------------------- | -------------- |
| Início                        | 56,7%          |
| Pós-tratamento 1 (Contrato)   | 46,1%          |
| Pós-tratamento 2 (Gráficos)   | 18,4%          |
| Ajustes extras (idade, gasto) | Até 4,8%\*     |

\* Ajustes extras podem não ser viáveis dependendo da realidade da empresa.

---

## 🤔 Considerações

A análise de dados é essencial para **tomadas de decisões mais inteligentes** dentro das empresas. Nem sempre reduzir cancelamentos a zero é viável, mas definir metas realistas (como 20%) pode trazer ganhos expressivos.
