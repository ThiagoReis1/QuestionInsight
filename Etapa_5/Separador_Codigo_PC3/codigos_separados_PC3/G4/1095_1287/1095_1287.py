x = float(input("digite o valor de x: "))
p = (x // 10000)
q = (x % 10000)
numero = (p + q)**2
if (numero == p ):
	print("X atende a propriedade")
else:
	print(numero)