from numpy import*
from numpy.linalg import*
m = input("m: ").upper().split(',')
c = zeros(5,dtype=int)
for i in range(len(m)):
	if m[i]=='AM':
		c[0] = c[0] + 1
	elif m[i]=='PE':
		c[1] = c[1] + 1
	elif m[i]=='MG':
		c[2] = c[2] + 1
	elif m[i]=='SP':
		c[3] = c[3] + 1
	elif m[i]=='RS':
		c[4] = c[4] + 1
print(max(c))
print(c)