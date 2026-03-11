from numpy import *

n = array(eval(input()))
t = 0
for i in range(size(n)):
	if n[i] >= 5.0:
		t += 1
print(t)
v = zeros(t, dtype = int)
s = 0
for i in range(size(n)):
	if n[i] >= 5.0:
		v[s] = i
		s += 1
print(v)