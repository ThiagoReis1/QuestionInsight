from numpy import *
from numpy.linalg import *

n = array(eval(input("M: ")))
lin = shape(n)[0]
col = shape(n)[1]
menor = 999999999999
indice = 0
for i in range (lin):
	for j in range (col):
		if n[i][j] <menor:
			indice = i
			menor = n[i][j]
		else:
			j=j+i
print(menor)