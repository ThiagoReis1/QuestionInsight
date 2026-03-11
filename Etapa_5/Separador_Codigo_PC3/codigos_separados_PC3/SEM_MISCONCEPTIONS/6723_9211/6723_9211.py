x = int(input("numero "))
if x % 19 == 0:
	valor = x // 19
	print(valor)
	print("sim")
else:
	valor = x % 19
	print(valor)
	print("nao")