pais = input("pais:")

cidade = input ("cidade:")

if (pais .upper() == "ITALIA") or (pais .upper() == "ESPANHA"):
	if (cidade.upper() == "ROMA"):
		print("LATINA")
	elif (cidade.upper() == "FLORENCA"):
		print("SIENA")
	elif (cidade.upper() == "FRIGILIANA"):
		print ("MALAGA")
	elif (cidade.upper() == "MADRID"):
		print ("MADRID")

else:
	print("PROVINCIA NAO IDENTIFICADA")

