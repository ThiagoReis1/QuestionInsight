pedido = input().upper()
qtd = int(input())
qtdCappu = int(input())

if(pedido == 'S'):
	print(round((qtd*4.00 + qtdCappu*7.5),2))
else:
	print(round((qtd*5 + qtdCappu*7.5),2))