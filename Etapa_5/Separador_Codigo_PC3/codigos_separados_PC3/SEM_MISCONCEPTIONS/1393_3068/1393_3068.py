enc = float(input("Peso da Encomenda (g):"))
if (enc < 5000):
	preco = enc * .05
else:	
	preco = 60 + enc * .04
print(round(preco,2))