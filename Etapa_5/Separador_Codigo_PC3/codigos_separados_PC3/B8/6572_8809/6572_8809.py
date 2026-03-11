quant=int(input("quantidade de pizza: "))
if quant < 3:
	total=quant*5+3
elif quant == 3:
	total=quant*5+3.25
elif quant > 3:
	total=quant*5+4.50
print("total= ",round(total,2))