Estado = input("caracteristica1: ").upper()
Cidade = input("caracteristica2: ").upper()

if (Estado == "AMAZONAS") and (Cidade == "MANAUS"):
	saida = "COROADO"
	print(saida)
elif (Estado == "AMAZONAS") and (Cidade == "PARINTINS"):
	saida = "PALMARES"
	print(saida)
elif (Estado == "PARA") and (Cidade == "BELEM"):
	#saida = "CIDADE VELHA"
	print("CIDADE VELHA")
elif (Estado == "PARA")  and (Cidade == "SANTAREM"):
	saida = "CENTRO"
	print(saida)
else:
	saida = "BAIRRO NAO IDENTIFICADO"
	print(saida)