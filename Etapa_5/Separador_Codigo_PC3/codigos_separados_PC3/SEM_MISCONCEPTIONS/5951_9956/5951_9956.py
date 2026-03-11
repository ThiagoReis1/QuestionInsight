pedido = input()
quant = int(input())
a = int(input())

if pedido.upper()== "T" :
	print(round(4.50*quant+a*12,1))
if pedido.upper()== "S":
	print(round(5*quant+a*12,1))