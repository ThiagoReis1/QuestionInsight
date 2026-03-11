ca = int(input("Digite o consumo de agua:"))

tx = (3 * ca) + 30
v = (3.50 * ca) + 30

if(ca < 10):
	print(round(tx, 2))
else:
	print(round(v, 2))