from numpy import *

a = input("Digite ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)
ac = 0
am = 0
pa = 0
ro = 0
rr = 0

for i in range(len(v)):
	if v[i] == "AC":
		ac += 1
	elif v[i] == "AM":
		am += 1
	elif v[i] == "PA":
		pa += 1
	elif v[i] == "RO":
		ro += 1
	elif v[i] == "RR":
		rr += 1

vet_z[0] = ac
vet_z[1] = am
vet_z[2] = pa
vet_z[3] = ro
vet_z[4] = rr

print(max(vet_z))
print(vet_z)