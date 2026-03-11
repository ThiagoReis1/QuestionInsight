continente = input("Digite o continente: ")
pais = input("Digite o pais: ")

if ((continente == "asia" or continente == "america-do-sul") and (pais == "jordania" or pais == "india" or pais == "peru" or pais == "brasil")):
	if (continente == "asia" and pais == "jordania"):
		carac = As ruinas de petra
	elif (continente == "asia" and pais == "india"):
		carac = taj mahal
	elif (continente == "america-do-sul" and pais == "peru"):
		carac = machu picchu
	elif (continente == "america-do-sul" and pais == "brasil"):
		carac = "cristo redentor").upper()
else:
	print("INFORMACAO NAO IDENTIFICADA")