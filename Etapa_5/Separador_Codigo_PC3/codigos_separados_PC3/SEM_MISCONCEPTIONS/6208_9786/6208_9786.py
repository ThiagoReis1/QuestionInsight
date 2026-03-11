numero = int(input(''))
contador = 0
while (numero != -1):
	if numero >= 51 and numero <=75:
		contador += 1
	numero = int(input(''))
	
print(contador)