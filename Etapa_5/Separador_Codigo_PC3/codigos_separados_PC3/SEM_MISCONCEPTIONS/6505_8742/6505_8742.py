tipo_combo = input("Qual combo deseja (A/B/C): ")
if tipo_combo.upper() == "A" or tipo_combo.upper() == "B":
	combos = int(input("quantos combos: ")) * 30
	print(round(combos, 2))
else:
	combos = int(input("quantos combos: "))
	valor = combos * 30
	desconto = 30 *combos * 0.15
	total = valor - desconto
	print(total)
	