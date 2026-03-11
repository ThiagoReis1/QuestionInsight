peso=float(input("Coloque o peso:"))
if(0 <= peso <= 5000 ):
	tarifa=0.03
	taxa=20
	total= (peso * tarifa) + taxa
	print(round(total, 2))
elif(5001 < peso <= 6000):
	tarifa=0.04
	taxa=25
	total= (peso * tarifa) + taxa
	print(round(total, 2))
elif(6001 < peso <= 7000):
	tarifa=0.05
	taxa=30
	total= (peso * tarifa) + taxa
	print(round(total, 2))
elif(peso > 7000):
	tarifa=0.06
	taxa=35
	total= (peso * tarifa) + taxa
	print(round(total, 2))