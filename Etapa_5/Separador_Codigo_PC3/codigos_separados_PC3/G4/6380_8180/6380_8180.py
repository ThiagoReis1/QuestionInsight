from numpy import*
v = input(": ").split()

i = 0


for i in range(size(v)):
	if(v[i] == "E"):
		vt[0] = vt[0] + 1
	if(v[i] == "V"):
		vt[1] = vt[1] + 1
	if(v[i] == "A"):
		vt[2] = vt[2] + 1
	if(v[i] == "D"):
		vt[3] = vt[3] + 1

print(vt)