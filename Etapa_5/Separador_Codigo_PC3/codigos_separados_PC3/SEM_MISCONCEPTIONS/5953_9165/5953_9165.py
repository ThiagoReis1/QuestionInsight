pedido = input("L se for lanche ou P se for prato executivo: ").upper()
qnt = int(input("Quantidade de lanches ou PE: ")) 
R = int(input("Quantidade de refrigerantes: "))

refri = R * 3
l = qnt * 6
pe = qnt * 13.50

if pedido == "L":
	print(round(refri + l, 2))
else:
	print(round(refri + pe, 2))

	

