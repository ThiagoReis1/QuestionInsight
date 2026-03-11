from math import*
ne = input("Nome do estado: ").upper()
nc = input("Nome da cidade: ").upper()
if(ne == "AMAZONAS" or ne == "PARA"):
	if(nc == "MANAUS"):
		print("coroado".upper())
	elif(nc == "PARINTINS"):
		print("palmares".upper())
	elif(nc == "BELEM"):
		print("cidade velha".upper())
	elif(nc == "SANTAREM"):
		print("centro".upper())
	else:
		print("bairro nao identificado".upper())
else:
	print("bairro nao identificado".upper())