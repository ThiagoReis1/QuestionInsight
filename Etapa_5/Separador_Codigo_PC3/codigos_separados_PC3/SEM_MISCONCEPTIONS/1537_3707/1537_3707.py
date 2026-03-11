from math import factorial

numero = float(input())
k = int(input())

valor = 0
i = 0

while (i<k):
	valor = valor + ((numero**i)/factorial(i))
	i = i + 1
	
print(round(valor,9))