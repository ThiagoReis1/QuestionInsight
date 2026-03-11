mangas = float(input())

if  mangas >= 6:
	p_mangas = 3.45 * mangas
else:
	p_mangas = 3.80 * mangas 
print(round(p_mangas, 2))
