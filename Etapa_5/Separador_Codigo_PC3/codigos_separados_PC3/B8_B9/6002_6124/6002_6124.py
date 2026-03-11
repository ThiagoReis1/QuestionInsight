mangas = float(input("O numero de mangas compradas: "))
if mangas < 6:
	valor = mangas * 3.80
	print(round(valor,2))
else: 
	if mangas >= 6:
		valor = mangas * 3.45
		print(round(valor, 2))