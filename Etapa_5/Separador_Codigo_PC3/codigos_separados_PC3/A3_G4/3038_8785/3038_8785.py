fx=float(input())
x=0
if fx<= -1 or fx>=1:
	x= abs(fx)**(1/2)
elif -1 < fx < 0 or 0 < fx < 1:
	x= abs(fx)
else:
	x= 0
	
print(round(x,2))
	
	
