from numpy import *
v = zeros(4,dtype=int)
e = str(input()).split(",")
for c in e:
	if c == "E":
		v[0] += 1
	if c == "V":
		v[1] += 1
	if c == "A":
		v[2] += 1
	if c == "D":
		v[3] += 1
print(v)