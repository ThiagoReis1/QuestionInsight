al = 1.65
tl = 0.02
c=0
x= float(input())
t= float(input())
while al>x:
	al=al+tl
	x=x+t
	c=c+1
print(c)