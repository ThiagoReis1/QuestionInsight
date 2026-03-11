x = int(input("Digite um numero para verificar a divisao: "))

if (x % 31) == 0:
	print(x // 31)
	print("sim")
else:
	print(x % 31)
	print("nao")