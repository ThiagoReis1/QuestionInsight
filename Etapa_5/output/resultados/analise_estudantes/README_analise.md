# Análise PC³ — documentação de execução

Este pacote contém um único script Python, `analise_pc3.py`, que transforma um arquivo CSV bruto ou um ZIP contendo esse CSV em tabelas analíticas para um modelo logístico de efeitos aleatórios cruzados. A unidade de análise é o episódio individual identificado por estudante e questão.

## Entrada

Você pode usar `--input CAMINHO`, apontando para um `.csv` ou `.zip`; se esse argumento for omitido, o script procura automaticamente um arquivo compatível na mesma pasta de `analise_pc3.py`. O CSV deve conter, no mínimo, `usuario`, `question` e `misconceptions_detectados`, além das métricas de esforço usadas pelo modelo: `tempo_implementacao`, `num_eventos_del`, `num_tests`, `num_logic_errors`, `num_syntax_errors` e `qtd_alteracoes_codigo`. O ZIP é pesquisado recursivamente e o primeiro CSV compatível é utilizado.

## Processamento

O código identifica todos os PC³ presentes no mapa global a partir de `misconceptions_detectados`, renomeia as variáveis para nomes analíticos, calcula a elegibilidade de B8/B4/B9 por questão e aplica transformação `log1p` seguida de padronização nas seis métricas de esforço. Para cada PC³, ajusta uma regressão logística com interceptos aleatórios cruzados de estudante e questão. Os resultados incluem razões de chances, intervalos de confiança de 95%, valores de *p*, correção de Benjamini–Hochberg, componentes de variância e ICC.

> Os ICC produzidos são estimativas aproximadas pelo procedimento PQL/Laplace implementado no próprio arquivo. Para publicação, recomenda-se validar os valores em R com `glmmTMB`.

## Saída

A execução cria `resultados/` (ou o diretório indicado por `--output`) e grava os arquivos abaixo.

| Arquivo | Conteúdo |
|---|---|
| `tabela_analitica.csv` | Dados individuais, indicadores PC³, elegibilidade e variáveis renomeadas. |
| `glmm_final.csv` | Coeficientes, OR, IC95%, *p*, *p* ajustado, variâncias e ICC. |
| `resumo_variancia_icc.csv` | Uma linha por PC³ com variância entre estudantes/questões e ICC. |
| `prevalencias.csv` | N, positivos e prevalência geral e, quando aplicável, restrita a questões elegíveis. |
| `README_analise.md` | Esta documentação, gerada pelo próprio script. |

Na execução usada para validar o pacote, foram lidas **20,780 linhas** e produzidas **20,780 linhas analíticas**.

## Como executar

```bash
python analise_pc3.py
python analise_pc3.py --input dados.csv
python analise_pc3.py --input dados.zip --output resultados
```

O script requer Python 3.9 ou superior e os pacotes `numpy`, `pandas` e `scipy`.
