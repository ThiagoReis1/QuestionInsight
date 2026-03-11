escolha = input("Coxinha ou esfirra?C ou E?").upper()
quant = float(input("Quantas coxinhas ou esfirras? "))
qs = float(input("Quantos sucos? "))

if escolha.upper() == "C":
	valor = (2*quant) + (6*qs)
	print(round(valor, 2))

if escolha.upper() == "E":
	total = (4.5*quant) + (6*qs)
	print(round(total, 2))