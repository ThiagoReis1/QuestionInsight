pedido = input("digite L para lanche e P para pizzas")
qtd_l = int(input("digite a quantidade de pizzas"))
qtd_ref = int(input("digite a quantidade de refrigerantes"))

if pedido.upper() == "L": 
	valor = (qtd_l * 6) + (qtd_ref * 3)
	print(round(valor, 1))
else: 
	valor = (qtd_l * 4.50) + (qtd_ref * 3)
	print(round(valor, 1))