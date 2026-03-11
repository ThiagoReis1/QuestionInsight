from math import*

x=eval(input())
k=int(input())

cont=1
cos=1
indice=1
termo=1
sinal=1

while k>cont:
	termo=((x**indice)/(factorial(indice)))
	cos=cos+(termo*sinal)
	cont=cont+1
	indice=indice+2
	sinal=sinal*(1)
print(round(cos,6))