from numpy import *
v = array(eval(input("valor: ")))
v1 = zeros(size(v), dtype = int)

for i in range(size(v)):
	if v[i] == 0:
		v1[i] = v[i]*2
		
	else: v1[i] = v[i]*2
		
		
print(v1)
