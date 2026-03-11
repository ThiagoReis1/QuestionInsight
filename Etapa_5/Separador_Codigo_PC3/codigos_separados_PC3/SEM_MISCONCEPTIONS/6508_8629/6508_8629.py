# faça seu código aqui!
pcombo = 50

quantidade_combo_especial = int(input("quantidade combo especial: "))

if (quantidade_combo_especial > 4):
	desconto = ((pcombo * quantidade_combo_especial) * 12) / 100
	total = (pcombo * quantidade_combo_especial) - desconto
	print(round(total,2))
else: 
	total = (pcombo * quantidade_combo_especial)
	print(round(total,2))