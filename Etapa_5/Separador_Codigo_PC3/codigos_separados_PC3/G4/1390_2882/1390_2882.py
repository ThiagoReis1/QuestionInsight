c=int(input("Consumo: "))

if(c<=100):
	x1=(1.20*c)
	print(float(round(x1,2)))
	
else:
	x2=(1.4*c)+25
	print(float(round(x2,2)))