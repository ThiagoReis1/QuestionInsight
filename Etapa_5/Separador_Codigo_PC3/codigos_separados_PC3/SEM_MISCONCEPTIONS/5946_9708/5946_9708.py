pedido = input("digite o pedido ")
quant = int(input("digite a quantidade: "))
refri = int(input("digite a quantidade: "))
if pedido == "L":
	valor = ((quant*6.00)+(refri*3.00))
	print(round(valor, 2))
else:
	valor1 = ((quant*4.50)+(refri*3.00))
	print(round(valor1, 2))