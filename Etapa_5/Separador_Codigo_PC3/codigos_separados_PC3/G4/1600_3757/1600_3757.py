from numpy import*
x=array(eval(input("x:")))
t=size(x)
c=0
y=0
while(c<t):
	if(x[c]>80):
		y=y+(x[c]-(x[c]*0.15))
		c=c+1
	else:
		y=y+x[c]
		c=c+1
print(round(y,2))