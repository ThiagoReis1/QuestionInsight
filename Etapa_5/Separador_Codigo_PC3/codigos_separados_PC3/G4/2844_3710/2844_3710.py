from numpy import *

v = array(eval(input()))

f = zeros((size(v)), dtype=int)
y = 0

for i in range (size(v)): 
	f[y] = v[i]-1
	if(f[y] == -1):
		f[y] = 9
	y +=1
	
print(f)