pedido = input()
qLanche = int(input())
qRefri = int(input())

if(pedido.lower() == 'l'):
	total = (qLanche * 6.0) + (qRefri * 3.0)
	
if(pedido.lower() == 'p'):
	total = (qLanche * 4.5) + (qRefri * 3.0)
	
print(round(total, 2))