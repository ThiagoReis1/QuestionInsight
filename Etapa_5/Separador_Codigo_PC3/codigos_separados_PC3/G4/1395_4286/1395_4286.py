v = float(input("volume de vendas"))
if(v <= 1000):
	print(round(((5/100) * v), 2))
else: 
	print(round(((5/100) * 1000) + (10/100) * (v - 1000), 2))