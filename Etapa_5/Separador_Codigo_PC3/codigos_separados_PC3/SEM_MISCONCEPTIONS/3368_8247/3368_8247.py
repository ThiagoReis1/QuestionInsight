tipo = input("Digite C para Celsius e K para Kelvin: ")
valor = float(input("Insira a temperatura: "))
if tipo == "C":
	r = valor + 273.15
	print(round(r, 2))
else:
	r = valor - 273.15
	print(round(r, 2))