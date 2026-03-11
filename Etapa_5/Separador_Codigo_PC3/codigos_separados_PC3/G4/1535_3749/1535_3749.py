x = float(input("x: "))
k = int(input("k: "))

i = 0
soma = 0

while (i < k):
	soma = soma + ((-1) ** (i) * x ** (2 * i + 1) / (2 * i + 1))
	i = i + 1

print (round(soma, 6))
	