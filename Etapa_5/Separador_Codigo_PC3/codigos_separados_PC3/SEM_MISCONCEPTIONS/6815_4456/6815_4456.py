import math

numero = int(input())
iterador = 1

while iterador <= numero:
	raiz = math.sqrt(iterador)
	print(round(raiz,2))
	iterador += 1

print("fim")