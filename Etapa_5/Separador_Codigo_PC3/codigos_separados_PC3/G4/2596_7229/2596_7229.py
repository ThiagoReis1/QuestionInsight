from numpy import *

p=array(eval(input()))
m=1
l=0	 
while m<size(p):
	if p[m]>=p[0]:
		l=l+1
		print(m)
	m=m+1
	
print(l)