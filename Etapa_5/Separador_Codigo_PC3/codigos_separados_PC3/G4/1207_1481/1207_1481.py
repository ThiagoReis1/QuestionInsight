from numpy import *
v = array(eval(input("vain:")))
record = 98.48

i = 0
k = 0

while(i < size(v)):
	if(v[i] > record):
		k = k + 1
	i = i + 1	
print(record)
print(k)
