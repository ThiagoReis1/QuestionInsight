# Mayume Ihara Lima Rodrigues - 21602330
# Avaliacao 3
# Exercicio 1
# 21/07/16

x = float(input("valor do salario:"))
y = int(input("codigo:"))

print("Entradas: R$", x, "e codigo", y)

if (y == 101 and x > 0):
	z = x + (x * 0.08/100)
	print("Novo salario: R$", round(z, 2))
elif(y == 102 and x >0):
	z = x + (x * 0.65/100)
	print("Novo salario: R$", round(z, 2))
elif(y == 103 and x>0):
	z = x + (x * 0.60/100)
	print("Novo salario: R$", round(z, 2))
elif(y ==104 and x > 0):
	z = x + (x * 0.55/100)
	print("Novo salario: R$", round(z, 2))
else:
	print("Dados invalidos")