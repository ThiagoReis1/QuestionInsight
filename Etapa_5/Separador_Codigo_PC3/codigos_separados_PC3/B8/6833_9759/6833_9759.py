vetor = input("Informe oq precisa: ").upper()

i = 0
soma = 0 
while i < len(vetor):
	if vetor[i] == "M":
		soma = soma + 7.25
	elif vetor[i] == "P":
		soma = soma + 4.75
	elif vetor[i] == "R":
		soma = soma + 3.50
	i = i + 1
print(round(soma, 2))