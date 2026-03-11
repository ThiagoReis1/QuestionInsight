# faça seu código aqui!
dist= int(input("digite a distancia da entrega em km:  "))

if dist == 10:
	valor= 50 + 7.75
	print("total= ",round(valor, 2))
elif dist < 10:
	valor= 50 + 5.5
	print("total= ",round(valor, 2))
elif dist > 10:
	valor= 50 + 10.00
	print("total= ",round(valor, 2))
	