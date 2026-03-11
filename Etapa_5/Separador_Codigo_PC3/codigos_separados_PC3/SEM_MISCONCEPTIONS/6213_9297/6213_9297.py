contador_eficiencia = 0

while True:
	numero = int(input("digite um numero: "))
	if numero == -1:
		break
	if 101 <= numero <= 201:
		contador_eficiencia += 1
print(contador_eficiencia)