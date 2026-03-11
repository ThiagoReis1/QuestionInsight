from math import sqrt
n = int(input("digite o valor de n: "))
cont = 1

while (cont <= n):
	raiz1 = sqrt(cont)
	cont = cont + 1
	print(round(raiz1, 2))
print("fim")