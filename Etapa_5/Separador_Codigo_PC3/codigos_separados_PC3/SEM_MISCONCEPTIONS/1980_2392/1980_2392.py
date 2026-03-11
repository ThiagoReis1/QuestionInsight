caracteristica1 = input()
caracteristica2 = input()

if(caracteristica1=="Amazonas" and caracteristica2=="Parintins"):
	print("palmares".upper())
elif(caracteristica1=="Amazonas" and caracteristica2=="Manaus"):
	print("coroado".upper())
elif(caracteristica1=="Para" and caracteristica2=="Belem"):
	print("cidade velha".upper())
elif(caracteristica1=="Para" and caracteristica2=="Santarem"):
	print("centro".upper())
else:
	print("bairro nao identificado".upper())