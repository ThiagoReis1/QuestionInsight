arma =  input("Digite o nome: ")
fator = int(input("Digite o fator de sucesso: "))

if(arma.lower() == "machado"):
	dano = 30 * (fator/10);
	print(dano)
elif(arma.lower() == "lanca"):
	dano = 5 + 20 * (fator/10);
	print(dano)