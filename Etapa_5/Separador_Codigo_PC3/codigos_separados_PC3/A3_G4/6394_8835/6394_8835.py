from numpy import *
n = array(eval(input("")))
v = zeros(size(n), dtype=int)
for i in range(size(n)):
	if n[i] == 9:
		n[i] = 0
	else:
		n[i] = n[i] + 1
print(n)