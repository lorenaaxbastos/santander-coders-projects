# O que é a Lei Rouanet

A Lei Rouanet, oficialmente denominada Lei 8.313/91, é o principal mecanismo de incentivo à cultura no Brasil, criando o Programa Nacional de Apoio à Cultura (Pronac). Essa legislação estabelece as diretrizes para o Governo Federal disponibilizar recursos destinados à realização de projetos artístico-culturais. Originalmente, a Lei Rouanet foi concebida com três mecanismos: o Fundo Nacional da Cultura (FNC), o Incentivo Fiscal e o Fundo de Investimento Cultural e Artístico (Ficart). No entanto, o Ficart nunca foi implementado, enquanto o Incentivo Fiscal, também conhecido como mecenato, se destacou e, por vezes, é erroneamente associado como sendo a própria Lei Rouanet.

# Sobre o projeto

Este projeto oferece a oportunidade de compreender a distribuição de recursos culturais por meio da Lei Rouanet, buscando extrair insights significativos sobre a diversidade e impacto dos projetos financiados.

**Objetivo do projeto**

Realizar uma análise exploratória de dados (EDA) no conjunto de dados da Lei Rouanet (2009-2024), com o propósito de compreender padrões, tendências e insights relacionados aos projetos culturais financiados por meio dessa lei de incentivo à cultura no Brasil. Os dados utilizados são públicos, porém foram utilizados somente para fins de estudo.

## Passos do projeto

### 1. Coleta e carregamento de dados

- Obtenção do dataset da Lei Rouanet, disponibilizado pelo Ministério da Cultura [(SALIC)](https://api.salic.cultura.gov.br/doc/).
- Carregamento dos dados em um DataFrame do pandas.

### 2. Exploração inicial

- Análise preliminar para entender a estrutura do dataset, tipos de variáveis e dados disponíveis.

### 3. Limpeza e preparação dos dados

- Tratamento de valores ausentes, inconsistências ou duplicatas.
- Análise, criação e ajuste de categorias relevantes.

### 4. Análise

**4.1. Segmentação por áreas culturais**

- Classificação dos projetos por áreas e distribuição nas regiões por área.
- Verificação da distribuição dos projetos em relação às áreas ao longo dos anos.
- Análise do tempo necessário para iniciar um projeto e duração média por área.
- Exploração dos mecanismos de incentivo à cultura e enquadramentos dos projetos por área.

**4.2. Participação geográfica**

- Visualização da participação geográfica dos projetos.
- Verificação da distribuição dos projetos em relação aos estados e regiões ao longo dos anos.
- Análise do tempo necessário para iniciar um projeto e duração média por região.
- Exploração dos mecanismos de incentivo à cultura e enquadramentos dos projetos por região.

**4.3. Representividade sociocultural**

- Análise dos projetos voltados para as minorias.
- Avaliação da representatividade por área e por região geográfica.

**4.5. Distribuição de recursos**

- Análise da distribuição de recursos por área, estados, região, minoria e enquadramento.
- Exploração da distribuição de recursos financeiros ao longo do tempo.
- Identificação dos projetos que receberam a maior e menor quantidade de financiamento.
- Análise da dificuldade na captação de recursos.

**4.6. Influência de grandes projetos**

- Identificação e análise de grandes projetos que receberam um montante significativo de financiamento. 

### 5. Conclusão

- Resumo das principais descobertas do projeto.
- Identificação de padrões interessantes, tendências ao longo do tempo e insights valiosos para as partes interessadas e tomadores de decisão.

## Ferramentas utilizadas

- Python (`numpy`, `pandas`, `geobr`, `matplotlib`)
- Jupyter Notebook para documentação e visualização interativa.

## Fontes 

- [Instrução normativa MINC nº 1, de 10 de abril de 2023](https://www.conjur.com.br/dl/in/instrucao-normativa-cultura-oab-rouanet.pdf)
- [Portal do Incentivo](https://portaldoincentivo.com.br/visitors/incentive_laws/1)
- [ntendendo a Lei Rouanet, por Carolina Bassin](https://www.crc.org.br/_eventos/2018/897.pdf)