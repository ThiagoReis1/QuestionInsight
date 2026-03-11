import numpy as np

notas = eval(input("notas: "))
pesos = [2, 1, 5]

notas_array = np.array(notas)
pesos_array = np.array(pesos)

media_ponderada = np.sum(notas_array * pesos_array)/ np.sum(pesos_array)

print(round(media_ponderada,2))