from numpy import*
x=array(eval(input("x: ")))
t=size(x)
c=0
y=0
while(t>c):
	if(x[c]>90):
		y=y+x[c]-6.50
		c=c+1
	else:
		y=y+x[c]
		c=c+1
print(round(y,2))