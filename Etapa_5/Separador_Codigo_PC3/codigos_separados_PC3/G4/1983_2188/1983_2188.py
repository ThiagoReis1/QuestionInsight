con = input("Continente:")

if (con.upper() == "ASIA"):
	pa = input("Pais:")
	if (pa.upper() == "JORDANIA"):
		print("AS RUINAS DE PETRA")
	elif (pa.upper() == "INDIA"):
		print("TAJ MAHAL")
	else: 
		print("INFORMACAO NAO IDENTIFICADA")
elif (con.upper() == "AMERICA-DO-SUL"):
	pa = input("Pais:")
	if (pa.upper() == "PERU"):
		print("MACHU PICCHU")
	elif (pa.upper() == "BRASIL"):
		print("CRISTO REDENTOR")
	else: 
		print("INFORMACAO NAO IDENTIFICADA")
else: 
	print("INFORMACAO NAO IDENTIFICADA")