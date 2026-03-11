tomato = int(input("Quantos tomates deseja comprar? "))
if tomato >= 4:
	calculo = tomato * 0.55
	print(round(calculo, 2))
else:
	calculo = tomato * 0.75
	print(round(calculo, 2))