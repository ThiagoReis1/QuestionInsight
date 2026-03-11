from numpy import*

nome = input("Digite a palavra:")
j = 0
cont = 0

while(j < len(nome)):
	if((nome [j] == "A") or (nome[j] == "E") or (nome [j] == "I") or (nome [j] == "O") or (nome [j] == "U")):
		cont = cont + 1.12
		j = j + 1
	
	else:
		cont = cont + 1.18
		j = j + 1
		
print(round(cont,2))