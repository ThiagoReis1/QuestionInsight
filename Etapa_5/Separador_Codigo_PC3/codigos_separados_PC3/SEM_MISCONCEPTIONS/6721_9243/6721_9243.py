numero = int(input("numero: "))
quociente = numero // 13
	
if numero % 13 == 0:
	print (quociente)
	print ("sim")
else:
	print(numero % 13)
	print("nao")