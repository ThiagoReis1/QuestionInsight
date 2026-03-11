from numpy import *
from numpy.linalg import *

matriz_temp = array(eval(input("M: ")))
lin = shape(matriz_temp)[0]
col = shape(matriz_temp)[1]
menor = 99999999999999999
indice = 0
for i in range (lin):
   for j in range (col):
      if matriz_temp[i][j] < menor:
         indice = i
         menor = matriz_temp [i][j]
      else:
        	j=j+1
			
print(indice)