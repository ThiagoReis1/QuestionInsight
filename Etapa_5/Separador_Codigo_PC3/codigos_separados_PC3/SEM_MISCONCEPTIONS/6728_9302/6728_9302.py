numero = int(input("digite o numero: "))

if numero % 37 == 0:
	y = numero // 37
	print(y)
	print("sim")
	
else:
	y = numero % 37
	print(y)
	print("nao")