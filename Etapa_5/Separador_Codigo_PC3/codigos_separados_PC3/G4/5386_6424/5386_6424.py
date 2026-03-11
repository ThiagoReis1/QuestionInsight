from numpy import *
x = str(input()).upper()
l = array(x)
a = []
for c in range(size(l)):
	if 'A' in l:
		a.append(1)
print(a)