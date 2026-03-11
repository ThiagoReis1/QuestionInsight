from numpy import *

x=array(eval(input("Vetor: ")))

i=0
a=0

while(i<size(x)):
	if(x[i]>160):
		a=a+x[i]-25
	else:
		a=a+x[i]
	i=i+1
	
print(a)