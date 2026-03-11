# Iserindo dados de entrada
x = int(input("Qual o numero desejado?: "))

if x % 31 == 0:
	print(x // 31)
	print("sim")
else:
	print(x % 31)
	print("nao")