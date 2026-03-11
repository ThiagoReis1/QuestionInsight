manga = int(input("digite o numero de mangas: "))
cada1 = 3.80
mais_duzia = 3.45

if manga < 5:
	print(round(cada1  * manga, 2))
else:

	print(round(mais_duzia * manga, 2))