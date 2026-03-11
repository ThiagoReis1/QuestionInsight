prod = float(input("valor do produto: "))

if(prod<= 50):
	venda = prod +(prod*1)
	print(round(venda,2))
else:
	if(50<prod<=100):
		venda = prod + (prod*5/10)
		print(round(venda,2))
	else:
		if(100<prod<=500):
			venda = prod + (prod*4/10)
			print(round(venda, 2))
		else:
			venda = prod + (prod*3/10)
			print(round(venda, 2))