from numpy import*

vt = array(eval(input()))
c = zeros(size(vt), dtype=int)

for i in range(size(vt)):
	if(vt[i] == 9):
		c[i] = 0
	else:
		c[i] = vt[i] + 1
print(c)