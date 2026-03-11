h = float(input("Informe o horario em que o prato foi pedido: "))
q = int(input("Informe a quantidade de pratos: "))

p = 28.50

if h >= 18:
	p1 = (q * p) - (p * q) * 0.2
else:
	p1 = q * p
	
print(round(p1, 2))