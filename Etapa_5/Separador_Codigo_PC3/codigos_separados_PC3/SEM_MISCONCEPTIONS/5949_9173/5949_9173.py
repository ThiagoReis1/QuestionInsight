pedido = input (" vc quer (B) ou (C): ")
qtde_comida = int(input("qtde de fatia de Bolo ou Croissant: "))
qtde_croissant = int(input("qtde de Cappuccino: ")) 
valor_fatia_bolo = 3.00
valor_croissant = 6.00
valor_cappuccino = 5.50

if pedido == "B":
	valor_total_1 = ( qtde_comida * valor_fatia_bolo ) + ( qtde_croissant *  valor_cappuccino )
	print(round(valor_total_1 , 2))
	
else: 
	valor_total_2 = ( qtde_comida  *  valor_croissant ) + ( valor_cappuccino  * qtde_croissant )
	print(round( valor_total_2 , 2))

