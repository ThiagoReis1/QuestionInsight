numero = int(input())
contador = 0

while numero != -1:
	if numero >= 26 and numero <= 85:
		contador += 1
	numero = int(input())

print(contador)