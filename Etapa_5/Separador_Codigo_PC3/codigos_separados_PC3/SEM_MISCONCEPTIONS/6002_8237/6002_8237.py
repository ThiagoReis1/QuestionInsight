mangas_c = int(input("Digite um valor:"))

if( mangas_c < 6):
	total = mangas_c * 3.80
	print(round(total, 2))
else:
	total = mangas_c * 3.45
	print(round(total,2))