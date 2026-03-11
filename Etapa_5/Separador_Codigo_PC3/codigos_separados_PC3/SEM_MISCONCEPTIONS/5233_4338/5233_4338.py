numero = int(input("Numero: "))

if (numero >= 0):
	if((numero % 3 == 0) and (numero % 5 == 0)):
		print("AuauMiau")
	elif (numero % 5 == 0):
		print("Miau")
	elif(numero % 3 == 0):
		print("Auau")
	else:
		print(numero)
else:
	print(numero)