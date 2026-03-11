import numpy as np

notas = eval(input("notas:"))
peso = [5,4,3,2]

media = np.dot(notas, peso) / sum(peso)
media = round (media, 2)
print(media)