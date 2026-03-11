numero = int(input("Numero: "))
quociente = numero // 19

if numero % 19 == 0:
	print(quociente)
	print("sim")
else:
	print(numero % 19)
	print("nao")
	