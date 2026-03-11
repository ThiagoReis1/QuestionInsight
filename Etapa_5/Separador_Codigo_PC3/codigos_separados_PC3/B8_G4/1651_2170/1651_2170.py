from numpy import*
from numpy.linalg import*
m = input("m: ").upper().split(',')
c = zeros(6,dtype=int)
for i in range(len(m)):
	if m[i]=='MC':
		c[0] = c[0] + 1
	elif m[i]=='C':
		c[1] = c[1] + 1
	elif m[i]=='CM':
		c[2] = c[2] + 1
	elif m[i]=='EM':
		c[3] = c[3] + 1
	elif m[i]=='E':
		c[4] = c[4] + 1
	elif m[i]=='ME':
		c[5] = c[5] + 1
print(max(c))
print(c)