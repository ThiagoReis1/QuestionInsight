c=float(input("consumo:"))

t= (0.60 * c) + 5.00

t1= (0.75 * c) + 16.00

if c <= 150 :
	print(round(t,2))
	
else:
	print(round(t1,2))