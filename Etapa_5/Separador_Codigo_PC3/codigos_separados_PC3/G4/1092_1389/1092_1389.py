n = float(input(" numero: "))

x = n // 100
rx = n % 100
y = rx // 10
ry = rx % 10
z = ry

numero = (x**3) + (y**3) + (z**3)

if(numero < 0):
	print(numero, " X atende a propriedade ")
else:
	print((numero))