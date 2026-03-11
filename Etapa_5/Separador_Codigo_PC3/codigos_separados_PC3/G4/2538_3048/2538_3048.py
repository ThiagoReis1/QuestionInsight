s = float(input("valor do sitio: "))
d = float(input("valor depositado: "))
m = float(input("deposito mensal: "))
j = float(input("taxa de juros: "))

if((s > 0) and (d > 0) and (m > 0) and (j > 0)):
	a = (m * j / 100) * d
	print(round(a, 2))
else:
	print("Dados incorretos")
	
	
	