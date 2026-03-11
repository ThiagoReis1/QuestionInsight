from math import*

x = eval(input())
k = int(input())

cont = 0
cos = 0
indice = 0
termo = 0
sinal = 1

while k>cont:
	termo = ((x**indice)/(factorial(indice)))
	cos = cos+ (termo*sinal)
	cont = cont + 1
	indice = indice + 2
	sinal=sinal*-1
print(round(cos,10))
