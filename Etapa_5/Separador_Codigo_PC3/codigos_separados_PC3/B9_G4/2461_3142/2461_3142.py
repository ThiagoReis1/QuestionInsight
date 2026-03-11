p = float(input("Preco de custo do produto: "))

if(p > 0):
	if(p <= 50.0):
		d = p + (1 * p)
		print(round(d,2))
	elif(p > 50.0 and p <= 100.0):
		d = p + (0.50 * p)
		print(round(d,2))
	elif(p > 100.0 and p <= 500.0):
		d = p + (0.40 * p)
		print(round(d,2))
	else:
		d = p + (0.30 * p)
		print(round(d,2))
