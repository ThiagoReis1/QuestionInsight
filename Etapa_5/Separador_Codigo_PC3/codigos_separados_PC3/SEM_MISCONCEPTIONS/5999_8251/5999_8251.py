quant = int(input("insira um numero: "))

if(quant > 6):
	valor = quant * 0.6
	print(round(valor, 2))
else: 
	valor = quant * 0.75
	print(round(valor, 2))