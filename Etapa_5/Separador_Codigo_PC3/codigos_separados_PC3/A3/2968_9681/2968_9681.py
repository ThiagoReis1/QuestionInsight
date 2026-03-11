item = str(input("Qual pedido deseja, L para lanche ou S para salgado?")).upper
quantidade = int(input("Quantidade de lanches ou salgados: "))
refri = int(input("Quantidade de refrigerantes desejada: "))

if item == "L":
	total = (item * 3.5)+ refri
	print(total)
else:
	final = (item * 5) + refri
	print(final)