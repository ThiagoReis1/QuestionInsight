prod = input()
i = 0
soma = 0

while i < len(prod):
	if prod[i] == "A":
		soma = soma + 19.90
	elif prod[i] == "L":
		soma = soma + 3.50
	else:
		soma = soma + 4.25
	i = i + 1
print(round(soma, 2))