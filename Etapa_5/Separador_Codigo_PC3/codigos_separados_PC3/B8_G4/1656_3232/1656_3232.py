from numpy import *

a = input("Digite ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)

be = 0
es = 0
fr = 0
it = 0
pt = 0

for i in range(len(v)):
	if v[i] == "BE":
		be += 1
	elif v[i] == "ES":
		es += 1
	elif v[i] == "FR":
		fr += 1
	elif v[i] == "IT":
		it += 1
	elif v[i] == "PT":
		pt += 1

vet_z[0] = be
vet_z[1] = es
vet_z[2] = fr
vet_z[3] = it
vet_z[4] = pt

print(max(vet_z))
print(vet_z)