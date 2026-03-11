mangas = int(input("digite a quantidade de mangas: "))

valor = 3.80
valord = 3.45

if ( mangas >= 6):
	total = mangas*valord
	
else:
	total = mangas*valor

print(round(total, 2))