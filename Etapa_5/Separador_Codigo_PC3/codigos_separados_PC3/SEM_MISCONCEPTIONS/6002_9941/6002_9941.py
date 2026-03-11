m= int(input("unidade de mangas: "))

if m<6:
	preco=(m*3.80)
	print(round(preco,6))
else:
	preco= m*3.45
	print(round(preco,6))