from math import*
x=float(input())

if(x<0 and x>=0):
	if(-1<=x and x<(-1/2)) or (1/2<x and x<=1):
		x=asin(x)
		y=(degrees(round(x,2)))
		print(round(y,2))
	elif((-1/2)<=x and x<=(1/2)):
		x=acos(x)
		y=(degrees(x,2))
		print(round(y,2))
else:
	print("entrada invalida")