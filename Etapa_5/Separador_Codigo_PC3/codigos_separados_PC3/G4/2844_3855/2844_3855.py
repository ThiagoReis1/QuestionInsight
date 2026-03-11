from numpy import *

n = array(eval(input()))
v = zeros(size(n),dtype=int)

for i in range (size(n)):
	v[i]=n[i]-1
	if (n[i] == 0):
		v[i] = 9
			
print(v)
		