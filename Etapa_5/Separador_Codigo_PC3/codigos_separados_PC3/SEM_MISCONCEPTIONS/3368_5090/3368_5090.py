escala = input("Qual a escala: ")
valor = float(input("Valor da temperatura: "))

if (escala == "C"):
	calculo = valor + 273.15
	print(round(calculo,2))
	
else:
	calculo = valor - 273.15
	print(round(calculo,2))