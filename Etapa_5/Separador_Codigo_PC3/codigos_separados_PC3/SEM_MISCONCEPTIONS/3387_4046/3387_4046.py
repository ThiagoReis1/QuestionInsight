unidade = input("Informe a unidade em que a medida esta. Digite M para milhas por galao ou K para quilometros por litro: ")
medida = float(input("Informe o valor da medida: "))

#if(unidade == "M"):
	#Mg = (medida / 2.35215)
	#print(round(Mg, 2))
if(unidade == "M"):
	Mg = (medida / 2.35215) #Mg = Kl / 2.35215
	print(round(Mg, 2))
else:
	Kl = (medida * 2.35215)
	print(round(Kl, 2))