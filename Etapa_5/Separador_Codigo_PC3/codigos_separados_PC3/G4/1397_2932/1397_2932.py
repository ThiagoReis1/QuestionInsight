#entradas
hec = float(input("Hectares: "))
h1 = 10000
v1 = float(5.0)
v2 = float(4.0)
if(hec <= h1):
	cus = hec * v1
	print(round(cus, 2))
	
else:
	cus = h1 * v1
	cus = ((hec - h1) * v2) + cus
	print(round(cus, 2))
	