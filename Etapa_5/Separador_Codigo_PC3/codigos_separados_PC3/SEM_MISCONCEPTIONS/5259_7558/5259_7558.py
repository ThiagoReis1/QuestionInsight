valor = float(input("R$: "))
cria = int(input(" "))
if cria == 1:
	taxa =( valor - valor*(10/100))*cria
	print(round(taxa, 2))
if cria == 2:
	taxa =( valor - valor*(30/100))*cria
	print(round(taxa, 2))
if cria >= 3:
	taxa =( valor - valor*(40/100))*cria
	print(round(taxa, 2))
		