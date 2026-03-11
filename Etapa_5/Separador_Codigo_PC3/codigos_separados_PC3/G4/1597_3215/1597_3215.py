from numpy import *
x=array(eval(input()))
y=0
while(y<len(x)):
	if(x[y]>80):
		x[y]=x[y]-5
		y=y+1
	else:			
		x[y]=x[y]+0
		y=y+1
print(round(sum(x),2))
