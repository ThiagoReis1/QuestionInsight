v = int(input("digite a velocidade escolhida: "))

if v < 50:
	valor = (60.00 + 4.50)
	print(round(valor, 2))
	
elif v == 50:
	valor = (60.00 + 5.50)
	print(round(valor, 2))
	
else:
	valor = (60.00 + 6.50)
	print(round(valor, 2))