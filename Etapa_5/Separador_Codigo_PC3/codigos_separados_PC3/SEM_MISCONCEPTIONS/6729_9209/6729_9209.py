numero_x = int(input("Digite um numero inteiro: "))
quo = numero_x //41
if numero_x % 41 == 0:
	print(quo)
	print("sim")
else:
	print(numero_x % 41)
	print("nao")