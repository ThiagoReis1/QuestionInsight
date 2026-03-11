from numpy import *
v = eval(input())
s = 0
for i in range(size(v)):
	if v[i] > 80:
		v[i] = v[i] - 5
print(round(sum(v),2))