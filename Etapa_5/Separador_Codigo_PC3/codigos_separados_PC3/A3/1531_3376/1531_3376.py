from math import*

x = float(input())
k = int(input())

cont = 0
cosh = 0
indice = 0
termo = 0
sinal = 1

while k>cont:
	termo = ((x**indice)/(factorial(indice)))
	cosh = cosh + (termo*sinal)
	cont = cont + 1
	indice = indice + 2
	sinal = sinal * (-1)
print(round(cosh,10))