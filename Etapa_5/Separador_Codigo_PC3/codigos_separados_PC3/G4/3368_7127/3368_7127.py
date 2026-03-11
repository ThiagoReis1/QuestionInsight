E = input("Escala da temperatura: ").upper()
V = float(input("Temperatura: "))
if (E == "K"):
	V1 = V - 273.15
	print(round(V1, 2))
if (E == "C"):
	V1 = V + 273.15
	print(round(V1, 2))