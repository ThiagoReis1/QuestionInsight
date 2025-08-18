# QuestionInsight

Este projeto é uma análise e avaliação de questões de testes, utilizando múltiplas métricas para medir aspectos como dificuldade, discriminação, acerto por acaso e muito mais. Ideal para educadores, psicometristas e desenvolvedores de testes que buscam otimizar a eficácia e o desempenho de suas questões.

## Etapas do Projeto

### Etapa 1: Análise Inicial e Coleta de Dados
Execute o notebook `Etapa_1.ipynb`. Nesta etapa, você realizará a coleta e análise inicial dos dados das questões, preparando o ambiente para as próximas etapas. O objetivo é entender os aspectos básicos das questões a partir das informações fornecidas. 

Para mais informações sobre a **Etapa 1**, visite o repositório relacionado: [codebench-mining-tool](https://github.com/marcosmapl/codebench-mining-tool).

### Etapa 2: Pré-processamento dos Dados
Execute o notebook `Pre_Processamento.ipynb`. Aqui, os dados serão limpos e transformados. Esta etapa envolve a remoção de dados inválidos, normalização de formatos e preparação dos dados para análises mais avançadas.

### Etapa 3: Processamento dos Dados
Execute o notebook `Processamento.ipynb`. Nessa fase, você aplicará as métricas de análise nas questões, como dificuldade, discriminação e outras estatísticas relacionadas. O objetivo é avaliar como as questões se comportam em relação aos parâmetros definidos.

### Etapa 4: Resultados Finais e Avaliação
Execute o notebook `Etapa_4.ipynb`. Nesta última etapa, você visualizará os resultados finais das análises. A etapa foca na interpretação dos resultados das métricas calculadas, fornecendo insights detalhados sobre o desempenho das questões de teste.

Para mais informações sobre a **Etapa 4**, visite o repositório relacionado: [codebench-analytics](https://github.com/Jacksonfern/codebench-analytics).

### Etapa 5: Identificação e Análise de Misconceptions

Execute os notebooks `1_Misconceptions_Parser.ipynb` e `2_analise_graficos.ipynb`. Esta etapa tem como foco a identificação de **misconceptions** (conceitos incorretos) presentes nas respostas dos estudantes, por meio da análise sintática e semântica de códigos-fonte.

A ferramenta realiza parsing dos códigos utilizando técnicas de visita à árvore sintática (via `VisitorMC3.py`), detectando padrões recorrentes de erro. Após isso, são gerados gráficos e métricas que ajudam a visualizar e interpretar esses equívocos, permitindo a construção de estratégias pedagógicas mais eficazes.

Para mais informações sobre a **Etapa 5**, visite o repositório relacionado: [Misconceptions_Parser](https://github.com/Airtonn/Misconceptions_Parser).

