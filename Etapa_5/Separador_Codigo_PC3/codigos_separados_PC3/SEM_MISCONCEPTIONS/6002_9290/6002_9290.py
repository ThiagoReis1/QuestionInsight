num = int(input("numero de mangas"))
######################
if num < 6:
	valor = 3.80 * num
	print(round(valor,2))
if num >= 6:
	valor = 3.45 * num
	print(round(valor,2))