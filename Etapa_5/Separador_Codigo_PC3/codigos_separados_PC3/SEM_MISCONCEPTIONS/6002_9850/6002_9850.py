qtd = int(input("Quantidade de mangas compradas: "))

if qtd < 6:
	valor = qtd * 3.80
	print(round(valor,2))
else:
	valor = qtd * 3.45
	print(round(valor,2))
	