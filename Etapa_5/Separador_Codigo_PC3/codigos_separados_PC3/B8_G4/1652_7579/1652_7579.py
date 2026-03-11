from numpy import *
n = (input(": ").upper()).split(",")
v = zeros(5,dtype = int)
for x in n:
	if x == "B":
		v[0] += 1
	elif x == "PA":
		v[1] += 1
	elif x == "PR":
		v[2] += 1
	elif x =="A":
		v[3] += 1
	elif x == "I":
		v[4] += 1
		
print(max(v))
print(v)