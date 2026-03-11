n = int(input("Digite o numero identificador: "))
contador = 0
while (n >= 0):
	if (n >= 45 and n <= 150):
		contador += 1
	n = int(input("Digite o numero identificador: "))
print (contador)