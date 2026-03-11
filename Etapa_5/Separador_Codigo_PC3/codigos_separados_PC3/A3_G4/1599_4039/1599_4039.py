from numpy import *

vet = array(eval(input()))
m=0
i=0
t=0
while(i<size(vet)):
	if(vet[i]>80.0):
		m=vet[i]-(vet[i]*0.15)
		t=t+m
	else:
		t=t+vet[i]
		
	i=i+1
	
print(round(t, 2))

