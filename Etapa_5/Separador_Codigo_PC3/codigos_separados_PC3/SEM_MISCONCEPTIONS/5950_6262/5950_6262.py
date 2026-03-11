tipo_item = input("Digite o tipo de item que deseja(T para torta e P par pastel):")
quantidade = int(input("Digite a quantidade de itens que deseja:"))

quantidade_capuccino = int(input("Digite a quantidade de capuccinos que deseja:"))

if tipo_item == "T":
	preco_item = 6.0
elif topo_item == "P":
	preco_item = 5.0
	
preco_total = (preco_item*quantidade) + (4.5*quantidade_capuccino)
	print(round(preco_total,2))