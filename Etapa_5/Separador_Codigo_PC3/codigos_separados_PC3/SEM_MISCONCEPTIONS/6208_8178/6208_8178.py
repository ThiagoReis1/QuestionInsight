numero = int(input("insira um numero: "))
contador_ns = 0

while numero != -1:
	if 51 <= numero <= 75:
		contador_ns += 1
	numero = int(input("insira um numero: "))
print(contador_ns)