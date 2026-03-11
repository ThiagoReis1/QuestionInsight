from numpy import*
v = input("").split(",")

t = zeros(6, dtype=int)
for i in range(size(v)): 
	if v[i] == "MC":
		t[0] += 1
	elif v[i] =="C":
		t[1] += 1
	elif v[i]== "CM":
		t[2] += 1
	elif v [i] =="EM":
		t[3] += 1
	elif v[i] == "E":
		t[4] += 1
	else:
		t[5] += 1
print(max(t))
print(t)

		
	