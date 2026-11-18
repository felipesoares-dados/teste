# 🩺 Análise de Indicadores de Saúde e Fatores de Risco para Diabetes (BRFSS 2015)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Hypothesis%20Testing-8CAAE6?logo=scipy&logoColor=white)
![Status](https://img.shields.io/badge/Status-EDA%20Conclu%C3%ADda-brightgreen)

## 📌 Contexto e Objetivo

O diabetes é uma das doenças crônicas mais prevalentes no mundo e representa um desafio significativo para sistemas de saúde pública. A identificação precoce de fatores clínicos e socioeconômicos associados à condição permite direcionar políticas preventivas e triagens mais eficientes.

Este projeto realiza um pipeline completo de **engenharia de dados exploratória, otimização de memória e análise estatística** sobre a base **Diabetes Health Indicators (BRFSS 2015)**, composta por **70.692 registros e 22 variáveis** (balanceada entre indivíduos com e sem diagnóstico de diabetes, com 35.346 registros por classe).

**Perguntas norteadoras da análise:**
1. Como otimizar o armazenamento e a tipagem de uma base de saúde com dezenas de milhares de registros para análises ágeis?
2. Existem diferenças estatisticamente significativas nos indicadores numéricos (como IMC e dias de saúde física/mental comprometida) entre pessoas com e sem diabetes?
3. Quais comorbidades e fatores socioeconômicos apresentam maior associação visual e proporcional com o diagnóstico?

---

## 🔍 Principais Resultados e Insights

### 1. Otimização de Dados e Performance
* **Redução de ~87% no uso de memória:** por meio da conversão estratégica de tipos (*downcasting* de variáveis numéricas para `int8` e tipagem de 15 variáveis binárias e 4 ordinais para `category`), o consumo de RAM do DataFrame caiu de **11,9 MB para 1,5 MB**.
* **Persistência em Parquet:** a base tratada e traduzida para o português foi exportada em formato `.parquet`, preservando os metadados de tipagem e acelerando o carregamento na etapa de análise exploratória.

### 2. Achados Estatísticos (Variáveis Numéricas)
* **Distribuição assimétrica:** os testes de **Kolmogorov-Smirnov** indicaram que as variáveis numéricas (`IMC`, `DiasProblemasMentais` e `DiasProblemasFisicos`) não seguem distribuição normal, justificando o uso de métricas não paramétricas e tratamento de *outliers* via **Intervalo Interquartil (IQR)**.
* **Diferença significativa no IMC:** os testes de **Levene** (variância), ***t* de Welch** e **Mann-Whitney** confirmaram diferença estatisticamente significativa ($p < 0,05$) no Índice de Massa Corporal entre os grupos com e sem diabetes.

### 3. Fatores Clínicos e Socioeconômicos (Variáveis Binárias e Ordinais)
* **Comorbidades associadas:** indivíduos diagnosticados com diabetes apresentam proporções expressivamente maiores de **pressão alta**, **colesterol alto** e histórico de doenças cardíacas ou dificuldades de locomoção.
* **Autoavaliação e demografia:** a prevalência de diabetes cresce de forma consistente conforme piora a percepção de **saúde geral** (`SaudeGeral`), avança a **faixa etária** (`FaixaIdade`) e diminuem os níveis de **escolaridade** (`Ensino`) e **faixa de renda** (`FaixaRenda`).

---

## 📊 Visualizações da Análise Exploratória

> *Dica: salve os gráficos gerados no notebook `02_eda` dentro de `reports/figures/` e atualize os caminhos abaixo.*

### Distribuição das Variáveis Numéricas (pós-tratamento de outliers)
![Distribuição Numérica](reports/figures/distribuicao_numericas.png)

### Comparativo de Indicadores Binários e Ordinais por Diagnóstico
![Indicadores Categóricos](reports/figures/comparativo_categoricas.png)

---

## 🗂️ Estrutura dos Notebooks

| Arquivo | Descrição | Técnicas Aplicadas |
| :--- | :--- | :--- |
| `01_conhecendo_a_base.ipynb` | Inspeção inicial, padronização semântica e otimização de tipos. | Tradução de schema, `category`, `int8`, exportação em `Parquet`. |
| `02_analise_exploratoria_eda.ipynb` | Estatística descritiva, tratamento de anomalias, testes de hipótese e visualização. | Assimetria/Curtose, Kolmogorov-Smirnov, IQR, Levene, Welch, Mann-Whitney, Matplotlib/Seaborn. |

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Manipulação e Armazenamento:** Pandas, NumPy, PyArrow / FastParquet
* **Estatística:** SciPy (`scipy.stats`)
* **Visualização:** Matplotlib, Seaborn
* **Ambiente:** Jupyter Notebook / VS Code

---

## 🚀 Como Reproduzir o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/diabetes-health-indicators-eda.git](https://github.com/seu-usuario/diabetes-health-indicators-eda.git)
   cd diabetes-health-indicators-eda
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os notebooks na ordem numérica (`01` → `02`).**

---

## 🗺️ Próximos Passos

* [ ] **Engenharia de Atributos e Pré-processamento:** codificação de variáveis ordinais/nominais e escalonamento para algoritmos sensíveis à escala.
* [ ] **Modelagem Preditiva:** treinamento e comparação de modelos de classificação (Regressão Logística, Random Forest, XGBoost/LightGBM).
* [ ] **Avaliação Orientada à Saúde:** otimização de limiar (*threshold*) priorizando **Recall** e **ROC-AUC** para minimizar falsos negativos na triagem de risco.

---

## 👤 Autor

**[Felipe Soares Oliveira]**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/felipe-soares-oliveira-7101a213b/)
[![GitHub](https://img.shields.io/badge/GitHub-Portf%C3%B3lio-181717?logo=github&logoColor=white)](https://github.com/felipesoares-dados)