estado = input("nome: ")
cidade = input("nome: ")
if ((estado != "Amazonas" and estado != "Para") or (cidade != "Manaus" and cidade != "Parintins" and cidade != "Belem" and cidade != "Santarem")):
	print("bairro nao identificado".upper())
elif((estado == "Amazonas") and (cidade == "Manaus")):
	print("coroado".upper())
elif((estado == "Amazonas") and (cidade == "Parintins")):
	print("Palmares".upper())
elif((estado == "Para") and (cidade == "Belem")):
	print("cidade velha".upper())
elif((estado == "Para") and (cidade == "Santarem")):
	print("centro".upper())