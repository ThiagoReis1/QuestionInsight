from numpy import *
v = array(eval(input("codigo: ")))
for i in range(size(v)):
	if v[i]==0:
		v[i]= 10
	v[i] = (v[i] - 1)**2
print(v)
