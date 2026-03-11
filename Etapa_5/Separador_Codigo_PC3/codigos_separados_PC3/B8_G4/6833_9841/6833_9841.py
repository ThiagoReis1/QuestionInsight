n = str(input())
soma = 0
for c in range(0, len(n)):
	if n[c] == "M":
		soma = soma + 7.25
	elif n[c] == "P":
		soma = soma + 4.75
	elif n[c] == "R":
		soma = soma + 3.50
print(soma)
	