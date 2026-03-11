x=float(input("valor de x:"))

if(x<=-1)or(x>=1):
	f=x
elif((x>-1)and(x<0))or((0<x)and(x<1)):
	f=1
elif(x==0):
	f=2
print(round(f, 2))