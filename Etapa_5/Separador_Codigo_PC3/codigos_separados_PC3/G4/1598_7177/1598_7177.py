from numpy import*
v=array(eval(input("x:")))
c=0
x=0
while(size(v)>c):
	if(v[c]>90):
		x=x+v[c]-6.50
		c=c+1
	else:
		x=x+v[c]
		c=c+1
print(round(x,2))