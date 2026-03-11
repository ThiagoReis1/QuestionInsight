from math import*
x=float(input())
k=int(input())
indice = 2
cos = 1
cont=1
while (k>cont):
	termo = (x**indice)/factorial(indice)
	soma = soma + termo
	cont = cont +1
	indice = indice+2
	
print(round(soma, 9))