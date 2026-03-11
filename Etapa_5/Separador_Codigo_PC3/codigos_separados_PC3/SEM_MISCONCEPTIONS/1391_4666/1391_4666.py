consumo = float(input("qual o consumo?"))
if(consumo<=150000):
	valor1= consumo*5
	print(round(valor1,2))
else:
	valor2 = 150000*0.60+5(consumo-150000)
	print(round(valor2,2))