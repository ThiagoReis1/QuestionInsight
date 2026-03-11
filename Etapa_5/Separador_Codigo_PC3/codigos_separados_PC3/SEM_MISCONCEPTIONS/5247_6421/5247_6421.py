x = float(input("digite: "))
cod = int(input("digite: "))

print("Entradas: R$" , x, "e codigo " , cod)

if (x > 0):
	if (cod == 101):
		total = x + (x * 0.0080)
		print("Novo salario: R$", round(total, 2))
	elif (cod == 102):
		total = x + (x * 0.0065)
		print("Novo salario: R$", round(total, 2))
	elif (cod == 103):
		total = x + (x * 0.0060)
		print("Novo salario: R$", round(total, 2))
	elif (cod == 104):
		total  = x + (x * 0.0055)
		print("Novo salario: R$", round(total, 2))
	else:
		print("Dados invalidos")
else: 
	print("Dados invalidos")