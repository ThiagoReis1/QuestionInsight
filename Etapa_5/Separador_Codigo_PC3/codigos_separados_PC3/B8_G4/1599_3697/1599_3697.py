from numpy import*
from numpy.linalg import*

c=array(eval(input()))
t=0
d=0
k1=0
while(t<size(c)):
	if(c[t]>80.0):
		d=(c[t]-(c[t]*15)/100)+d
		t=t+1
	elif(c[t]<80.0):
		k1=c[t]+k1
		t=t+1
k=d+k1
print(round(k,2))