from math import*
x=float(input())

if((x>=-1 and x<-1/2) or (x>1/2 and x<=1)):
	fx=asin(x)
	print(round(degrees(fx), 2))
elif(x>=-1/2 and x<=1/2):
	fx=acos(x)
	print(round(degrees(fx), 2))
else:
	print("entrada invalida")

