from numpy import *
from numpy.linalg import *

matriz_notas = array(eval(input("M: ")))
lin = shape(matriz_notas)[0]
col = shape(matriz_notas)[1]
maior = 0
indice = 0
for i in range (lin):
    for j in range (col):
        if matriz_notas[i][j] >maior:
            indice = i
            maior = matriz_notas [i][j]
        else:
            j=j+1
print(maior)