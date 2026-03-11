from numpy import*
from numpy.linalg import*
notas=array(eval(input()))
soma = 0
pesos = 0
q = size(notas)
for i in range(size(notas)):
	soma = soma + notas[i]*(i + 1)
	pesos = pesos + (i+1)
total = soma/pesos
print(round(total,2))
