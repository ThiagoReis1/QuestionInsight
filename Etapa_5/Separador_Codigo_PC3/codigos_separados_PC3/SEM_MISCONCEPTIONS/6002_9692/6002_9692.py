mangas = int(input("insira a quantidade de mangas: "))

if mangas >= 6:
	total = mangas*3.45  
else:
	total = mangas*3.80
print(round(total,2))