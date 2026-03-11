mangas = int(input("Digite a quantidade de mangas: "))
if mangas < 6:
	total = mangas*3.8
else:
	total = mangas*3.45
print(round(total,2))