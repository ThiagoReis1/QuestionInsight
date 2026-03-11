numero = int(input("consumo de agua: "))



if (numero < 10):
	total = numero * 2
	print(round(total + 20, 2))
	
elif (10 <= numero < 20):
	total = numero * 2.5
	print(round(total + 20, 2))
	
elif ( 20 <= numero < 40):
	total = numero * 2.75
	print(round(total + 20, 2))
	
elif (numero >= 40):
	total = numero * 3
	print(round(total + 20, 2))
	
else:
	numero=numero