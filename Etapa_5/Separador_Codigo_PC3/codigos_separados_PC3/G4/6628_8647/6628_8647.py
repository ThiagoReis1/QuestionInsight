nome = (input("Qual o nome?: ").upper())

i = 0
cont = 0

while i < len(nome):
	if nome[i] == "E":
		cont = cont + 1
	i += 1
	
print(cont)