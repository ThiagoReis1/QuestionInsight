numero = int(input("numero: "))
cont = 0
while numero != -1:
	if numero >= 0 and numero <= 25:
		cont = cont + 1
	numero = int(input("numero: "))
	
print(cont)	