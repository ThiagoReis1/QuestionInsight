n = int(input("Nro termos:"))
num = 1
den = 1
soma = 0
while (num <= n):
	if (num % 2 == 0):
		soma = soma + (num**3 / (8 + den))
	else:
		soma = soma - (num**3 / (8 + den))
	num = num + 1
	den = den + 2
print(round(soma,5))
							