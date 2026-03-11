from numpy import *

n = array(eval(input()))
t = 0
for i in range(size(n)):
	if n[i] == 0:
		n[i] = 9 ** 3
	else:
		n[i] = (n[i] - 1) ** 3
print(n)