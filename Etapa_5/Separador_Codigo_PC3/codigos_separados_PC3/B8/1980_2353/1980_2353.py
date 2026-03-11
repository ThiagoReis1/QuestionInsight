nome1=str(input("digite o nome do Estado:")).upper()
nome2=str(input("digite o nome da Cidade:")).upper()

if(nome1=="AMAZONAS")and(nome2=="MANAUS")or(nome2=="PARINTINS")or(nome1=="PARA")and(nome2=="BELEM")or(nome2=="SANTAREM"):
	if(nome1=="AMAZONAS")and(nome2=="MANAUS"):
		print("COROADO")
	elif(nome1=="AMAZONAS")and(nome2=="PARINTINS"):
		print("PALMARES")
	elif(nome1=="PARA")and(nome2=="BELEM"):
		print("CIDADE VELHA")
	elif(nome1=="PARA")and(nome2=="SANTAREM"):
		print("CENTRO")
else:
	print("bairro nao identificado".upper())
