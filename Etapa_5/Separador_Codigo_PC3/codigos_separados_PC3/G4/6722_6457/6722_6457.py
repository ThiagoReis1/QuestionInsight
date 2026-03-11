x = int(input("Digite o numero inteiro: "))

if x % 17 == 0:
	print(x // 17)
	print("sim")
else:
	print(x % 17)
	print("nao")