tipo = input("Tipo de Ataque:")
valor = int(input("Valor:"))
n = int(input("Turnos:"))

if (tipo == 'cauda'):
	aux = n*valor
	print(aux)
else:
	if (tipo == 'cuspe'):
		aux = 2*n*valor
		print(aux)
