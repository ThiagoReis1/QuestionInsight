from numpy import *

a = input().upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)

CHN = 0
JPN = 0
KOR = 0
MGL = 0
THA = 0

for i in range(len(v)):
	if v[i] == "CHN":
		CHN += 1
	elif v[i] == "JPN":
		JPN += 1
	elif v[i] == "KOR":
		KOR += 1
	elif v[i] == "MGL":
		MGL += 1
	elif v[i] == "THA":
		THA += 1

vet_z[0] = CHN
vet_z[1] = JPN
vet_z[2] = KOR
vet_z[3] = MGL
vet_z[4] = THA

print(max(vet_z))
print(vet_z)