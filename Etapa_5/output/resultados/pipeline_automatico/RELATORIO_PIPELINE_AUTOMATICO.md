# Pipeline automático de métricas e PC³

## Amostra e regras
- Questões analisadas: 617 (mínimo 16 respostas; casos completos para métricas: 617).
- Métricas iniciais: 10 (MD5, MD8 e MD10 compostas não entram; MD14 = MD10 − MD9).
- Removidas automaticamente por redundância/colinearidade: MD3, MD2. Regra: remover, entre as métricas em pares com |Spearman rho| >= 0.9, a de maior VIF; depois remover máximo VIF enquanto > 10.0.
- Removidas por MSA < 0,50: nenhuma.
- Métricas finais consecutivamente renumeradas em renumeracao_metricas.csv, com codigo_origem, codigo_final, fórmula, unidade, nível e fonte; dicionario_metricas.csv preserva o significado oficial de MD1--MD14.

## Fatorabilidade final
- KMO=0.844; MSA mínimo=0.610; Bartlett chi²(28)=3140.19, p <0,001; determinante=0.0059353.
- Limiares orientativos: KMO >= 0,60 e Bartlett p < 0,05.

## Componentes
Análise paralela reteve 2 componente(s) (500 simulações; percentil 95%). Cargas em pca_cargas.csv. A hipótese teórica de três eixos não é imposta: comparar com os dados e justificar no artigo.

## MD13 / IRT 2PL
Status: formalmente excluída: o ajuste 2PL anterior não convergiu; MD13-IRT não entra nas análises.. O 2PL é tentado com mirt; itens sem variação observada recebem a não estimável, não um valor artificial. Revisar diagnósticos, erro-padrão, ajuste e pressupostos antes de reportar.

## GLMM
Status: validado separadamente em Python com modelo Bayesiano logístico de interceptos aleatórios cruzados (ver seção QP5); resultados antigos de glmmTMB são apenas arquivo diagnóstico. Desfechos PC³ com pelo menos 50 ocorrências, efeitos aleatórios cruzados por estudante e questão, seis preditores existentes no pipeline, filtro completo e elegibilidade atual de B8/B4/B9. Conferir convergência e N por desfecho antes de publicar.

## Nota metodológica
As métricas são agregadas por questão; o filtro 16+ é aplicado por questão. Correlação é Spearman sobre os valores originais; os postos decrescentes padronizados são exportados para análise de componentes. Remoção automática por maior VIF é uma regra operacional reproduzível, não uma decisão teórica.
