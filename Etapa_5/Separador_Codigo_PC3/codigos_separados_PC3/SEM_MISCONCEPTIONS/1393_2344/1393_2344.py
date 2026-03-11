peso= float(input("Digite o valor do peso da encomenda:"))

if (peso <= 4999.9):
	frete= (peso * 0.05)
	print(round(frete,2))
	
else:
	(peso >= 5000)
	frete = ((peso * 0.04) + 60 )
	print(round(frete,2))