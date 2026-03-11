arma=input("escolha sua arma: ")
fator_sucesso=int(input("qual seu fator de sucesso: "))
if(arma=="machado"):
	machado=30*fator_sucesso/10
	print(machado)
else:
	lanca=5+20*fator_sucesso/10
	print(lanca)