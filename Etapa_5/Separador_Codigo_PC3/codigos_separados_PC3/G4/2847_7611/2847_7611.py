from numpy import*

v = array(eval(input('')))

for i in range(size(v)):
	v[i] = v[i] ** 2
print(v)