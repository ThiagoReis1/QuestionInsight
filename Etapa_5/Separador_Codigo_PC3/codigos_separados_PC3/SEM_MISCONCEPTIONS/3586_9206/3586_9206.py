# Importação necessária
import numpy as np

# Vetor de anéis acertados (exemplo)
aneis_acertados = [1, 3, 2, 1, 4, 2, 3, 1]

# Inicialização da variável acumuladora para a pontuação total
pontuacao_total = 0

# Iteração sobre os anéis acertados
for anel in aneis_acertados:
    if anel == 1:
         pontuacao_total += 100
      elif anel == 2:
         pontuacao_total += 60
      elif anel == 3:
         pontuacao_total += 20

# Imprime a pontuação total do jogador
print("Pontuação total:", pontuacao_total)