p = float(input(" "))
codigo = int(input(" "))
desconto = 40/100

if codigo  == 1: 
	f = 10
	venda = (p - p * desconto) + p * (f/100)
	print(round(venda,2))
elif codigo == 2: 
	f = 8 
	venda = (p - p * desconto) + p * (f/100)
	print(round(venda, 2))
	
elif codigo == 3: 
		f = 0 
		venda = (p - p * desconto) + p * (f/100)
		print(round(venda,2))

elif codigo == 4: 
	f = 2 
	venda = (p - p * desconto) + p * (f/100)
	print(round(venda,2))
