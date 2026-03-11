x = float(input("salario atual: "))
y = int(input("codigo correspondente: "))
if (x<=0) or (y!=101 and y!=102 and y!=103 and y!=104):
	print("Entradas: R$", x,"e codigo", y)
	print("Dados invalidos")
elif(y == 101):
	z = (x * 0.0080) + x
	z = (round(z,2))
	print("Entradas: R$", x,"e codigo", y)
	print("Novo salario: R$", z)
elif(y == 102):
	z = (x * 0.0065) + x
	z = (round(z,2))
	print("Entradas: R$", x,"e codigo", y)
	print("Novo salario: R$", z)
elif(y == 103):
	z = (x * 0.0060) + x
	z = (round(z,2))
	print("Entradas: R$", x,"e codigo", y)
	print("Novo salario: R$", z)
else:
	z = (x * 0.0055) + x
	z = (round(z,2))
	print("Entradas: R$", x,"e codigo", y)
	print("Novo salario: R$", z)