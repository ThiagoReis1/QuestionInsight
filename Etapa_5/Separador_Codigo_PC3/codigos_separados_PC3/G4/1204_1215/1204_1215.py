from numpy import *

v = array(eval(input("digite o vetor:")))

i = 0
k = 0
recorde = 2.5
while(i < size(v)):
	if(v[i] < recorde):
		k = k + 1
	i = i + 1
print(recorde)
print(k)
	   
