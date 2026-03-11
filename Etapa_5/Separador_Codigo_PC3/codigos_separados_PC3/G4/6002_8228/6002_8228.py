m = int(input("quantidade de mangas: "))
c1 = m * 3.80
cm = m * 3.45
if (m < 6):
	print(round(c1, 2))
if (m >= 6):
	print(round(cm, 2))