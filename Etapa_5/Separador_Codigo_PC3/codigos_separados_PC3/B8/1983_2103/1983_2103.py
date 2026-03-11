#Entradas
cont1 = input("Digite o continente: ")
pais1 = input("Digite o pais: ")
cont = cont1.upper()
pais = pais1.upper()

if(cont=="ASIA" or cont=="AMERICA-DO-SUL"):
	if(cont=="ASIA"):
		if(pais=="JORDANIA"):
			print("AS RUINAS DE PETRA")
		elif(pais=="INDIA"):
			print("TAJ MAHAL")
		else:
			print("INFORMACAO NAO IDENTIFICADA")
	elif(cont=="AMERICA-DO-SUL"):
		if(pais=="PERU"):
			print("MACHU PICCHU")
		elif(pais=="BRASIL"):
			print("CRISTO REDENTOR")
		else:
			print("INFORMACAO NAO IDENTIFICADA")
else:
	print("INFORMACAO NAO IDENTIFICADA")