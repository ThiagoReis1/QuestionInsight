m = int(input("Numero de mangas: "))

total = 0

if m >= 6:
	total = m * 3.45
	print(round(total,2))
else:
	total = m * 3.8
	print(round(total,2))