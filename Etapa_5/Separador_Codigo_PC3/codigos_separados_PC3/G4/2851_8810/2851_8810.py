from numpy import *
v = eval(input())
s = 0
for i in range(size(v)):
	if v[i] == 99:
		s = s * 2
	else:
		s = s + v[i]
print(s)
