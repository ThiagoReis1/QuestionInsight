from numpy import *
a=eval(input())
x=0
cont=0
recorde=217
while(x<size(a)):
	if(a[x]<recorde):
		cont+=1
	x+=1
print(recorde)
print(cont)
	
