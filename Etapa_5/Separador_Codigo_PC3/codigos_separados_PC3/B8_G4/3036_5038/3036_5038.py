x = float(input("valor de x: "))
if((x<=-1)or (x>=1)):
	fx = x
	print(round(fx,2))
elif((-1<x and x<0) or (0<x and x<1)):
	fx = 1
	print(round(fx,2))
elif(x==0):
	fx = 2
	print(round(fx,2))