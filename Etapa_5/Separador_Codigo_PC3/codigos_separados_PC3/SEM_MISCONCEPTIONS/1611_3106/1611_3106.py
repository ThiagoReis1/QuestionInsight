frase = input("Digite a frase: ").upper()

i=0
custo = 0

while(i<len(frase)):
	if(frase[i] == "A") or (frase[i] == "E") or (frase[i] == "I") or (frase[i] == "O") or (frase[i] == "U"):
		custo = custo + 0.15
	else:
		custo = custo + 0.17
	i = i + 1
	
print(round(custo,2))