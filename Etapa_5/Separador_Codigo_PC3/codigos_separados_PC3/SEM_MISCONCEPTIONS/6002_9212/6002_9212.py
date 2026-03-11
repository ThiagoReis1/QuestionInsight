mangas = float(input("numero de mangas:"))

if mangas < 6:
	total = mangas * 3.80
	
else:

	total = mangas * 3.45
	
print(round(total,2))