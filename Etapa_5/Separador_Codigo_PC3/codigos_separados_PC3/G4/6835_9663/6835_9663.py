from numpy import*

p = input("Digite se voce deseja Biscoito, Cereais ou Enlatados: ").upper()
i = 0
soma = 0

while i < len(p):
	if p[i] == "B":
		soma = soma + 3.75
	elif p[i] == "C":
		soma = soma + 7.90
	else:
		soma = soma + 9.85
	i = i + 1
print(round(soma,2))