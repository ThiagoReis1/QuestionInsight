from numpy import *
p = input("nacionalidades: ").split(',')

c = zeros(5, dtype = int)

for i in range(size(p)):
	if p[i] == 'AR':
		c[0] += 1
	elif p[i] == 'BR':
		c[1] += 1
	elif p[i] == 'CL':
		c[2] += 1
	elif p[i] == 'CO':
		c[3] += 1
	elif p[i] == 'UY':
		c[4] += 1
m = max(c)
print(m)
print(c)