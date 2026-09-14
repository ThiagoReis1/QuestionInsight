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

Esta etapa depende de um arquivo externo (o gabarito/soluções de referência do professor), que precisa ser colocado manualmente em `Etapa_4/codebench-analytics-full/input/` antes da execução — veja detalhes na seção [Dados Externos Necessários](#dados-externos-necessários) abaixo.

Para mais informações sobre a **Etapa 4**, visite o repositório relacionado: [codebench-analytics](https://github.com/Jacksonfern/codebench-analytics).

### Etapa 5: Identificação e Análise de Misconceptions

Esta etapa tem como foco a identificação de **misconceptions** (conceitos incorretos, também chamados de **MC³**) presentes nas respostas dos estudantes, por meio da análise sintática e semântica de códigos-fonte em Python.

Execute os arquivos na seguinte ordem:

1. `1_Misconceptions_Parser.py` (ou o notebook equivalente `1_Misconceptions_Parser.ipynb`) — analisa os códigos dos estudantes e detecta os tipos de misconceptions (MC³) usando `VisitorMC3.py`, gerando `output/misconceptions_resumo_por_questao.csv` e `output/misconceptions_detalhado_por_usuario.csv`.
2. `2_preparacao_analise.ipynb` — consolida os dados das etapas anteriores e gera `output/dataset_analise_questoes.csv` e `output/mapeamento_provas_questoes.json`, únicos arquivos consumidos pelo notebook seguinte.
3. `3_analise_etapas_1_7.ipynb` — gera os gráficos e métricas finais (caracterização da amostra, análise dos MC³, análise de dificuldade, correlações entre misconceptions e métricas de dificuldade/discriminação, e comparação com fatores demográficos), permitindo a construção de estratégias pedagógicas mais eficazes.

> Os notebooks antigos `2_analise_graficos.ipynb` e `3_analise_assuntos.ipynb` foram substituídos por `2_preparacao_analise.ipynb` e não fazem mais parte do fluxo do projeto.

Para mais informações sobre a **Etapa 5**, visite o repositório relacionado: [Misconceptions_Parser](https://github.com/Airtonn/Misconceptions_Parser).

---

#### `VisitorMC3.py` — Motor de detecção de Misconceptions

É o núcleo técnico da Etapa 5: um `ast.NodeVisitor` que percorre a árvore sintática (AST) de cada código-fonte Python submetido pelos alunos e detecta **21 tipos de misconceptions (MC³)**, organizados em 7 categorias (A a H). Cada tipo tem um método `get<Código>()` público, que internamente chama um método `check<Nome>()` responsável pela análise real e retorna um booleano (ou tupla, para casos que também retornam detalhes, como nomes de variáveis problemáticas).

| Código | Categoria | O que detecta |
|---|---|---|
| **A2** | Atribuição | Variável atribuída a si mesma |
| **A3** | Atribuição | Variável inicializada sem necessidade (escrita nunca lida antes de ser sobrescrita) |
| **A4** | Atribuição | Redefinição de nome *built-in* (ex.: usar `list`, `str` como nome de variável/função) |
| **A5** | Atribuição | Importação (`import`) não utilizada no código |
| **B4** | Condicionais | Comandos repetidos dentro de blocos `if`/`elif`/`else` |
| **B6** | Condicionais | Comparação booleana tentada com `while` (condição solta em vez de expressão booleana) |
| **B8** | Condicionais | Não utilização de `elif`/`else` quando seria mais apropriado |
| **B9** | Condicionais | `elif`/`else` retestando condição já verificada anteriormente |
| **B10** | Condicionais | `elif`/`else` desnecessário |
| **B11** | Condicionais | `if`s distintos com blocos de código idênticos |
| **B12** | Condicionais | Declarações `if` consecutivas e iguais realizando operações distintas |
| **C1** | Laços | Condição do `while` retestada dentro do próprio corpo do laço |
| **C2** | Laços | Laço redundante ou desnecessário |
| **C3** | Laços | Operações redundantes repetidas dentro do laço |
| **C4** | Laços | Número arbitrário/fixo de execuções de `for` no lugar de um `while` (limite configurável, padrão: `range` ≥ 50 iterações) |
| **C8** | Laços | Laço `for` cuja variável de iteração é sobrescrita dentro do corpo |
| **D4** | Escopo | Variável usada fora do escopo da função (uso de variável global dentro de função) |
| **E1** | Estruturas de dados | Verificação desnecessária de todas as combinações possíveis (`if/elif` enumerando exaustivamente) |
| **E2** | Estruturas de dados | Uso redundante ou desnecessário de listas (limite configurável, padrão: mais de 5 listas declaradas) |
| **G4** | Boas práticas | Funções/variáveis/parâmetros com nomes não significativos (muito curtos ou pouco descritivos) |
| **G5** | Boas práticas | Organização arbitrária das declarações no código |
| **H1** | Boas práticas | Declaração/expressão sem efeito (statement "solto", sem uso) |

**Parâmetros configuráveis** (definidos em `1_Misconceptions_Parser.py` e repassados ao visitor):

- `C4_MAX_ALLOWED_RANGEITER = 50` — número máximo de iterações de um `range()` fixo antes de ser sinalizado como "deveria ser `while`".
- `E2_MAX_ALLOWED_LISTS = 5` — número máximo de listas declaradas antes de sinalizar uso excessivo.
- `G4_MIN_VAR_CHRS = 4` / `G4_MIN_FNC_CHRS = 8` — tamanho mínimo de nome considerado significativo para variáveis e funções, respectivamente.
- `G4_MAX_ALLOWED_NONSIGNIFICANT = 70` — percentual máximo tolerado de nomes não significativos.

**Detalhes técnicos importantes:**
- Suporta código assíncrono (`async def`, `async for`, `async with`), tratando-os de forma equivalente às versões síncronas em todas as verificações aplicáveis.
- Usa análise de fluxo (`pending_write`/`used`) para distinguir corretamente atribuições realmente "mortas" de atribuições feitas em ramos diferentes de um `if/else` (evitando falsos positivos quando a variável é usada em pelo menos um caminho de execução).
- É um projeto em evolução: o cabeçalho do arquivo documenta um changelog detalhado (atualmente na versão **v11**) com correções de falsos positivos/negativos acumuladas ao longo do desenvolvimento.

#### `1_Misconceptions_Parser.py` / `1_Misconceptions_Parser.ipynb` — Orquestração da análise

Script responsável por rodar o `VisitorMC3` em escala sobre toda a base de códigos dos alunos.

**Entradas:**
- `../Etapa_3/output/questoes_ordenadas.csv` — lista de questões e os IDs dos usuários que a responderam.
- `../Etapa_3/output/indice_usuarios.json` e `../Etapa_2/output/usuarios_completos/` — base de códigos-fonte dos alunos (`{usuario}/codes/{prova}_{questao}.py`).

**Como funciona:**
1. Constrói um **índice em memória** `(usuario_id, questao_id) → caminho do arquivo .py`, varrendo o disco uma única vez (evita I/O repetido).
2. Para cada questão do `questoes_ordenadas.csv`, localiza os arquivos de código de cada aluno que a respondeu via lookup O(1) no índice.
3. Analisa cada código com `ast.parse()` + `VisitorMC3`, coletando os MC³ detectados (ignora silenciosamente arquivos vazios ou com erro de sintaxe/parsing).
4. Processa as questões **em paralelo** (`ThreadPoolExecutor`, padrão 3 threads) para acelerar a análise em bases grandes, com monitoramento de status por thread em tempo real (modo texto) ou barra de progresso (`tqdm`, ao rodar com o argumento `progressBar`).

**Saídas:**
- `output/misconceptions_resumo_por_questao.csv` — por questão: total de respostas e contagem de cada um dos 21 tipos de MC³.
- `output/misconceptions_detalhado_por_usuario.csv` — por par (questão, usuário): lista de MC³ detectados, total de misconceptions e número de categorias afetadas.

Ao final, o script imprime no console um relatório-resumo com tempo total de execução, velocidade de processamento (usuários/segundo), percentual de usuários com pelo menos uma misconception, top 10 MC³ mais frequentes e totais por categoria (A a H).

> `1_Misconceptions_Parser.ipynb` contém exatamente o mesmo código do `.py`, empacotado em uma única célula — útil para execução interativa no Jupyter, enquanto o `.py` é indicado para rodar via linha de comando (ex.: `python 1_Misconceptions_Parser.py progressBar`).

---

## Estrutura do Projeto

```
QuestionInsight/
├── setup_env.py                             # Cria/atualiza o ambiente virtual (.venv) e instala requirements.txt
├── prep_notebooks_for_git.py                # Limpa outputs dos notebooks antes de commitar (evita diffs gigantes no Git)
├── requirements.txt                         # Dependências Python do projeto (pandas, numpy, scipy, matplotlib, seaborn, plotly, scikit-learn, radon, tqdm)
│
├── DataSets/                                # [EXTERNO] dataset(s) bruto(s) do Codebench — baixar em codebench.icomp.ufam.edu.br/dataset/
│
├── Etapa_1/                                 # Coleta e análise inicial dos dados
│   ├── Etapa_1.ipynb
│   └── codebench-mining-tool/               # Ferramenta que extrai os dados brutos de DataSets/ (submissões, soluções, etc.)
│
├── CSVS_JO/                                 # Gerado automaticamente pela Etapa 1 (unified_solutions.csv) — não precisa criar manualmente
│
├── Etapa_2/                                 # Pré-processamento (limpeza e normalização dos dados)
│   ├── Pre_Processamento.ipynb
│   └── output/                              # Gerado pela execução (usuarios_completos/, etc.)
│
├── Etapa_3/                                 # Cálculo das métricas (dificuldade, discriminação, etc.)
│   ├── Processamento.ipynb
│   └── output/                              # Gerado pela execução (questoes_ordenadas.csv, indice_usuarios.json, etc.)
│
├── Etapa_4/                                 # Visualização e interpretação dos resultados finais
│   ├── Etapa_4.ipynb
│   ├── output/                              # Gerado pela execução
│   └── codebench-analytics-full/            # Sub-projeto (Poetry) que extrai métricas de código das soluções
│       ├── codebench_analytics/             # Código-fonte do extrator (collector/, extractor/, model/, utils/)
│       ├── input/                           # [EXTERNO] colocar aqui o codigo_solucao.csv pedido ao professor
│       └── output/                          # Gerado pela execução
│
└── Etapa_5/                                 # Identificação e análise de misconceptions (MC³)
    ├── VisitorMC3.py                        # Motor de detecção: percorre a AST do código dos alunos
    ├── 1_Misconceptions_Parser.py / .ipynb  # Roda o VisitorMC3 em escala sobre a base de códigos
    ├── 2_preparacao_analise.ipynb           # Consolida os dados das etapas anteriores
    ├── 3_analise_etapas_1_7.ipynb           # Gráficos e métricas finais
    ├── Separador_Codigo_PC3/                # Notebook auxiliar de apoio à Etapa 5
    └── output/                              # Gerado pela execução (misconceptions_resumo_por_questao.csv, etc.)
```

> Pastas marcadas com **[EXTERNO]** guardam dados que não vêm no repositório — veja a seção [Dados Externos Necessários](#3-dados-externos-necessários). As pastas `output/` de cada etapa são criadas automaticamente durante a execução, não precisam existir de antemão.

## Como Rodar o Projeto

### 1. Pré-requisitos

- Python 3.11 ou 3.12 instalado.
- Os dados externos do projeto, descritos em detalhes na seção [Dados Externos Necessários](#dados-externos-necessários) abaixo.

### 2. Criar o ambiente virtual e instalar dependências

Na raiz do projeto, rode:

```bash
python setup_env.py
```

Isso cria a pasta `.venv/` e instala tudo o que está em `requirements.txt` (pandas, numpy, scipy, matplotlib, seaborn, plotly, scikit-learn, radon, tqdm).

O script aceita os seguintes comandos (`python setup_env.py <comando>`):

| Comando | O que faz |
|---|---|
| `install` (padrão, roda mesmo sem argumento) | Cria o venv (se não existir) + instala/atualiza dependências do `requirements.txt` |
| `clean` | Apaga o venv e todas as pastas `__pycache__` do projeto |
| `help` | Mostra instruções de uso |

Depois, ative o ambiente:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows (cmd)
.venv\Scripts\activate.bat

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

> Para limpar o ambiente e recomeçar do zero: `python setup_env.py clean`

### 3. Dados Externos Necessários

Antes de rodar o projeto, você precisa colocar manualmente dois arquivos que não vêm no repositório:

- **`DataSets/`** → baixe o(s) dataset(s) do Codebench em **https://codebench.icomp.ufam.edu.br/dataset/** e coloque aqui antes de rodar a **Etapa 1**.
- **`Etapa_4/codebench-analytics-full/input/`** → solicite ao professor o arquivo `codigo_solucao.csv` (o gabarito das questões) e coloque aqui antes de rodar a **Etapa 4**.

A pasta `CSVS_JO/` não precisa de nada manual: o arquivo `unified_solutions.csv` que fica nela é gerado automaticamente pela Etapa 1, a partir do que você colocou em `DataSets/`.

> ⚠️ Sem o `codigo_solucao.csv` em `Etapa_4/codebench-analytics-full/input/`, a Etapa 4 falha ao tentar extrair as métricas de código da solução (`run_solution_command`), com o erro `❌ Arquivo de solução não encontrado`.

### 4. Ordem correta de execução

Execute os notebooks/scripts **nesta sequência**, pois cada etapa consome os arquivos de saída (`output/`) gerados pela etapa anterior:

1. **`Etapa_1/Etapa_1.ipynb`** — coleta e análise inicial dos dados (a partir de `DataSets/`).
2. **`Etapa_2/Pre_Processamento.ipynb`** — limpeza e normalização dos dados.
3. **`Etapa_3/Processamento.ipynb`** — cálculo das métricas de dificuldade, discriminação, etc.
4. **`Etapa_4/Etapa_4.ipynb`** — visualização e interpretação dos resultados finais (requer o `codigo_solucao.csv` externo em `Etapa_4/codebench-analytics-full/input/`, ver seção acima).
5. **Etapa 5** (identificação de misconceptions), nesta ordem interna:
   1. `Etapa_5/1_Misconceptions_Parser.py` (linha de comando) **ou** `1_Misconceptions_Parser.ipynb` (Jupyter) — detecta os MC³ nos códigos dos alunos.
      ```bash
      python Etapa_5/1_Misconceptions_Parser.py progressBar
      ```
   2. `Etapa_5/2_preparacao_analise.ipynb` — consolida os dados das etapas anteriores.
   3. `Etapa_5/3_analise_etapas_1_7.ipynb` — gera os gráficos e métricas finais.

### 5. Observações importantes

- Cada etapa depende dos arquivos gerados na(s) etapa(s) anterior(es) — não pule etapas nem mude a ordem.
- As pastas de saída (`Etapa_2/output`, `Etapa_3/output`, `Etapa_4/output`, `Etapa_5/output`) são geradas automaticamente durante a execução, não é preciso criá-las manualmente.
- Ao terminar, desative o ambiente virtual com `deactivate`.