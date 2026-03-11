from numpy import *
x=array(eval(input()))
y=0
z=0
while(x[y]<4):
	if(x[y]==1):
		z=z+80
	elif(x[y]==2):
		z=z+40
	elif(x[y]==3):
		z=z+20
	y=y+1
print(z)