p = float(input("peso da encomenda"))
if(p<5000):
	encomenda= p*0.05
	print(round(encomenda,2))
else:
	enco = p*0.04+60
	print(round(enco,2))