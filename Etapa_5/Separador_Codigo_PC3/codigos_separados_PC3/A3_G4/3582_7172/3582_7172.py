from numpy import*
x=array(eval(input("x")))
c=0
p=0
y=0
d=0
while(size(x)>c):
	if(x[c]>160):
		
		y=y+x[c]-25
		c=c+1
	else:
		y=y+x[c]
		c=c+1
print(round(y,2))