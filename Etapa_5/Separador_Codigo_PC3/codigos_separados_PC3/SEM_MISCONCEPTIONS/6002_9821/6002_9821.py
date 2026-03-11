mangas = float(input(" quantidade de mangas:"))

total = (3.80 * mangas)
total2 = (3.45 * mangas)

if mangas <= 6:
	print(round(total,2))
	
else:
	print(round(total2, 2))