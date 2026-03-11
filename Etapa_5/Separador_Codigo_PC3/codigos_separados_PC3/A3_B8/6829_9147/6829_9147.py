vetors = input("insira o produto (A) para acougue, (L) para laticinios e (P) para padaria: ").upper()

i = 0
preco = 0
qtdA = 0
qtdL = 0
qtdP = 0

while	i < len(vetors):
	if	vetors[i] == "A":
		preco += 19.90
		qtdA += 1
	elif	vetors[i] == "L":
		preco += 3.50
		qtdL += 1
	elif	vetors[i] == "P":
		preco += 4.25
		qtdP += 1
		
	i += 1
	
print(round(preco, 2))