es = input()
ci = input()

if (es.upper() != "AMAZONAS" and es.upper() != "PARA"):
	print("BAIRRO NAO IDENTIFICADO")
elif (es.upper() == "AMAZONAS" and ci.upper() == "MANAUS"):
	print("COROADO")
elif(es.upper() == "AMAZONAS" and ci.upper() == "PARINTINS"):
	print("PALMARES")
elif (es.upper() == "PARA" and ci.upper() == "BELEM"):
	print("CIDADE VELHA")
elif (es.upper() == "PARA" and ci.upper() == "SANTAREM"):
	print("CENTRO")
else:
	print("BAIRRO NAO IDENTIFICADO")