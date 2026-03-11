x = int(input("Digitar idade: "))
y = float(input("Digitar peso: "))
if(x == 0 or x == 130, y == 0,0 or 550,0):
	if (x >= 12 and y >= 60):
		z = "1000"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif(x >= 12 and y <= 60):
		z = "875"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif (x <= 12 and y <= 5):
		z = "75"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif( x <= 12 and y >= 5 or y == 9):
		z = "125"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif(x <= 12 and y >= 9 or y == 16):
		z = "250"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif( x <= 12 and y >= 16 or y == 24):
		z = "375"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif(x <=12 and y >= 24 or y == 30):
		z = "500"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
	elif(x <= 12 and y >= 30):
		z = "750"
		print("Entradas:", x, "anos e ", y, "kg")
		print("Dosagem:", z, "mg")	
else:
		print("Entradas:", x, "anos e ", y, "kg - Dados invalidos")		