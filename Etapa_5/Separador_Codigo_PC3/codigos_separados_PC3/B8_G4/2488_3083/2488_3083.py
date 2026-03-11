x = float(input("salario: "))

if(x < 0.00):
	print("Entrada: R$", x)
	print("Dado invalido")
elif(x <= 800.00):
	y = x/100 * 50 + x
	print("Entrada: R$", x)
	print("Novo salario: R$", round(y, 2))
elif(800.00 < x <= 1000.00):
	y = x/100 * 40 + x
	print("Entrada: R$", x)
	print("Novo salario: R$", round(y, 2))
elif(1000.00 < x <= 1200.00):
	y = x/100 * 30 + x
	print("Entrada: R$", x)
	print("Novo salario: R$", round(y, 2))
elif(1200.00 < x <= 1400.00):
	y =  x/100 * 20 + x
	print("Entrada: R$", x)
	print("Novo salario: R$", round(y, 2))
elif(1400.00 < x <= 1600.00):
	y = x/100 * 10 + x
	print("Entrada: R$", x)
	print("Novo salario: R$", round(y, 2))
elif(x > 1600.00):
	y = x/100 * 5 + x
	print("Entrada: R$", x)
	print("Novo salario: R$", round(y, 2))