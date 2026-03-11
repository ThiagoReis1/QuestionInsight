from math import*

x=eval(input())
k=int(input())

cont=0
cos=0
indice=1
termo=0
soma=1

while k>=cont:
	termo=((x**indice)/(factorial(indice)))
	cos=cos+(termo*sinal)
	cont=cont+2
	indice=indice+2
print(round(cos,10))