numero = int(input("digite um numero:"))
contador = 0
while (numero != -1):
	if (numero >= 101 and numero <= 201):
		contador += 1
	numero = int(input("digite um numero:"))
print(contador)