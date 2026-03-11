mangas_compradas = int(input())

if mangas_compradas < 6:
	manga = 3.8
	print(round(mangas_compradas * manga,2))
else:
	manga = 3.45
	print(round(mangas_compradas * manga,2))