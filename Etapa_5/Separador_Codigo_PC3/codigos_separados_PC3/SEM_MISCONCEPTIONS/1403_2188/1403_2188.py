armadura = input("Insira a armadura: malha/placa ")
fator_d = int(input())

if (armadura.lower() == "malha"):
	print((15 * fator_d) - 1)
else:
	print((20 * fator_d) - 18)