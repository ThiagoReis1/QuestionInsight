from numpy import *
v = array(eval(input()))
w = zeros(size(v), dtype = int)

e = -1
for i in range(size(v)):
	w[i] = v[e]
	e = e - 1
print(w)