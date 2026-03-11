from numpy import*
s = input(" ").split(",")
v = zeros(4, dtype=int)
for e in s:
	if e == "A":
		v[0] = v[0]+1
	if e == "B":
		v[1] = v[1]+1
	if e == "C":
		v[2] = v[2]+1
	if e == "D":
		v[3] = v[3]+1
print(v)