T = input ("Digite o tipo de ataque que deseja usar (maritimo ou terrestre): ")
Q = int (input ("Digite a quantidade de baforadas dadas pelo dragão: "))

if T == "maritimo":
	print ("Viserion")
	print (int(Q*40))
else:
	print ("Drogon")
	print (int(Q * 150))