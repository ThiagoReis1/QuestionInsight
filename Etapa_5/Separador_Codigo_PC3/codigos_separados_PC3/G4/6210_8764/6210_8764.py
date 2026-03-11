n = int(input("Digite seu numero: "))

cont = 0

while (n != -1):
	if (n >= 35 and n <= 95):
		cont = cont + 1
	n = int(input("Digite seu numero: "))
print (cont)