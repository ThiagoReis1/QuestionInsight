abr =round(float(input()), 2)
fec =round(float(input()), 2)
per=fec-abr
if ( per< 0) :
	print("saldo negativo")
else :
	if (abr==fec) :
		print("sem variacao")
	else :
		print("saldo positivo")
