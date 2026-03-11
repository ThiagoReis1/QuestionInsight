nome_da_arma = input("arma: ")
fator_de_sucesso = int(input("inserir valor: "))
if nome_da_arma == 'machado' :
	dano = 30 * fator_de_sucesso / 10
	print(dano)
else:
	dano = 5 + 20 * fator_de_sucesso / 10
	print(int(dano))