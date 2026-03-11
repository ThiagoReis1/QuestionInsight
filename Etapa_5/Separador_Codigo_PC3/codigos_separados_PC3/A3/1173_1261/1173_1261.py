from math import*
k = int(input("k: "))
n = 0
resultado = 0

while(n < k):
	if (n == 0):
		resultado = 1
	else:
		resultado = resultado = (1 / factorial(n))
	n = n + 1
print(round(resultado, 10))
