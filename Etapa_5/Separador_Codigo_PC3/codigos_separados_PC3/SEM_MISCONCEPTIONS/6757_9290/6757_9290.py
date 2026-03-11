num = int(input("numero_de_pizzas: "))
######################################
if num < 3:
	valor = (5.0 * num) + 3.0
else:
	if num == 3:
		valor = (5.0 * num)+ 3.25
	else:
		valor = (5.0 * num)+ 4.50
		
valorfinal = round(valor,2)
print(valorfinal)