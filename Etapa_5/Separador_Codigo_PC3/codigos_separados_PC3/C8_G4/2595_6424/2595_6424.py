from numpy import *
v = array(eval(input()))
i = 0
q = 0
for i in range(size(v)-1):
	i += 1
	if v[i] <= -v[0]:
		q += 1
		print(i)
print(q)