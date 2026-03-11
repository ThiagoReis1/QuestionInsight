peso= float(input("Peso da encomenda: "))

if(peso < 5000.0):
	total= (0.05 * peso)
else:
	total= ((0.04 * peso) + 60.0)
print(round(total, 2))	