import numpy as np

notas = eval(input("digite o valor das notas: "))

pesos = [3, 2, 4, 1, 3]

media_ponderada = np.dot(notas, pesos) / sum(pesos)

media_ponderada = round(media_ponderada, 2)

print(media_ponderada)