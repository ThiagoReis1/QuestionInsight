c1 = input("Pais:").upper()
c2 = input("Cidade:").upper()

if((c1 =="ITALIA" or c1 == "ESPANHA") and( c2 == "ROMA"or c2 == "FLORENCA"or c2 == "FRIGILIANA"or c2 == "MADRID")):
	if (c1 == "ITALIA" and c2 == "ROMA"):
		print("LATINA")
	elif (c1 == "ITALIA" and c2 == "FLORENCA"):
		print("SIENA")
	elif (c1 == "ESPANHA"and c2 == "FRIGILIANA"):
		print("MALAGA")
	elif (c1 == "ESPANHA"and c2 == "MADRID"):
		print("MADRID")
else:
	print("PROVINCIA NAO IDENTIFICADA")