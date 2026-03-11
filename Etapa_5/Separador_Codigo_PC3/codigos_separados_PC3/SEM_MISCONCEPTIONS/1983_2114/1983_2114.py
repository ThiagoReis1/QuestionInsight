a = input("Digite o continente: ")
b = input("Digite o país: ")

if (a.upper()!= "ASIA") and (a.upper()!= "AMERICA-DO-SUL") or ((b.upper()!="JORDANIA") and (b.upper()!="INDIA") and (b.upper()!="PERU") and (b.upper()!="BRASIL"):
	print("INFORMACAO NAO IDENTIFICADA")
else:
	if (a.upper() == "ASIA") and (b.upper() == "JORDANIA"):
		print("AS RUINAS DE PETRA")
	if (a.upper() == "ASIA") and (b.upper() == "INDIA"):
		print("TAJ MAHAL")
	if (a.upper() == "AMERICA-DO-SUL") and (b.upper() == "PERU"):
		print("MACHU PICCHU")
	if (a.upper() == "AMERICA-DO-SUL") and (b.upper() == "BRASIL"):
		print("CRISTO REDENTOR")
