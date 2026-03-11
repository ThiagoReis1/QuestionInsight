consumo = float(input("digite o valor: "))
if (consumo >= 0):
	if(consumo <= 100):
		valor1 = consumo * 1.20 + 1.00
		print (round(valor1, 2)
	elif(consumo >= 100) and (consumo <= 200):
		valor2 = consumo * 1.30 + 10.00
		print(round(valor2, 2))
	elif (consumo >= 200) and (consumo <= 300):
		 valor3 = consumo * 1.40 + 20.00
		 print(round(valor3, 2))
	else:
		 valor4 = consumo * 1.50 + 25.00
		 print(round(valor4, 2))