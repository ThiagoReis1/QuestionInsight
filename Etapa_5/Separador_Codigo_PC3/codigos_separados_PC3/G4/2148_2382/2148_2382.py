from numpy import *

v=array(eval(input()))
s=0
cont=0
for i in range(size(v)):
	s=s+v[i]
	if(v[i]>=5):
		cont=cont + 1
		

print(s)
print(cont)