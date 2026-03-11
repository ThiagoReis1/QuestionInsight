consumo = float(input())

if(consumo<=100):
	valor=consumo*1.2
	print(round(valor,2))
else:
	valor=consumo*1.4 + 25
	print(round(valor,2))