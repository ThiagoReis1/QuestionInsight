from math import *
n = int(input("Nro de termos:"))
numerador = 1
denominador = 1
soma = 0
while (numerador <= n):
	if (numerador % 2 == 0):
		soma = soma - (sqrt(numerador) / (6 + denominador))
	else:
		soma = soma + (sqrt(numerador) / (6 + denominador))
	numerador = numerador + 1
	denominador = denominador + 2
print(round(soma,10))