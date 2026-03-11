peso = float(input("Insira o peso da encomenda, em gramas: "))

if peso < 5000:
	print(round(peso*0.05, 2))
else:
	print(round(peso*0.04 + 60 , 2))