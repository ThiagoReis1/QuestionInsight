numero = int(input("numero negativo: "))
cont = 0	
				 
while (numero >= 0):
	if (numero >= 26 and numero <= 50):
		cont = cont + 1
	numero = int(input("numero negativo: "))
print(cont)