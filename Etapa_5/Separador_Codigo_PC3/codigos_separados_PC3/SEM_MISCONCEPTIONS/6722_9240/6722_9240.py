numero = int(input("Numero: "))
quociente = numero // 17

if numero % 17 == 0:
	print (quociente)  
	print ("sim")
else:
	print (numero % 17)
	print ("nao")