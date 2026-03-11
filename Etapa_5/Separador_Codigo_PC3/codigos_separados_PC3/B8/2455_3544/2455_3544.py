nivel = int(input("nivel:"))
hora = float(input("hora:"))
if nivel == 1:
	salario = 12 * hora
elif nivel == 2:
	salario = 17 * hora
elif nivel == 3:
	salario = 25 * hora
print(round(salario, 2))