from numpy import *

a = input("Digite ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)

AM = 0
PE = 0
MG = 0
SP = 0
RS = 0

for i in range(len(v)):
	if v[i] == "AM":
		AM += 1
	elif v[i] == "PE":
		PE += 1
	elif v[i] == "MG":
		MG += 1
	elif v[i] == "SP":
		SP += 1
	elif v[i] == "RS":
		RS += 1

vet_z[0] = AM
vet_z[1] = PE
vet_z[2] = MG
vet_z[3] = SP
vet_z[4] = RS

print(max(vet_z))
print(vet_z)