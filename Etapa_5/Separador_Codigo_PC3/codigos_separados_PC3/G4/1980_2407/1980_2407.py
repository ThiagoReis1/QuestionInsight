ne = input("Nome do estado: ")
nc = input("Nome da cidade: ")

if (ne == "Amazonas") and (nc == "Manaus"):
	print("COROADO")
elif (ne == "Amazonas") and (nc == "Parintins"):
	print("PALMARES")
elif (ne == "Para") and (nc == "Belem"):
	print("CIDADE VELHA")
elif (ne == "Para")	and (nc == "santarem"):
	print("CENTRO")
else: 
	print("BAIRRO NAO IDENTIFICADO")