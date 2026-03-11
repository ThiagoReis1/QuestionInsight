consumo = float(input('consumo de energia: '))
if(consumo <= 150):
	valor1 = consumo*0.60+5
	print(round(valor1, 2))
else: 
	valor2 = consumo*0.75+16
	print(round(valor2, 2))