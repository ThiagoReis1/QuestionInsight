from numpy import * 

v = input('estados: ').split(',')

v0 = zeros(5, dtype=int)

i = 0 

for i in range(len(v)):
	if v[i] == "AZ":
		v0[0] = v0[0] + 1
	elif v[i] == "CA":
		v0[1] = v0[1] + 1
	elif v[i] == "FL":
		v0[2] = v0[2] + 1
	elif v[i] == "PA":
		v0[3] = v0[3] + 1
	elif v[i] == "WI":
		v0[4] = v0[4] + 1
		
print(max(v0))
print(v0)
	
