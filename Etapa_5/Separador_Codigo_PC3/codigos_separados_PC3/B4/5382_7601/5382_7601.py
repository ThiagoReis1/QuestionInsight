from numpy import*

rotulo = input("Escreva o rotulo: ").upper()

i = 0
soma = 0
while i < len(rotulo):
	if rotulo[i] == "A":
		soma = soma + 0.25
	elif rotulo[i] == "E":
		soma = soma + 0.25
	elif rotulo[i] == "I":
		soma = soma + 0.25
	elif rotulo[i]== "O":
		soma = soma + 0.25
	elif rotulo[i] == "U":
		soma = soma + 0.25
	else:
		soma = soma + 0.27
	i = i + 1
	
print(round(soma,2))