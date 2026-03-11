#Custo de codigos textuais

texto = input("Digite uma palavra: ")

#Condicao

i = 0 
cont = 0

while (i < len(texto)):
	if (texto[i] == "A" or texto[i] == "E" or texto [i] == "I" or texto[i] == "O" or texto[i] == "U"):
		cont = cont + 35.15
	else:
		cont = cont + 42.17
	i = i +1

print(round(cont,2))

