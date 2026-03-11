pedido = input()

if pedido == 'C':
	quant = int(input())
	quant_suco = int(input())
	valor = quant*2 + quant_suco*6
	print(round(valor,2))
	
elif pedido == 'E':
	quant = int(input())
	quant_suco = int(input())
	valor = quant*4.5 + quant_suco*6
	print(round(valor,2))