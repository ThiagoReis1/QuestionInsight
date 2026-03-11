escala = input("escala em C ou K: ")
temp = float(input("temperatura: "))

if (escala == "C"):
	print(round(temp+273.15, 2))
	
else:
	print(round(temp-273.15, 2))
	