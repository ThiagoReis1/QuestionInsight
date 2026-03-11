pais = input("Digite o nome do país: ")
cidade = input("Digite o nome da cidade: ")

if (pais != "Italia" and pais != "Espanha") or (cidade != "Roma" and cidade != "Florença" and cidade != "Frigiliana" and cidade != "Madrid" ):
	print("PROVINCIA NAO IDENTIFICADA")
else:
	if pais == "Italia" and cidade == "Roma":
		X = "latina"
		print(X.upper())
	elif pais == "Italia" and cidade == "Florença":
		X = "siena"
		print(X.upper())
	elif pais == "Espanha" and cidade == "Frigiliana":
		X = "malaga"
		print(X.upper())
	elif pais == "Espanha" and cidade == "Madrid":
		X = "madrid"
		print(X.upper())
		