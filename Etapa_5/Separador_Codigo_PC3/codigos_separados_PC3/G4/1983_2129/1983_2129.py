c = input("continente: ").upper()
p = input("pais: ").upper()

if (c == "ASIA") and (p == "JORDANIA"):
	print("AS RUINAS DE PETRA")
elif (c == "ASIA") and (p == "INDIA"):
	print("TAJ MAHAL")
elif (c == "AMERICA-DO-SUL") and (p == "PERU"):
	print("MACHU PICCHU")
elif (c == "AMERICA-DO-SUL") and (p == "BRASIL"):
	print("CRISTO REDENTOR")
else:
	print("INFORMACAO NAO IDENTIFICADA")