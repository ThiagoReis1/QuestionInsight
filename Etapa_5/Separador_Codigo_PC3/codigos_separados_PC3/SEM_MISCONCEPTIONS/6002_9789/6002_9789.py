numero_mangas = int(input( "digite o numero de mangas:"))
if numero_mangas < 6:
	valor_total = numero_mangas * 3.80
else:
	valor_total = numero_mangas * 3.45
	
print(round(valor_total, 2))
