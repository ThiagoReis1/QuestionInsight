pedido= input("t se for uma tapioca ou s se for salgado: ")
a1 = int(input("quantidade de produto: "))
acai= int(input("quantidade de acai: "))

if(pedido.upper() == "T"):
	x= (a1 * 4.50) + (acai * 12)
	print(round(x, 2))
	
if(pedido.upper() == "S"):
	y= (a1 * 5) + (acai * 12)
	print(round(y, 2))