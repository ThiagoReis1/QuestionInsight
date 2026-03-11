import numpy as np

notas = eval(input("notas:"))
peso = [3,5,1]

ponderada = np.dot(notas, peso) / sum(peso)
ponderada = round(ponderada, 2)