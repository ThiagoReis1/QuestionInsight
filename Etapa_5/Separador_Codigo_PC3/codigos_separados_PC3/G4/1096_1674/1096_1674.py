x = int(input("Qual o numero?"))
a = x // 10000
b = ( x % 10000 ) // 100
c = ( (x % 10000) % 100) // 1
valor = a ** 3 + b ** 3 + c ** 3
if( x == a ** 3 + b ** 3 + c ** 3):
	print(x," atende a propriedade")
else:
	print(valor)
