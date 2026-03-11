from numpy import *
from numpy.linalg import *

matriz_notas = array(eval(input("M: ")))
lin = shape(matriz_notas)[0]
col = shape(matriz_notas)[1]
menor = 999999999999999999999999
indice = 0
for i in range (lin):
    for j in range (col):
        if matriz_notas[i][j] < menor:
            indice = i
            menor = matriz_notas [i][j]
        else:
            j=j+1
print(menor)