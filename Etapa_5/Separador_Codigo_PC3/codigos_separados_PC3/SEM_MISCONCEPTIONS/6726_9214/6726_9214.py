x = int(input("numero inteiro"))
if x % 29 == 0:
	valor = x // 29
	print(valor)
	print("sim")
else:
	valor = x % 29
	print(valor)
	print("nao")