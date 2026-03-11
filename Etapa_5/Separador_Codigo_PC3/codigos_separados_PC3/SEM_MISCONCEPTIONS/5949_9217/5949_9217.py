pedido = str(input("B para bolo e C para croissant: "))
qtd_fatias = int(input("Quantidade de fatias: "))
qtd_cappuccinos = int(input("Quantidade de cappuccinos: "))

if pedido.upper() == "B":
	print( round( ( qtd_fatias * 3 ) + ( qtd_cappuccinos * 5.50 ), 2 ) )
else:
	print( round( ( qtd_fatias * 6 ) + ( qtd_cappuccinos * 5.50 ), 2 ) )