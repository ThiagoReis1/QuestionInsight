peso = float(input("Qual o peso da encomenda? "))

if (peso >= 5000):
	frete = ((peso * 0.04)+60)
		
else:
	frete = peso * 0.05
	
print(round(frete, 2))