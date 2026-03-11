# Luiz Matheus Abecassis

compra1 = float(input("valor primeira compra: "))
compra2 = float(input("valor segunda compra: "))
compra3 = float(input("valor terceira compra: "))
compra4 = float(input("valor quarta compra: "))
limite = float(input("informe o seu limite: "))

valortotal = compra1 + compra2 + compra3 +compra4

print(round(valortotal, 2))

if (valortotal <= limite):
	print("Sim")
else:
	print("Nao")