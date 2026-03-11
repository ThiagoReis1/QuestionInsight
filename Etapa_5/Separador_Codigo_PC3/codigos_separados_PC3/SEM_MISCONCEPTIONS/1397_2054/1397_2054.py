area = int(input("informar area em hectare: "))

if(area <= 10000):
	custo = float(round(area*5.00, 2))
	print("valor total: ", custo)
	
else:
	custo = float(round((50000 + (area - 10000)*4.00), 2))
	print("valor total: ", custo)