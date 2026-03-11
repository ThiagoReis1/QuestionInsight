numero = int(input("Informe um numero: "))


contador = 0

while numero != -1:
	if numero >=45 and numero <=150:
		contador = contador + 1
	numero = int(input("Informe um numero: "))
print(contador)