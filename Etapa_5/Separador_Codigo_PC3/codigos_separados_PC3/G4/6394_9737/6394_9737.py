from numpy import*

vt = array(eval(input()))

for i in range(size(vt)):
	if vt[i] == 9:
		vt[i] = 0
	else:
		vt[i] = vt[i] + 1
print(vt)