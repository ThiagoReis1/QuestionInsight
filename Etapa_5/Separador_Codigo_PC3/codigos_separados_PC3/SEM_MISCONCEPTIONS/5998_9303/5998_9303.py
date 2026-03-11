quant_maca = int(input("maca: "))
preco1 = quant_maca * 0.30
preco2 = quant_maca * 0.25

if quant_maca < 12:
	print(round(preco1,2))
else:
	print(round(preco2,2))
