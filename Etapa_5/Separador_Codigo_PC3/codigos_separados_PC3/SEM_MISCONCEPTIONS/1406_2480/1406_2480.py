tipo = input("Tipo de ataque: ")
valor = int(input("Valor: "))
rodadas = int(input("Número de turnos: "))

if (tipo == "cauda"):
	dano = valor * rodadas
	print(dano)
else:
	dano = (2 * valor) * rodadas
	print(dano)