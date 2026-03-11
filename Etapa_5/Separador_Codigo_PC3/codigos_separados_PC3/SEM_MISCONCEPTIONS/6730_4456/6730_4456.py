numero = int(input())

if numero % 43 == 0:
	print(numero // 43)
	print("sim")
else:
	print(numero % 43)
	print("nao")