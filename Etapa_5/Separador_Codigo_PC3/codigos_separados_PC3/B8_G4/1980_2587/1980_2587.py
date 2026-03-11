e = input("Nome do estado: ")
c = input("Nome da cidade: ")

if( e != "Amazonas") or ( e != "Para"):
	print("BAIRRO NAO IDENTIFICADO")
elif( e == "Amazonas" ) or ( c == "Manaus"):
	print("BAIRRO COROADO")
elif( e == "Amazonas" ) or ( c == "Parintins"):
	print("BAIRRO PALMARES")
elif( e == "Para" ) or ( c == "Belem"):
	print("BAIRRO CIDADE VELHA")
elif( e == "Para" ) or (c == "Santarem"):
	print("BAIRRO CENTRO")