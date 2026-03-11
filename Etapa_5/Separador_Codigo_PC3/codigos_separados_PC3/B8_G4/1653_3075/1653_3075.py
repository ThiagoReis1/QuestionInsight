from numpy import *
n = input()
n = n.split(',')
b = 0
a = 0
c = 0
o = 0
u = 0
pos = 0
for pos in range(size(n)):
	if (n[pos] == "BR"):
		b = b + 1
	elif (n[pos] == "AR"):
		a = a + 1
	elif (n[pos] == "CL"):
		c = c + 1
	elif (n[pos] == "CO"):
		o = o + 1
	elif (n[pos] == "UY"):
		u = u + 1
	

sa = zeros(5, dtype=int)	
sa[0] = a
sa[1] = b
sa[2] = c 
sa[3] = o
sa[4] = u
print(max(sa))
print(sa)