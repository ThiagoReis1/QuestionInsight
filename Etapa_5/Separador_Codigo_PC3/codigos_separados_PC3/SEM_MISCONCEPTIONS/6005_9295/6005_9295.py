quant = int(input("Quantidade:"))

if quant < 5:
	a = quant * 3.80
	
else: 
	a = quant * 3.45
	
print(round(a, 2))