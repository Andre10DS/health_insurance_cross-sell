# Health Insurance Cross-Sell

## This project aims to order a potential client list by propensity score
O projeto refere-se a uma empresa ficticia de seguros de vida que deseja realizar uma estratégia de cross-sell para um novo produto de seguro veicular.

Para executar a estratégia será desenvolvido um modelo de ranqueamento de clientes que apresetam potecial para adquirir o seguro veicular.

O projeto utiliza uma base de dados de clientes de uma empresa de seguros de saúde para predizer se os novos clientes tem potencial para adiquirir o novo produto.

A estratégia de cross-sell é uma abordagem de marketing e vendas que visa oferecer produtos ou serviços complementares aos clientes, com base em suas compras ou preferências anteriores. Isso não apenas aumenta a receita da venda atual, mas também pode melhorar a satisfação do cliente, pois ele percebe que a empresa está atendendo às suas necessidades e oferecendo soluções abrangentes.

# 1. Business Problem.
A empresa tem restrições de capacidade e custo para realizar a abordagem em toda a base de novos. Desta forma, deve ser criado alguma ferramenta que traga mais precisão, reduza o tempo e o custo do processo de venda.


# 2. Business Assumptions.

1. A empresa tem restrições de capacidade e, desta forma, não consegue atender todos os novos clientes da base.
2. O resultado deverá ser entregue em google sheets.
3. O contato com os clientes será realizada por meio de ligações.
4. A empresa tem a capacidade de realizar ligações para cerca de 20% da base de novos clientes (76222).

# 3. Objetivo.

1. Entregar um modelo de ranqueamento que evidencie os clientes com maiores probabilidades de serem convertidos em venda.
2. O modelo deverá ser disponibilizado em planilhas do google sheets.

# 4. Planejamento da solução.
## 4.1 Produto final.
  - Modelo de ranqueamento que poderá ser consultado via API
  - Construção de uma planilha capaz demostrar o score de probabilidade de cada cliente com base nos dados preenchidos.
    
## 4.2 Ferramentas.
  1. Jupyter notebook;
  2. VSCode;
  3. Render;
  4. Google sheets apps scripts;
  5. Git e Github;
  6. SweetViz;
  7. Python 3.9.17
  8. Flask
  9. Algoritmos KNN, Regressão Logistica e LightGBM
  
## 4.3 Processo.
### 4.3.1. Estratégia da solução.

**Step 01. Data Description:**

  - Realizar a descrição das colunas.
  - Maperar as hipoteses.
  - Ajustar o nome das colunas.
  - Checar os tipos de dados e verificar a necessidade de alteração.
  - Checar os NA e realizar e o replace caso necessário.
  - Relizar a descrição estatisticas dos dados númericos e avaliar distorções.

**Step 02. Feature Engineering:**

  - Realizar a construção de novos features ou o ajuste dos dados daquelas existentes.

**Step 03. Data Filtering:**

  - Filtragem de dados que possuem restrições de negócio. (Nesta base de dados não foi verificado a necessidade de realizar tal ação)

**Step 04. Exploratory Data Analysis:**

  - Realizar a análise univariada.
  - Realizar a análise bivariada.
  - Realizar a análise multivariada.
  - Estudo das correlações de person e cramer v.

**Step 05. Data Preparation:**

  - Realizar a separação dos dados de treino e validação.
  - Padronizar os dados númericos com a distribuição normal
  - Realizar a reescalar dos dados.
  - Realizar o encooding dos dados categóricos.
  - Aplicar transormações de natureza.
  - Realizar as transformações nos dados de validação.

**Step 06. Feature Selection:**

  - Aplicar tecnicas de seleção de features com base na relevancia e importância para o desenvolvimento do projeto.
  - Verificar se as features selecionadas pela técnica tem alguma relação com as analises realizadas na EDA.
  - Selecionar as features com maior relevancia para o modelo.

**Step 07. Machine Learning Modelling e Hyperparameter Fine Tunning:**

  - Criar bases de possíveis valores de hiperparametros para cada modelo. Foram utilizados os modelos KNN, Regressão logistica e LightGBM.
  - Criar o algoritmode stratificação da base de treino para realizar o cross validation.
  - Treinar os modelos usando o algoritmo Bayseian Search para evidenciar os melhores parametros do modelo.
  - Testar o modelo com os dados de validação.
  - Avaliar os resultados obtidos com cada modelo e selecionar aquele com melhor performance levando em consideração também o desempenho processual e restrições de estrutura e custo.
  - Juntar os dados de treino e validação e realizar um novo treinamento do modelo escolhido.
  - Aplicar o modelo escolhido nos dados de teste e cruzar performance atingida com a performance do modelo em treinamento.

**Step 08. Convert Model Performance to Business Values:**

  - Desdobrar os resultados do modelo em performance de negócio.
  - Traduzir a performance em retorno financeiro para a empresa. 

**Step 10. Deploy Modelo to Production:**

  - Criar uma classe do modelo para realizar todo pipeline de dados
  - Criar uma API para rodar e consultar o modelo criado.
  - Realizar o teste da API localmente para verificar a necessidade de ajuste.
  - Exportar o modelo e API para o Git.
  - Publicar o modelo e API no Render.
  - Criar o script de consulta no google sheets atraves do Apps scripts.

# 4. Top 3 Data Insights

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve
