g = float(input("deposito inicial: "))
f = int(input("n meses a ser insirido: "))
total = g
e = 0
while(e < f):
	total = total + (total * 0.012)
	e = e + 1
	print(round(total, 2))