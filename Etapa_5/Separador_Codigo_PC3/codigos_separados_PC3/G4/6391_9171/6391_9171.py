from numpy import *

n = array(eval(input()))
nv = zeros(size(n), dtype = int)

for i in range(size(n)):
	if n[i] == 0:
		nv[i] = 9**3
	
	else:
		nv[i] = (n[i] - 1) ** 3
		
print(nv)