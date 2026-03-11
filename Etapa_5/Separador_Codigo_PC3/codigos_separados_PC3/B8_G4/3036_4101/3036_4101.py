x = float(input("Valor de x: "))

if(x<=-1 or x>=1):
	y = x 
	print(round(y, 2))
elif(-1<x<0 or 0<x<1):
	y = 1
	print(round(y, 2))
elif(x==0):
	y = 2
	print(round(y, 2))