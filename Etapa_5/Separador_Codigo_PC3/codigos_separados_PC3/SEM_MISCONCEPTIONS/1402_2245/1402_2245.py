nome_da_arma = input("Digite o nome da arma (Machado/lanca): ")
fator_de_sucesso = int(input("valor entre 1 e 10: "))

if (nome_da_arma.lower() == "machado"):
	dano = 30 * (fator_de_sucesso/10)
	print(int(dano))
else:
	dano = 5 + 20 * fator_de_sucesso/10
	print(int(dano))