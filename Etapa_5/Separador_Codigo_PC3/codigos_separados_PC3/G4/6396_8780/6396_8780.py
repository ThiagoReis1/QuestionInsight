from numpy import *
v = array(eval(input()))

j = 0
nv = zeros(size(v), dtype = int)

for i in v:
	nv[j] = i * 2
	j += 1
print(nv)