from numpy import*
vt = array(eval(input(": ")))
i = 0
for i in range(size(vt)):
	if(vt[i]<=9):
		vt[i]= vt[i] - 1
	if(vt[i]>9):
		vt[i]