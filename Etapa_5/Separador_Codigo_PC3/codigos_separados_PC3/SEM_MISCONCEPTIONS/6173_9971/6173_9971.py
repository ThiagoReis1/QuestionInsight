simOUnao = input("").upper()
contador = 0
while (simOUnao != 'S'):
	if simOUnao == 'SIM':
		contador = contador + 1
	simOUnao = input("").upper()

print(contador)