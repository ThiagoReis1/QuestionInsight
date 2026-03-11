num_maca = int(input())


if num_maca < 12:
	valor_total = 0.3*num_maca 
	print(round(valor_total, 2))
	
else:
	valor_total = 0.25*num_maca
	print(round(valor_total, 2))