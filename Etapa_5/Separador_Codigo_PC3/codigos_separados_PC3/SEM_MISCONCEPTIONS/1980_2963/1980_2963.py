#include<math.h>
informacao = input("Nome do Estado\n")
informacao2 = input("Nome da Cidade\n")
if(informacao.upper() == "AMAZONAS" and informacao2.upper() == "PARINTINS"):
	print ("PALMARES")
elif(informacao.upper() == "AMAZONAS" and informacao2.upper() == "MANAUS"):
	print ("COROADO")
elif(informacao.upper() == "PARA" and informacao2.upper() == "BELEM"):
	print ("CIDADE VELHA")
elif(informacao.upper() == "PARA" and informacao2.upper() == "SANTAREM"):
	print ("CENTRO")
else:
	print("BAIRRO NAO IDENTIFICADO")



