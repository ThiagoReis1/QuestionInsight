from numpy import*
vt = array(eval(input(":")))

for a in range(size(vt)):
	if (vt[a] == 9):
		vt[a] = 0
	else:
		vt[a]=vt[a] +1 
print(vt)