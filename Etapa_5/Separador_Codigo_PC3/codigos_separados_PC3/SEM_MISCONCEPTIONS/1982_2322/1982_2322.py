pais = input("digite o nome do pais aqui: ")
cidade = input("digite o nome da cidade aqui: ")

if(pais == "Italia" and cidade == "Roma"):
	provincia = "LATINA"
elif(pais == "Italia" and cidade == "Florenca"):
	provincia = "SIENA"
elif(pais == "Espanha" and cidade == "Frigiliana"):
	provincia = "MALAGA"
elif(pais == "Espanha" and cidade == "Madrid"):
	provincia = "MADRID"
else:
	provincia = "PROVINCIA NAO IDENTIFICADA."
print(provincia.upper())