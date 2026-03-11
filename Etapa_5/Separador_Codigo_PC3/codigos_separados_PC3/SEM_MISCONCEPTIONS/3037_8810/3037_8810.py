x = float(input("Digite o valor de x:"))
if((x <= -1) or (x >= 1)):
	calculo = x**2
	total = round(calculo,4)
	print(total)
elif((x > -1) and (x < 0) or (x > 0) and (x < 1)):
	calculo = x
	total = round(calculo,4)
	print(total)
elif(( x == 0)):
	calculo = 1 
	print(calculo)
else:
	print("Entrada Invalida")