from numpy import *

n = input().upper().split(',')
v = zeros(4, dtype=int)

for i in range(size(n)):
	if n[i] == "C":
		v[0] += 1
	elif n[i] == "D":
		v[1] += 1
	elif n[i] == "V":
		v[2] += 1
	elif n[i] == "U":
		v[3] += 1
print(v)