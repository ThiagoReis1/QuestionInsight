numero = int(input("Digite um numero: "))

if (numero % 19 == 0):
	print(numero // 19)
	print("sim")
else:
	print(numero % 19)
	print("nao")