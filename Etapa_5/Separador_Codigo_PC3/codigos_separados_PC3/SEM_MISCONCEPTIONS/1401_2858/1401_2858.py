tipo = input("Digite o tipo do ataque :")
quantidade = int(input("Digite a quantidade de baforadas dadas pelo dragão: "))
if(tipo.lower() == 'maritimo'):
	print("Viserion")
	destruicao = quantidade*40
	print(destruicao)
else:
	print("Drogon")
	destruicao = quantidade*150
	print(destruicao)