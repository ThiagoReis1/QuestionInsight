numero = int(input("numero "))
a = numero // 1000
b = a%1000 // 1
c = (a + b)*(a + b)
if( c == numero ):
	print(numero,"atende a propriedade")
else:
	print(c)