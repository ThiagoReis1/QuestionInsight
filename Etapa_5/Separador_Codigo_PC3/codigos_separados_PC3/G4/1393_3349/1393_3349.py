p = float(input("Insira o peso da encomenda em gramas: "))
e1 = p * 0.05
e2 = (p * 0.04) + 60
if(p < 5000.0):
	print(round(e1,2))
else:
	print(round(e2,2))