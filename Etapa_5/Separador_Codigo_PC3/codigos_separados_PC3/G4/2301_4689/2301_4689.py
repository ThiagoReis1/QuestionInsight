import math
while(1):
	
	b=float(input(""))
	c=float(input(""))
	ang=float(input(""))
	r=math.sqrt(b**2+c**2-(2*b*c)*(math.cos(math.radians(ang))))
	print(round(r,2))