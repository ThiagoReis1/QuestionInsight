from numpy import *

a=array(eval(input("Vetor: ")))

i=0
x=0

while(size(a)>i):
	if(a[i]==1):
		x=x+80
	elif(a[i]==2):
		x=x+40
	elif(a[i]==3):
		x=x+20
	elif(a[i]==4):
		x=x+10
	i=i+1
	
print(x)