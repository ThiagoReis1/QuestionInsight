import numpy as np

vetor_notas = eval(input("vetor: "))
vetor_peso = [1,2,3]

media_ponderada = np.dot(vetor_notas, vetor_peso) / sum(vetor_peso)
media_ponderada = round(media_ponderada, 2)
print(media_ponderada)


