from numpy import *

pa = (input('Digite os paises')).upper() .split(',')
z = zeros(5, dtype = int)
for i in range (size(pa)):
	if pa[i] == 'BE':
		z[0] = z[0] + 1
	elif pa[i] == 'ES':
		z[1] =z[1] + 1
	elif pa[i] == 'FR':
		z[2] = z[2] + 1
	elif pa[i] == 'IT':
		z[3] = z[3] + 1
	else:
		z[4] = z[4] + 1

print(max(z))
print(z)