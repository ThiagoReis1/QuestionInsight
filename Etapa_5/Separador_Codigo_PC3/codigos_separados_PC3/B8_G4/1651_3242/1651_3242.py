from numpy import *

a = input("Digite ").upper()
v = a.split(',')
vet_z = zeros(6, dtype=int)
mc = 0
c = 0
cm = 0
em = 0
e = 0
me = 0

for i in range(len(v)):
	if v[i] == "MC":
		mc += 1
	elif v[i] == "C":
		c += 1
	elif v[i] == "CM":
		cm += 1
	elif v[i] == "EM":
		em += 1
	elif v[i] == "E":
		e += 1
	elif v[i] == "ME":
		me += 1

vet_z[0] = mc
vet_z[1] = c
vet_z[2] = cm
vet_z[3] = em
vet_z[4] = e
vet_z[5] = me

print(max(vet_z))
print(vet_z)