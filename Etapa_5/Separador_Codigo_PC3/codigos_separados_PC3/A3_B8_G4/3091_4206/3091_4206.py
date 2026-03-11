a = input()
x = 0
y = 0
z = 0
d = 0
s = 0
a1 = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
while((a.upper())!="X"):
	if((a.upper())=="V"):
		x = x+3
		x1 = x1+3
		a = input()
	elif((a.upper())=="E"):
		y = y+1
		x2 = x2+3
		a = input()
	elif((a.upper())=="D"):
		z = z+0
		x3 = x3+3
		a = input()
	elif((a.upper())!="X" and (a.upper())!="V" and (a.upper())!="E" and (a.upper())!="D"):
		a1 = a1+0
		x4 = x4+0
		a = input()
if((a.upper())=="X"):
	s = x+y+z+a1
	d = x1+x2+x3+x4
	print(round((s/d)*100,2))
	
	
		
		