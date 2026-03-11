from numpy import*

v = array(eval(input(" vetores a serem substituidos:")))
v1 = zeros(size(v), dtype=int)

for i in range(size(v)):
	v1[i]=v[i]*2

print(v1)