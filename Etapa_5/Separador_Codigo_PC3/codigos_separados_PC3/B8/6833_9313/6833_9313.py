from numpy import*

nome=input("insira o nome do produto M mercearia, P padaria , e R rotisseria:  ").upper()
total=0
i=0

while i<len(nome):
	if nome[i]=="M":
		total +=7.25	
	elif nome[i]=="P":
		total += 4.75	
	elif nome[i]=="R":
		total += 3.50
	i += 1
	
print(round(total,2))