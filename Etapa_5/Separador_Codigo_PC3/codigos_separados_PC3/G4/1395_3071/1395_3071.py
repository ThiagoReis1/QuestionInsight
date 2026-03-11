valor = float(input("Digite: "))
#excedeu:
e = valor - 1000
if (valor <= 1000):
	p = (valor * 5) / 100
	print(round(p, 2))
if (valor > 1000):
	q = ((1000 * 5) / 100) + ((e * 10) / 100) 
	print(round(q, 2))