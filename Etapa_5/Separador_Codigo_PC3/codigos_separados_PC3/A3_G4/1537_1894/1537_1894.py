from math import *

x = float(input("valor de x: "))
k = int(input("valor de k: "))

cont = 1
acm = k
valor = e ** x

while (cont < k):
	valor = cont + x + ((x) ** (cont) / factorial(cont))
	cont = cont + 1
print(round(valor,9))