nome_da_arma = input("arma escolida pelo jogador: ")
fator_de_sucesso = int(input("lancamento do dado: "))

machado = 30*fator_de_sucesso/10
lanca = 5 + 20*fator_de_sucesso/10

if	(nome_da_arma == "machado"):
	dano = machado
else:
	dano = lanca
	
print(int(dano))