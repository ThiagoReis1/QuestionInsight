import math

num = int(input("digite o numero: "))

for x in range(1, num + 1):
	raiz = math.sqrt(x)
	print(round(raiz, 2))
print("fim")