numero = int(input("numero: "))
cont = 0
while numero > 0:
	if numero >= 100 and numero <= 199:
		cont = cont + 1
	numero = int(input("numero: "))
print(cont)