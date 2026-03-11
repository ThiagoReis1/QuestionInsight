mangas = int(input())

if mangas < 6 :
	p_mangas = 3.80 * mangas
	print(round(p_mangas,2))
else:
	p_mangas = 3.45 * mangas
	print(round(p_mangas, 2))