from math import*

x = float(input())
k = int(input())
soma = 0

while (k > 0):
	valor = (x ** k)/(factorial(k))
	soma = valor + 1
	print(round(valor,8))

