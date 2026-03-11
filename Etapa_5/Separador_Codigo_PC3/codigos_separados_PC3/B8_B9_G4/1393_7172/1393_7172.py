p=float(input("peso da encomenda: "))

if(p<=5000):
	vc=(p*0.05)
else:
	if(p>5000):
		vc=(p*0.04+60.00)
print(round(vc, 2))