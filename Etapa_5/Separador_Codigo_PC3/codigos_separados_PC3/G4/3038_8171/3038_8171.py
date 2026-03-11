x=float(input(""))

if (x<=-1 or x>=1):
	x=abs(x)**0.5
elif x==0:
	x=0
else:
	x=abs(x)
	
print(round(x,2))