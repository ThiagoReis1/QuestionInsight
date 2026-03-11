from numpy import *
c = input("Digite: ").upper().split(",")
q = zeros(4, dtype = int)
for i in range(len(c)):
	if c[i] == "A":
		q[0] += 1
	elif c[i] == "B":
		q[1] += 1
	elif c[i] == "L":
		q[2] += 1
	elif c[i] == "H":
		q[3] += 1
print(q)