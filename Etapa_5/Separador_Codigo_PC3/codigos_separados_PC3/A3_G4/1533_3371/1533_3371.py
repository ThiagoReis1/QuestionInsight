from math import *
x = float(input())
k = int(input())
indice = 2
cont = 0
cos = 1
soma=1
cont=1
while(k>cont):
	termo = (x**indice)/factorial(indice)
	soma = soma + termo
	cont = cont +1
	indice = indice+2

print(round(soma,8))