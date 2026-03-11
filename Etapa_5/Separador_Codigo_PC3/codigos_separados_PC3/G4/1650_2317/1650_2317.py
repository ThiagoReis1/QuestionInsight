from numpy import*
v = input("").split(",")

t = zeros(5, dtype=int)
for i in range(size(v)):
	if v[i] == "P":
		t[0]+=1
	elif v[i] == "C":
		t[1]+=1
	elif v[i] == "R":
		t[2] += 1
	elif v[i] == "L":
		t[3] += 1
	else:
		t[4] += 1
	
print(max(t))
print(t)