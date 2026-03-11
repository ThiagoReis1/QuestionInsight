import numpy as np
notas = eval(input("notas: "))
peso = [3,4,2,1,4,5]
MP = np.dot(notas,peso)/sum(peso)
MP = round(MP,2)
print(MP)