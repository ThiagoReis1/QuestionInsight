produto = input("Selecione o produto (Bolo ou Croissant): ")
quantidade = int(input("Quantidade de produtos: "))
capp = int(input("Quantidade de cappuccinos:"))

if (produto.upper() == "B"):
	valor = (quantidade * 3) + (capp * 5.5)
	print(valor)
else:
	valor = (quantidade * 6) + (capp * 5.5)
	print(valor)				