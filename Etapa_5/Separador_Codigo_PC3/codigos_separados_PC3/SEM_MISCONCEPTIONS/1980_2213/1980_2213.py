nome1=input("qual o nome: ").upper()
nome2=input("qual o nome: ").upper()

if((nome1=="AMAZONAS") and (nome2=="MANAUS") or (nome2=="PARINTINS") or (nome1=="PARA") and(nome2=="BELEM") or (nome=="SANTAREM"):
	if(nome1=="AMAZONAS")and(nome2=="MANAUS"):
		print("coroado")
	elif(nome1=="AMAZONAS") and(nome2=="PARINTINS"):
		print("PALMEIRAS")
	elif(nome1=="PARA") and(nome2=="BELEM"):
		print("CIDADE VELHA")
	elif(nome1=="PARAR") and(nome2=="SANTAREM"):
   	print("CENTRO")
else:
		print("bairro nao identificado".upper())