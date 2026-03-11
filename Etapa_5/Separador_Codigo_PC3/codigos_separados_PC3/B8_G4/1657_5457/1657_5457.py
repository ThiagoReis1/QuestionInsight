from numpy import *

p = input().upper().split(",")

v = zeros(5, dtype=int)

for i in range(size(p)):
	if p[i] == "AZ":
		v[0] = v[0] + 1
	elif p[i] == "CA":
		v[1] = v[1] + 1
	elif p[i] == "FL":
		v[2] = v[2] + 1
	elif p[i] == "PA":
		v[3] = v[3] + 1
	elif p[i] == "WI":
		v[4] = v[4] + 1
print(max(v))
print(v)