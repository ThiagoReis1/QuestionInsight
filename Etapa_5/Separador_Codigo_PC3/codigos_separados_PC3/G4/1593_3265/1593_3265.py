from numpy import *
from numpy.linalg import*

notas = array(eval(input("NOTAS: ")))
soma = 0
j = 0
for i in range(size(notas)):
	soma = soma +(notas[i]*(i + 1))
	j = j + (i+1)
m = soma/j
print(round(m, 2))

