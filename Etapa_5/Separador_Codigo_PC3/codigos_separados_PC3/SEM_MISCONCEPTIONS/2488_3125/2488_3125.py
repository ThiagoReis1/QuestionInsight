X = float(input("Salario:"))

if (X <= 800):
	Y = X + X * 0.5
	print(round("Entrada: R$", X),2)
	print((round("Novo salario: R$", Y),2)
elif (800 < X <= 1000):
	Y = X + X * 0.4
	print("Entrada: R$", X)
	print("Novo salario: R$", Y)
elif (X > 1000) or (X <= 1200):
	Y = X + X * 0.3
	print("Entrada: R$", X)
	print("Novo salario: R$", Y)
elif (X > 1200) or (X <= 1400):
	Y = X + X * 0.2
	print("Entrada: R$", X)
	print("Novo salario: R$", Y)
elif (X > 1400) or (X <=1600):
	Y = X + X * 0.1
	print("Entrada: R$", X)
	print("Novo salario: R$", Y)
elif (X > 1600):
	Y = X + X * 0.05
	print("Entrada: R$", X)
	print("Novo salario: R$", Y)
else:
	print("Entrada: R$", X)
	print("Dado invalido")