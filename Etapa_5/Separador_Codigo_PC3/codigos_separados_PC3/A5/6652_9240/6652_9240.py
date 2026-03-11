import numpy as up

vetor_notas = eval(input("Vetor: "))
vetor_pesos = [2,2,6,1]

media_ponderada = np.dot(vetor_notas, vetor_pesos) / sum(vetor_pesos)
media_ponderada = round(media_ponderada, 2)
print(media_ponderada)