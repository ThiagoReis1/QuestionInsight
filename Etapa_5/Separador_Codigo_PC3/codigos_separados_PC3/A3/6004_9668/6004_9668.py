tomat= 0.75

tomat_comp= int(input("quantos tomatos foram comprados ?"))

if tomat_comp >= 4:
	prom= tomat_comp * 0.55
	print(round(prom, 2))
	
else:
	ttomat= tomat_comp * 0.75
	print(round(ttomat, 2))