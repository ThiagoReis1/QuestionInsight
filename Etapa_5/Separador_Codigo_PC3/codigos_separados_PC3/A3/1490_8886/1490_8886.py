agua= float(input(" "))

if (agua >= 0.0) and (agua <= 10.0):
	Tarifa = 3.00
	Taxa = 15.00
	valor = (agua * 3.00) + 15.00
	print(round(valor,2))
elif (agua > 10.0) and (agua <= 15.0):
	Tarifa = 3.50
	Taxa = 20.00
	valor = (agua * 3.50) + 20.00
	print(round(valor,2))
elif (agua > 15.0) and ( agua <= 20.0):
	Tarifa = 4.00 
	Taxa = 25.00
	valor = (agua * 4.00) + 25.00
	print(round(valor,2))
else: 
	Tarifa = 4.50
	Taxa = 30.00
	valor = (agua * 4.50) + 30.00
	print(round(valor,2))
	
