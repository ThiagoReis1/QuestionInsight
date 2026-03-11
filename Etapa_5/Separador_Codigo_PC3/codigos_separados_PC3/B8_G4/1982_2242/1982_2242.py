a = input("Pais: ").upper()
b = input("Cidade: ").upper()

if(a == "ITALIA" or a == "ESPANHA") and (b == "ROMA" or b == "FLORENCA" or b == "FRIGILIANA" or "MADRID"):
	if(a == "ITALIA" and b == "ROMA"):
		print("LATINA")
	elif(a == "ITALIA" and b == "FLORENCA"):
		print("SIENA")
	elif(a == "ESPANHA" and b == "FRIGILIANA"):
		print("MALAGA")
	elif(a == "ESPANHA" and b == "MADRID"):
		print("MADRID")
else:
	print("PROVINCIA NAO IDENTIFICADA")

