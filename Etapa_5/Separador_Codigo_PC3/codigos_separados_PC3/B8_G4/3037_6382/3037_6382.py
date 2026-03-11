x=float(input("X "))

if(x<=-1 or x>=1):
	y=x**2
	print(round(y, 4))
elif((-1<x and x<0) or (0<x and x<1)):
	y=x
	print(round(y, 4))
elif(x==0):
	y=1
	print(round(y, 4))
