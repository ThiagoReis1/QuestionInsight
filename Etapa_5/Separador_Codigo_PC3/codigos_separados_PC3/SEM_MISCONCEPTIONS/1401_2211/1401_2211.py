#viserion maritimo, cada baforada 40 navios
#drogon terrestre, cada 150 guerreiros
#saida, nome do dragao, 
#quantidade de itens destruidos


#nome= input("tipo de aminoacido: ")

#if (nome=="ARGININA"):
 #   peso=ARGININA
#else:
#	 peso=TIROSINA
#print (round(peso,2))
ataque= input("Tipo de ataque: ")
alvos= int(input("quantidade de alvos destruidos: "))

if (ataque=="maritimo"):
	print ("Viserion")
	print (40*alvos)
else:
	print ("Drogon")
	print (150*alvos)
	