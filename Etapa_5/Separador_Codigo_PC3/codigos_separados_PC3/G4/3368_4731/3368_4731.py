var1 = input("escala: ")
if (var1 == "C"):
	c = float(input("temperatura: "))
	resultado = c + 273.15
else:
	k = float(input("temperatura: "))
	resultado = k - 273.15
print(round(resultado, 2))
	
