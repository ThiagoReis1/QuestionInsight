from numpy import *
v = array(eval(input()))

p = 0
while (p < size(v)):
	if (v[p] == min(v)):
		 v[p] = 0
		 p = p + 1
	else:
		 p = p + 1
m = sum(v)/(size(v) - 1)
print(round(m,2))