x = int(input("Digite um numero para verificar se ele e divisivel por 19: "))


if (x % 19 == 0):
	print(x // 19)
	print("sim")
else:
	print(x % 19)
	print("nao")