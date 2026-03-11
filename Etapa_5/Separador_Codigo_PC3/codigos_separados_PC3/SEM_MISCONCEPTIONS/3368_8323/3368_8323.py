esc = input("Qual escala de temperatura? ")
temp = float(input("Qual o valor da temperatura? "))
kelvin = temp + 273.15
celsius = temp - 273.15
if (esc == "C"):
	print(round(kelvin, 2))
if (esc == "K"):
	print(round(celsius, 2))