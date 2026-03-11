from numpy import *
v = array(eval(input("")))
l = 0
print(sum(v))
for i in range(size(v)):
	if v[i]>=5:
		l = l + 1
print(l)
	