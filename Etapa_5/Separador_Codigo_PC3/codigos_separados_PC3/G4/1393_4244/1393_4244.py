p = float(input("Peso da encomenda: "))
a = (p*0.04)+60
b = p*0.05

if(p>= 5000):
	print(round(a, 2))
else:
	print(round(b, 2))