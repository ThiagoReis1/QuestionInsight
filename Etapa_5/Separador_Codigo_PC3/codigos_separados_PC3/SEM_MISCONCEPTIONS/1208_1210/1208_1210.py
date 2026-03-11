from numpy import *
distancias=array(eval(input("Distancias:")))
i=0
s=0
recorde=98.48
print(recorde)
while(i<size(distancias)):
	if(distancias[i]<recorde):
		i=i+1
		s=s+1
	else:
		i=i+1
print(s)
