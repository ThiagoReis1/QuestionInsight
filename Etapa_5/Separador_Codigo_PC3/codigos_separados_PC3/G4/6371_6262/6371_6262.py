from numpy import* 
vt = array(eval(input(":")))
for a in range(size(vt)):
	if vt[a] == 0:
		vt[a] = 9**2
	else:
		vt[a] = (vt[a]-1)**2
print(vt)