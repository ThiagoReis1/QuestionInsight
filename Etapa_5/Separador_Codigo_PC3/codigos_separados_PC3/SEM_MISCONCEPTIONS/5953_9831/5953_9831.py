pedido= str(input("Entre com (L) Lanche ou (P) Prato Executivo: "))
qtde= int(input("Entre com a qtde de pedidos: "))
qtdeR= int(input("Entre com a qtde de refrigerantes: "))


if pedido == 'L':
	cst= (qtde * 6.00) + (qtdeR * 3.00)

else: 
	cst= (qtde * 13.50) + (qtdeR * 3.00)

print(cst)