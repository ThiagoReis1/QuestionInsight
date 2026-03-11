from numpy import *

a = input().upper()
v = a.split(',')
vet_z = zeros(5,dtype = int)

AC = 0
AM = 0
PA = 0
RO = 0
RR = 0

for i in range(len(v)):
	if v[i] == "AC":
		AC += 1
	elif v[i] == "AM":
		AM += 1
	elif v[i] == "PA":
		PA += 1
	elif v[i] == "RO":
		RO += 1
	elif v[i] == "RR":
		RR += 1

vet_z[0] = AC
vet_z[1] = AM
vet_z[2] = PA
vet_z[3] = RO
vet_z[4] = RR

print(max(vet_z))
print(vet_z)
