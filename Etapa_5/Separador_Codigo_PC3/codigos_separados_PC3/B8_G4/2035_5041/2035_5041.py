num = int(input("Informe um numero: "))

cont = 0
while num != 0:
	if num > 0:
		print("positivo".upper())
	elif num < 0:
		print("negativo".upper())
	cont = cont + 1
	num = int(input("Informe um numero: "))
		