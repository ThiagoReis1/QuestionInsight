bolinha = input("Digite um valor:")
cont = 0
while (bolinha.upper() != "S"):
	if bolinha.upper() == "PRETA":
		cont = cont + 1 
	bolinha = input("Digite:")
print(cont)