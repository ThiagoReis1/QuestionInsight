continente = input("escolha o continente: ").upper()
pais = input("escolha o pais: ").upper()


if((continente == "ASIA") and (pais == "JORDANIA")):
	print("AS RUINAS DE PETRA")

elif((continente == "ASIA") and (pais == "INDIA")):
	print("TAJ MAHAL")
	
elif((continente == "AMERICA-DO-SUL") and (pais == "PERU")):
	print("MACHU PICCHU")
	
elif((continente == "AMERICA-DO-SUL") and (pais == "BRASIL")):
	print("CRISTO REDENTOR")
	
else:
	print("INFORMACAO NAO IDENTIFICADA")