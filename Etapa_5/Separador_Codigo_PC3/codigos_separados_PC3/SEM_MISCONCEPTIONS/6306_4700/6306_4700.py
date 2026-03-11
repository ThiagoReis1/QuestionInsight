ent = input("Digite a string: ").upper()
i = 0
conta = 0
contl = 0
contp = 0
tam = len(ent)
while (i<tam):
	if (ent[i] == "A"):
		conta = conta + 1
		i = i*1.19
	
print (i, conta, contl, contp)
	
