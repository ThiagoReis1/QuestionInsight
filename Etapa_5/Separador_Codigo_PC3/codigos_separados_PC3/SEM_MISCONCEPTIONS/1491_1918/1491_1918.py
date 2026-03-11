a = float(input(""))
if( a >= 0):
	if(a >= 0 and a <= 5000):
		tarifa = 0.03
		taxa = 20
	elif(a > 5001 and a <= 6000):
		tarifa = 0.04
		taxa = 25
	elif(a > 6001 and a <= 7000):
		tarifa = 0.05
		taxa = 30
	else:
		tarifa = 0.06
		taxa = 35
	print(round(a*tarifa + taxa, 2))
else:
	print("Entrada invalida")
