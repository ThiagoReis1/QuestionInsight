numero = int(input("Digite o numero: "))

contador = 0

while numero != -1:
	if 26 <= numero and numero <= 50:
		contador = contador + 1
	numero = int(input("Digite um numero: "))
print(contador)