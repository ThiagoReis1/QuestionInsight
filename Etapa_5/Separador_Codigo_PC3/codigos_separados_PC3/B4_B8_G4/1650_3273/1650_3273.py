from numpy import *

a = input().upper()
v = a.split(',')
vet_z = zeros(5, dtype = int)

b = 0
l = 0
r = 0
c = 0
p = 0


for i in range(len(v)):
	if v[i] == "B":
		b += 1
	elif v[i] == "L":
		l += 1
	elif v[i] == "R":
		r += 1
	elif v[i] == "C":
		c += 1
	elif v[i] == "P":
		p += 1
	elif v[i] == "B":
		b += 1
	

vet_z[4] = b
vet_z[3] = l
vet_z[2] = r
vet_z[1] = c
vet_z[0] = p

print(max(vet_z))
print(vet_z)
