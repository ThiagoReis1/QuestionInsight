from numpy import *
i = array(eval(input()))
u = 0
for k in range(size(i)):
	if i[0]<=i[k] and k!=0:
		u = u + 1
		print(k)
print(u)