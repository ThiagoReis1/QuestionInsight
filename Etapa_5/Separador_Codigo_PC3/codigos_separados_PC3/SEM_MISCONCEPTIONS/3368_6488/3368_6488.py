# K + 273,15

escala = input("Digite se a temperatura sera de C ou K: ")
ESCALA = escala.upper()
temperatura = float(input("Digite o valor da temperatura: "))

if(ESCALA == "C"):
	c = temperatura + 273.15
	print(round(c, 2))
else:
	a = temperatura - 273.15
	print(round(a, 2))