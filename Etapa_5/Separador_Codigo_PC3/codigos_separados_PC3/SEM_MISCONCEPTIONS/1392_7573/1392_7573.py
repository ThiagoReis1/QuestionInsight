consumo = float(input("Digite o consumo de agua: "))

if(consumo < 10):
	valor = 30.00 + (consumo * 3.00)
	print(round(valor,2))

if(consumo >= 10):
	valor = 30.00 + (consumo * 3.50)
	print(round(valor,2))
	
