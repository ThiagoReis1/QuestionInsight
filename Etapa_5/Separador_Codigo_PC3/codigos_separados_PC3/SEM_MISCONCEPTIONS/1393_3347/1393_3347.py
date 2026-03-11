peso = float(input("peso da encomenda: "))
taxa = 60
frete1 = peso * 0.05
frete2 = (peso * 0.04) +  taxa

if( peso <= 4999.9):
	print(round(frete1, 2))
else:
	print(round(frete2, 2 ))

