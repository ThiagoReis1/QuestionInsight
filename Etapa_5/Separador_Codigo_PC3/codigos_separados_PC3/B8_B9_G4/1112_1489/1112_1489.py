# Leticia Filardi
# Avaliação 3

X = float (input ("Salario:"))

print ("Entrada: R$", X)

if X < 0:
	print ("Dado invalido")
elif X <= 800.0:
	Y = X * 1.5
	print ("Novo salario: R$", round (Y, 2))
elif X > 800.0 and X <= 1000.0:
	Y = X * 1.4
	print ("Novo salario: R$", round (Y, 2))
elif X > 1000.0 and X <= 1200.0:
	Y = X * 1.3
	print ("Novo salario: R$", round (Y, 2))
elif X > 1200.0 and X <= 1400.0:
	Y = X * 1.2
	print ("Novo salario: R$", round (Y, 2))
elif X > 1400.0 and X <= 1600.0:
	Y = X * 1.1
	print ("Novo salario: R$", round (Y, 2))
elif X > 1600.0:
	Y = X * 1.05
	print ("Novo salario: R$", round (Y, 2))