# Análise e Predição de Preços de Bolsas de Estudo

## Descrição do Projeto
Este projeto faz parte do meu aprendizado em Data Science e tem como objetivo analisar um conjunto de dados de bolsas de estudo e criar um modelo preditivo para estimar seus preços com base em diversas características.

Durante o desenvolvimento, explorei conceitos de análise exploratória de dados (EDA), engenharia de dados e machine learning. No entanto, por ser meu primeiro projeto, ainda existem desafios e pontos a melhorar.

## Dataset
O conjunto de dados utilizado contém 50.000 registros e foi obtido de uma fonte pública. As colunas do dataset incluem:

- **Brand** (Marca)
- **Material**
- **Size** (Tamanho)
- **Compartments** (Número de compartimentos)
- **Laptop Compartment** (Possui compartimento para notebook?)
- **Waterproof** (Resistente à água?)
- **Style** (Estilo)
- **Color** (Cor)
- **Weight Capacity (kg)** (Capacidade de peso em kg)
- **Price** (Preço)

Houve necessidade de tratamento de dados, remoção de duplicatas e tratamento de valores ausentes, mas ainda há desafios com ruídos e inconsistências.

## Tecnologias Utilizadas
- **Linguagens e Ferramentas**: Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn
- **Ambiente de Desenvolvimento**: JupyterLab, VSCode
- **Visualização de Dados**: Power BI

## Modelagem Preditiva
Utilizei um modelo de regressão para prever o preço das bolsas, mas os resultados ainda precisam de melhorias. Métricas atuais:

- **MAE (Mean Absolute Error)**: 33
- **R² Score**: -0.5

Os resultados indicam que o modelo ainda não está performando bem, possivelmente devido a ruído nos dados ou escolha de features e hiperparâmetros subótimos.

## Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute os notebooks no JupyterLab ou VSCode

## Desafios e Melhorias Futuras
### Dificuldades Enfrentadas:
- A limpeza dos dados ainda precisa ser refinada para reduzir ruídos
- O modelo preditivo apresenta um erro alto e baixa precisão
- Identificação das features mais relevantes para a previsão
- Melhorar a escolha de modelos e técnicas de ajuste de hiperparâmetros

### Melhorias Futuras:
- Aplicar técnicas mais avançadas de tratamento de outliers e feature engineering
- Testar diferentes algoritmos de regressão, como Random Forest ou XGBoost
- Avaliar normalização dos dados para melhorar a performance
- Refinar o pipeline de Machine Learning para otimização dos resultados

## Conclusão
Este projeto foi um excelente aprendizado inicial para mim, permitindo que eu colocasse em prática conceitos fundamentais de Data Science. Ainda há muito a evoluir, mas estou constantemente buscando melhorias e aprendendo com os desafios.

Caso tenha sugestões ou queira contribuir, fique à vontade para entrar em contato ou abrir uma issue no repositório!




