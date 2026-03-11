moeda = input("Digite o resultado do lancamento: ")
caras = 0 
while (moeda.upper() !="S"):
	if (moeda.upper() == "CARA"):
		caras = caras + 1 
	moeda = input("Digite o resultado do lancamento: ")
print(caras)

