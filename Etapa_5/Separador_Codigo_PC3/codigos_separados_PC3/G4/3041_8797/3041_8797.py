from math import * 

x = float(input("valores de x" ))

if -1000<=x<-2:
	x = -1/(x+2)
	print(round(x , 4))
elif 2<x<=1000:
	x = 1/(x-2)
	print(round(x , 4))
else:
	print("entrada invalida")