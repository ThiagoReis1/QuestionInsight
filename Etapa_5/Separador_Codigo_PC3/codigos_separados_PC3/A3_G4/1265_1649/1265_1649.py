from math import*
from numpy import*

p=float(input("Digite aqui o numero: "))
x=array(eval(input("Digite o valor do vetor: ")))
y=array(eval(input("Digite o valor do vetor: ")))
h = 0
h = 0
t=(p/(p-1))
xy = (2*x-3*y)
for i in xy:
	n = n + abs(i)**t
valor = n**(1/t)
print(round(valor,3))
	