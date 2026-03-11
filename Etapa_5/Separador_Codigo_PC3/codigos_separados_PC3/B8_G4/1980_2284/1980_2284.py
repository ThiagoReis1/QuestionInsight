est = input("Nome do Estado: ")
cid = input("Nome da cidade: ")

if (est == "Amazonas"):
	if (cid == "Manaus"):
		print("Coroado".upper())
	elif (cid == "Parintins"):
		print("Palmares".upper())
	else:
		print("Bairro nao identificado".upper())
elif (est == "Para"):
	if (cid == "Belem"):
		print("Cidade velha".upper())
	elif (cid == "Santarem"):
		print("Centro".upper())
	else:
		print("Bairro nao identificado".upper())
