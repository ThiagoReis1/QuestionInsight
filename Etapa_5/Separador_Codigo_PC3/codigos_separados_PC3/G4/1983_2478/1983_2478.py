cont = input("Informe o continente: ").upper()
pais = input("Informe o pais: ").upper()
if (cont == "ASIA" and pais == "JORDANIA"):
	print("AS RUINAS DE PETRA")
elif(cont == "ASIA" and pais == "INDIA"):
	print("TAJ MAHAL")
elif(cont == "AMERICA-DO-SUL" and pais == "PERU"):
	print("MACHU PICCHU")
elif(cont == "AMERICA-DO-SUL" and pais == "BRASIL"):
	print("CRISTO REDENTOR")
else:
	print("INFORMACAO NAO IDENTIFICADA")