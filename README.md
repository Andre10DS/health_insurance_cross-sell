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

A análise exploratória dos dados, juntamente com as analises descritivas, permite um melhor entendimento dos dados e possibilita a verificação de insights que possam ser utilizados pelos negócios. Os top três insights foram:

H1: Pessoas com mais de 40 anos são mais propensas a contratar um seguro de veículo.

** Colocar img Percentual_acima_e_abaixo_de_40**

Hipótese verdadeira: Pessoas com mais de 40 anos são mais propensas a contratar um seguro. Verificou-se que 63,22% das pessoas que declararam ter interesse em contratar o seguro tinham 40 anos ou mais.

H2: Os homens se interessaram mais pela proposta do que as mulheres.

** Colocar img Homens_mais_interessados_na_proposta**

Hipótese verdadeira: Os homens são mais interessados em adquirir a proposta do que as mulheres. Cerca de 61,2% da base que respondeu positivo eram homens.


H3: Dos clientes interessados, tinham carros com mais de dois anos.

** Colocar img Clientes_interessados**

Hipótese falsa: A demanda ocorre para veículos com idade entre 1 e 2 anos. Em relação à base de dados, esse tempo é considerado "mediano". O período de 1 a 2 anos concentra 74% dos interessados.


# 5. Machine Learning Model Applied

Para o desenvolvimento do projeto foram utilizadados três algoritmos de machine learning sendo eles o KNN, Regressão logística e LightGBM. Para escolher o melhor modelo para o projeto foram seguindos as seguintes etapas:

1. Realização das escolhas dos melhores parametros de cada modelo utlizando o metodo Bayseian Search com validação cruzada sobre os dados de treino utilizando o K top de 20000 amostras.
2. Após a verificação dos melhores parametros, cada modelo foi treinado com os dados de treino e verificado a performance sobre os dados de validação.
3. Foram obtidos as performances de cada modelo por percentual da base. As metricas utilizadas foram a precision k_top e a recall K_top. Segue abaixo os resultados obtidos:

Precision@k: conta quantas previsões foram corretas até k e divide por todas as previsões feitas até k.

|Precision|K-nearest neighbors|Logistic regression |LightGBM |
|----------------|:----------:|:-------------------:|:---------------------------------:|
| 10% (6097) | 0.32 | 0.30 | 0.38 |
| 20% (12195) | 0.32 | 0.28 | 0.35 |
| 30% (18293) | 0.29 | 0.26 | 0.31 |
| 40% (24391)| 0.26 | 0.27 | 0.28 |

Recall@k: conta quantas previsões foram corretas até k e divide por todos os exemplos verdadeiros.

|Recall|K-nearest neighbors|Logistic regression |LightGBM |
|----------------|:----------:|:-------------------:|:---------------------------------:|
| 10% (6097) | 0.26 | 0.24 | 0.31 |
| 20% (12195) | 0.50 | 0.46 | 0.57 |
| 30% (18293) | 0.72 | 0.65 | 0.78 |
| 40% (24391)| 0.87 | 0.88 | 0.92 |

O modelo que apresentou a melhor performance foi o LightGBM.

# 6. Machine Learning Modelo Performance

Nesta etapa um dos modelos de ML utilizados na fase de treino foi selecionada e avalida sobre dados de teste para simular o ambiente de produção. O modelo selecionado para implementação foi o LightGBM. Segue abaixo os resultados obtidos:

|Precision|LightGBM - Treino|LightGBM - Teste |
|----------------|:----------:|:-------------------:|
| 10%  | 0.38 | 0.38 |
| 20%  | 0.35 | 0.35 |
| 30%  | 0.31 | 0.31 |
| 40% | 0.28 | 0.28 |


|Recall|LightGBM - Treino|LightGBM - Teste |
|----------------|:----------:|:-------------------:|
| 10%  | 0.31 | 0.31 |
| 20%  | 0.57 | 0.57 |
| 30%  | 0.78 | 0.78 |
| 40% | 0.92 | 0.92 |

Os resultados obtidos com os dados de teste mostraram-se próximos aos dados de treino, sendo que para se possa verificar alguma diferença é necessário ampliar as casas decimais.

A curva de ganho acumulado é outra ferramenta que pode demonstar a performance do modelo. Ela representa quantas clientes interresados estão em cada percentual da base ordenada pelo modelo. Um exemplo é quando analisamos que nos 20% da base ordenada se encontra aproximadamente 57% dos clientes interessados.


A curva de lift demonstra o quando o modelo utilizada é mais eficiente do que o modelo de média. Desta forma, ao analisa o ponto 2 verificamos que ele é quase 3 vezes melhor do que o modelo de média.


# 7. Business Results

A base de teste foi de 76222 sendo que destes um número de 9342 mostraram-se interessados. O custo de aquisição de clientes (CAC) com base no site xxxxx é de  $ 500 para seguros de veículo e o LTV é de 500 segundo o site yyyyy. Desta forma, chegamos ao seguintes cenários para cada percentual da base de novos clientes:

|% da base|@k pessoas interessadas|Total de pessoas interessadas | Lucro - modelo atual | Lucro - novo modelo| Ganho / perda |
|----------------|:----------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|
| 10%  | 2969 | 9342	| 85,990 | 1,103,390 | 1,017,400 |
| 20%  | 5377 | 9342	| 171,980  | 1,926,280 | 1,754,300 |
| 30%  | 7304 | 9342	| 257,970  | 2,508,670 | 2,250,700 |
| 40% | 8636 | 9342	| 343,960  | 2,793,560 | 2,449,600 |
| 50% | 9250 | 9342	| 429,950  | 2,719,450 | 2,289,500 |

Conforme as premissas de negócio, a estrutura terá a capacidade de atendimento de somente 20% (15244) da base de novos clientes. Desta forma, com a utilização do modelo contruído neste projeto o lucro sairia de $ 171,980 para $ 1,926,280 representando um ganho de $ 1,754,300.

### Entrega - Planilha Google Sheets

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve
