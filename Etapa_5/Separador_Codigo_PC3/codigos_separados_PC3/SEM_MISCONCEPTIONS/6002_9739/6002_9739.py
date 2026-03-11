mangas = float(input("Informe mangas: "))

if mangas < 6: 
	valor = mangas * 3.80
	print(round(valor, 2))
else: 
	valor = mangas * 3.45
	print(round(valor, 2))