#LEIA: nome de uma das nove cidades livres
#saida: o gentilico correspondente

nc = input("Digite o nome da cidade: ")

if(nc=="Pentos")or(nc=="Bravos")or(nc=="Lys")or(nc=="Qohor")or(nc=="Norvos")or(nc=="Myr")or(nc=="Tyrosh")or(nc=="Volantis")or(nc=="Lorath"):
	if(nc=="Pentos"):
		g = "pentoshi"
		
	elif(nc=="Bravos"):
		g = "bravosiano"
		
	elif(nc=="Lys"):
		g = "liseno"
		
	elif(nc=="Qohor"):
		g = "qohorik"
		
	elif(nc=="Norvos"):
		g = "norvoshi"
		
	elif(nc=="Myr"):
		g = "myrano"
		
	elif(nc=="Tyrosh"):
		g = "tyroshi"
		
	elif(nc=="Volantis"):
		g = "volantino"
		
	elif(nc=="Lorath"):
		g = "lorathi"
	print(g)
else:
	print("Entrada",nc,"invalida")







