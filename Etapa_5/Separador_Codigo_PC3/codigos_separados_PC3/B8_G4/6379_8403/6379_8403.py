from numpy import *
v = str(input('notas')) .split(',')

c = zeros(5, dtype = int)

for i in range(size(v)):	
	if v[i] == 'A':
		c[0] = c[0] + 1
		
	elif v[i] == 'B':
		c[1] = c[1] + 1
		
	elif v[i] == 'C':
		c[2] = c[2] + 1
		
	elif v[i] == 'D':
		c[3] = c[3] + 1
		
	elif v[i] == 'E':
		c[4] = c[4] + 1
print(c)
