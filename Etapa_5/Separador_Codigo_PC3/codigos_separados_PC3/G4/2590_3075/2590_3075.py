from numpy import *
r = array(eval(input()))
n = 0
for i in range(size(r)):
	if (r[i] < r[0]):
		print(i)
		n = n + 1
print(n)