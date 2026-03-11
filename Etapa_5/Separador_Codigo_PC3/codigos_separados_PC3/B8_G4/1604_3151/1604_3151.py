from numpy import*
z=array(eval(input()))
y=0
e=0
while(z[y]<=4):
	if(z[y]==1):
		e=e+80
	elif(z[y]==2):
		e=e+40
	elif(z[y]==3):
		e=e+20
	elif(z[y]==4):
		e=e+10
	y=y+1
print(e)
		
	

