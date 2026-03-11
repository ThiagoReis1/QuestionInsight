pais = (input("Pais?: ")).upper()
cidade = (input("Cidade?: ")).upper()
if (pais == "ITALIA") and (cidade == "ROMA"):
	print("LATINA")
elif (cidade == "FLORENCA"):
	print("SIENA")
elif (pais == "ESPANHA") and (cidade == "FRIGILIANA"):
	print("MALAGA")
elif (cidade == "MADRID"):
	print("MADRID")
else:
	print("PROVINCIA NAO IDENTIFICADA")