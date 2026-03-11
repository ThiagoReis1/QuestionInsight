
compra = int(input("mangas: "))

if compra < 6:
	total = compra * 3.80
else:
	total = compra * 3.45
print(round(total, 2))