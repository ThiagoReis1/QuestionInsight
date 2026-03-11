solido = input("coxinha ou esfirra: ")
qtd = float(input("quantidade de coxinha ou esfirra: "))
suco_qtd = float(input("quantidade de sucos: "))

solido_C = 2.0
solido_E = 4.50
suco = 6.0

if solido == "C":
	conta = solido_C * qtd + suco * suco_qtd
	print(round(conta, 1))
else:
	conta = solido_E * qtd + suco * suco_qtd
	print(conta)