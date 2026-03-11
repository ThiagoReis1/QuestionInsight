mangas = int(input("Numero de mangas: "))

if mangas >= 6:
	val = mangas * 3.45
else:
	val = mangas * 3.8
	
print(round(val,2))