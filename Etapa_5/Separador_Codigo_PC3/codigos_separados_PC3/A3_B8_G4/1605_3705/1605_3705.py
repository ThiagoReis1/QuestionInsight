from numpy import *
anel= array (eval(input()))
i=0
x=200
y=0
while(i<size(anel)):
	if(anel[i]==1):
		anel[i]=x * 4
		x=anel[i]
	elif(anel[i]==2):	
		anel[i]=x * 2
		x=anel[i]
	elif(anel[i]==3):	
		anel[i]=x
		x=anel[i]
	elif(anel[i]==4):
		anel[i]=x/2
		x=anel[i]
	i=i+1

print(round(x,2))