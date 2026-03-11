from numpy import *
a = input("digite: ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)
AZ = 0
CA = 0
FL = 0
PA = 0
WI = 0

for i in range(len(v)):
	if a[i] == "AZ":
		AZ += 1
	elif a[i] == "CA":
		CA += 1
	elif a[i] == "FL":
		FL += 1
	elif a[i] == "PA":
		PA += 1
	elif a[i] == "WI":
		WI += 1

vet_z[0] = AZ
vet_z[1] = CA
vet_z[2] = FL
vet_z[3] = PA
vet_z[4] = WI

print (max(vet_z))
print (vet_z)