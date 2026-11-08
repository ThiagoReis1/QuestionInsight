# Pipeline automático de métricas e PC³

## Amostra e regras
- Questões analisadas: 630 (mínimo 16 respostas; casos completos para métricas: 630).
- Métricas definidas no projeto: 13 (MD1–MD12 originais + MD13 nova).
- Métricas observadas usadas na seleção: 10 (MD5, MD8 e MD10 ficam para descrição/auditoria; MD13 = MD10 − MD9).
- Removidas automaticamente por redundância/colinearidade: MD3, MD2. Regra: remover, entre as métricas em pares com |Spearman rho| >= 0.9, a de maior VIF; depois remover máximo VIF enquanto > 10.0.
- Removidas por MSA < 0,50: nenhuma.
- O crosswalk renumeracao_metricas.csv preserva MD1–MD13; a seleção indica somente mantida, removida por colinearidade, derivada ou não estimável.

## Fatorabilidade final
- KMO=0.847; MSA mínimo=0.621; Bartlett chi²(28)=3197.98, p <0,001; determinante=0.00601992.
- Limiares orientativos: KMO >= 0,60 e Bartlett p < 0,05.

## Componentes
Análise paralela reteve 2 componente(s) (500 simulações; percentil 95%). Cargas em pca_cargas.csv. A hipótese teórica de três eixos não é imposta: comparar com os dados e justificar no artigo.

## MD13 — Eventos sem deleções
MD13 = MD10 − MD9. A coluna discriminacao não pertence ao conjunto MD e não entra nas análises.

## GLMM
Status: validado separadamente em Python com modelo Bayesiano logístico de interceptos aleatórios cruzados (ver seção QP5); resultados antigos de glmmTMB são apenas arquivo diagnóstico. Desfechos PC³ com pelo menos 50 ocorrências, efeitos aleatórios cruzados por estudante e questão, seis preditores existentes no pipeline, filtro completo e elegibilidade atual de B8/B4/B9. Conferir convergência e N por desfecho antes de publicar.

## Nota metodológica
As métricas são agregadas por questão; o filtro 16+ é aplicado por questão. Correlação é Spearman sobre os valores originais; os postos decrescentes padronizados são exportados para análise de componentes. Remoção automática por maior VIF é uma regra operacional reproduzível, não uma decisão teórica.
