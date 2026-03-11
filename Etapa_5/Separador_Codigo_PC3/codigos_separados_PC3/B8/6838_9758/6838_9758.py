vetor = input("codigo: ").upper()

i = 0
soma = 0
while i < len(vetor):
	if vetor[i] == "D":
		soma = soma + 2.25
	elif vetor[i] == "S":
		soma = soma + 4
	elif vetor[i] == "I":
		soma = soma + 6.9
	i = i + 1
	
print(round(soma, 2))