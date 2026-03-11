import numpy as np
def calcular_media_ponderada():
  peso = np.array([5,4, 3, 2])
notas_input = input("digite o vetor:")
notas = np.array(eval(notas_input))
print("o vetor deve ser do mesmo tamanho")
return
soma_peso = np.sum(pesos)
soma_ponderada = np.sum(notas * pesos)
media_ponderada = soma_ponderda / soma_pesos
print(round(media_ponderada, 2))
calcular_media_ponderada