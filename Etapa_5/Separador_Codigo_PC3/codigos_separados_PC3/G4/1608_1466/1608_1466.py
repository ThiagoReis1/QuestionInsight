from numpy import *
a=array(eval(input())).astype(dtype=int)
i=0
s=0
while(i<size(a)):
	s+=a[i]
	if(s>75):
		s=75
	i+=1
print(s)