from numpy import *
v = input('x').split(',')

c = zeros(5,dtype = int)

for i in range(size(v)):
	if v[i] == 'AR':
		c[0] = c[0] + 1
	
		
	elif v[i] == 'BR':
		c[1] = c[1] + 1
		
		
	elif v[i] == 'CL':
		c[2] = c[2] + 1
	
		
	elif v[i] == 'CO':
		c[3] = c[3] + 1
	
		
	elif v[i] == 'UY':
		c[4] = c[4] + 1
	
		
print(max(c))	
print(c)
