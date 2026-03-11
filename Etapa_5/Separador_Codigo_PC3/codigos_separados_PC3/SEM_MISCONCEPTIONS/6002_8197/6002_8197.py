quantidade_manga = int(input("Quantas mangas voce comprou? "))

if (quantidade_manga < 6):
	print(round(quantidade_manga * 3.8, 2))
else:
	print(round(quantidade_manga * 3.45, 2))