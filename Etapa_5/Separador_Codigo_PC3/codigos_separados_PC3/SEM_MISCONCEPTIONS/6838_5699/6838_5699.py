compra = input().upper()

soma = 0
i = 0
while i < len(compra):
	if compra[i] == "D":
		soma += 2.25
	elif compra[i] == "S":
		soma += 4
	else:
		soma += 6.9
	i += 1

print(round(soma,2))