from numpy import *

a = input().upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)

AZ = 0
CA = 0
FL = 0
PA = 0
WI = 0

for i in range(len(v)):
	if v[i] == "AZ":
		AZ += 1
	elif v[i] == "CA":
		CA += 1
	elif v[i] == "FL":
		FL += 1
	elif v[i] == "PA":
		PA += 1
	elif v[i] == "WI":
		WI += 1

vet_z[0] = AZ
vet_z[1] = CA
vet_z[2] = FL
vet_z[3] = PA
vet_z[4] = WI

print(max(vet_z))
print(vet_z)
