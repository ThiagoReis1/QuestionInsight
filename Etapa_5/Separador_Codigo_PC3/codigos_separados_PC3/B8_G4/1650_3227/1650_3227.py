from numpy import *

a = input("DIgite ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)
p = 0
c = 0
r = 0
l = 0
b = 0

for i in range(len(v)):
	
	if v[i] == "P":
		p += 1
	elif v[i] == "C":
		c += 1
	elif v[i] == "R":
		r += 1
	elif v[i] == "L":
		l += 1
	elif v[i] == "B":
		b += 1

vet_z[0] = p
vet_z[1] = c
vet_z[2] = r
vet_z[3] = l
vet_z[4] = b

print(max(vet_z))
print(vet_z)