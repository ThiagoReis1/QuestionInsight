from numpy import *

a = input("Digite ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)

am = 0
pe = 0
mg = 0
sp = 0
rs = 0

for i in range(len(v)):
	if v[i] == "AM":
		am += 1
	elif v[i] == "PE":
		pe += 1
	elif v[i] == "MG":
		mg += 1
	elif v[i] == "SP":
		sp += 1
	elif v[i] == "RS":
		rs += 1

vet_z[0] = am
vet_z[1] = pe
vet_z[2] = mg
vet_z[3] = sp
vet_z[4] = rs

print(max(vet_z))
print(vet_z)