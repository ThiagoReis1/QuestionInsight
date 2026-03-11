import numpy as np

notas = eval(input("Digite o vetor de notas: "))
pesos = [1, 2, 3]

media_ponderada = np.dot(notas , pesos)/np.sum(pesos)

media_arredondada = round(media_ponderada, 2)

print(media_arredondada)