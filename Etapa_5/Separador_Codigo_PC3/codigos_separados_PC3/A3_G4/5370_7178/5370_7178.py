from numpy import *

v=array(eval(input("digite um vetor: ")))
i=0
x=0
while(i!=size(v)):
	if(v[i]>v[i+1]):
		x="False"
		i=size(v)
	else:
		x="True"
		i=i+1
print(x)	
	