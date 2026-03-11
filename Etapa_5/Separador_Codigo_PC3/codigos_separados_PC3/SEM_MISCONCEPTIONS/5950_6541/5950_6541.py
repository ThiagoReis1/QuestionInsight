pedido = input()
qt = int(input())
qt_cappuccionos = int(input())

if pedido == 'T':
	pagar = (qt * 6.00) + (qt_cappuccionos * 4.50) 
else:
	pagar = (qt * 5.00) + (qt_cappuccionos * 4.50)
	
print(round(pagar, 2))