u=input("L/K: ")
vl=float(input("valor da medida: "))
if(u=="K"):
	lb=vl * 2.20462
	print(round(lb, 2))
else:
	kg=vl/2.20462
	print(round(kg, 2))
	
	
	