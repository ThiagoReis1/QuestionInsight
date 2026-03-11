x = float(input("numero real: "))
k = int(input("numero inteiro: "))
i = 1
cont = 0
soma = 0

while (i <= k):
	if(x > 0):
		s = i / x
		i = i + 1
		soma = soma + s
print(round(soma,10))