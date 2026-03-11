#Lendo as informacoes de teclado
estado=input("Digite o nome do estado (Amazonas/Para): ")
cidade=input("Digite o nome da cidade: ")

if(estado.upper()=="AMAZONAS" and cidade.upper()=="MANAUS"):
	print("COROADO")
elif(estado.upper()=="AMAZONAS" and cidade.upper()=="PARINTINS"):
	pint("PALMARES")
elif(estado.upper()=="PARA" and cidade.upper()=="BELEM"):
	print("CIDADE VELHA")
elif(estado.upper()=="PARA" and cidade.upper()=="SANTAREM"):
	pint("CENTRO")
else:
	print("BAIRRO NAO IDENTIFICADO")