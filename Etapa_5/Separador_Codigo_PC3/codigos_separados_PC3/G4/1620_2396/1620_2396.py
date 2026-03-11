from numpy import *
v=array(eval(input()))
vet=array(eval(input()))
i=0
s=0
while(i<size(v)):
	s=s+5*(vet[i]/100)*v[i]	
	
	i=i+1
	
	
print(round(s,2))



